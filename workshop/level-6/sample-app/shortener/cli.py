"""CLI entry point for URL Shortener."""

import argparse
import sys
import re
from shortener.store import shorten, expand, delete, list_all, get_entry
from shortener.stats import get_summary


# Duplicated validation (also exists in validator.py — refactoring target)
def _quick_validate(url: str) -> bool:
    """Quick URL validation — duplicated from validator.py."""
    if not url or len(url) > 2048:
        return False
    return bool(re.match(r"^https?://\S+", url))


def cmd_shorten(args):
    """Handle the 'shorten' subcommand."""
    url = args.url

    # Uses local validation instead of validator module (duplication)
    if not _quick_validate(url):
        # Try adding scheme
        if not url.startswith(("http://", "https://")):
            url = f"https://{url}"
        if not _quick_validate(url):
            print(f"Error: Invalid URL: {args.url}", file=sys.stderr)
            sys.exit(1)

    try:
        result = shorten(url, custom_code=args.code)
        print(f"Shortened: {result['code']} → {result['url']}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_expand(args):
    """Handle the 'expand' subcommand."""
    try:
        url = expand(args.code)
        print(f"Expanded: {args.code} → {url}")
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_delete(args):
    """Handle the 'delete' subcommand."""
    if delete(args.code):
        print(f"Deleted: {args.code}")
    else:
        print(f"Not found: {args.code}", file=sys.stderr)
        sys.exit(1)


def cmd_list(args):
    """Handle the 'list' subcommand."""
    entries = list_all()
    if not entries:
        print("No URLs stored.")
        return

    for entry in entries:
        accessed = entry.get("access_count", 0)
        print(f"  {entry['code']}  →  {entry['url']}  (accessed: {accessed})")

    print(f"\nTotal: {len(entries)} URLs")


def cmd_stats(args):
    """Handle the 'stats' subcommand."""
    print(get_summary())


def cmd_info(args):
    """Handle the 'info' subcommand."""
    try:
        entry = get_entry(args.code)
        print(f"Code:       {entry['code']}")
        print(f"URL:        {entry['url']}")
        print(f"Created:    {entry.get('created_at', 'unknown')}")
        print(f"Accessed:   {entry.get('access_count', 0)} times")
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        prog="shortener",
        description="URL Shortener CLI — shorten, expand, and manage URLs"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # shorten
    p_shorten = subparsers.add_parser("shorten", help="Shorten a URL")
    p_shorten.add_argument("url", help="URL to shorten")
    p_shorten.add_argument("--code", help="Custom short code (optional)")
    p_shorten.set_defaults(func=cmd_shorten)

    # expand
    p_expand = subparsers.add_parser("expand", help="Expand a short code to its URL")
    p_expand.add_argument("code", help="Short code to expand")
    p_expand.set_defaults(func=cmd_expand)

    # delete
    p_delete = subparsers.add_parser("delete", help="Delete a short code")
    p_delete.add_argument("code", help="Short code to delete")
    p_delete.set_defaults(func=cmd_delete)

    # list
    p_list = subparsers.add_parser("list", help="List all shortened URLs")
    p_list.set_defaults(func=cmd_list)

    # stats
    p_stats = subparsers.add_parser("stats", help="Show usage statistics")
    p_stats.set_defaults(func=cmd_stats)

    # info
    p_info = subparsers.add_parser("info", help="Show details for a short code")
    p_info.add_argument("code", help="Short code to look up")
    p_info.set_defaults(func=cmd_info)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)


if __name__ == "__main__":
    main()
