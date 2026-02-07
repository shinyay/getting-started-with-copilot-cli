"""
Background worker service — Level 8 sample.
Intentionally minimal: the focus is on Copilot CLI features, not the app.
"""

import time
import json
import os
import sys


QUEUE_FILE = os.environ.get("QUEUE_FILE", "jobs.json")
POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "5"))


def load_jobs():
    """Load pending jobs from the queue file."""
    if not os.path.exists(QUEUE_FILE):
        return []
    try:
        with open(QUEUE_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_jobs(jobs):
    """Save jobs back to the queue file."""
    with open(QUEUE_FILE, "w") as f:
        json.dump(jobs, f, indent=2)


def process_job(job):
    """Process a single job."""
    job_type = job.get("type", "unknown")
    print(f"Processing job: {job.get('id', '?')} (type={job_type})")

    if job_type == "send_email":
        print(f"  → Sending email to {job.get('to', 'unknown')}")
        time.sleep(0.5)  # Simulate work
    elif job_type == "generate_report":
        print(f"  → Generating report: {job.get('report_name', 'unknown')}")
        time.sleep(1.0)
    else:
        print(f"  → Unknown job type: {job_type}")

    return True


def run_worker():
    """Main worker loop."""
    print(f"Worker started. Polling {QUEUE_FILE} every {POLL_INTERVAL}s")

    while True:
        jobs = load_jobs()
        pending = [j for j in jobs if j.get("status") == "pending"]

        if pending:
            for job in pending:
                success = process_job(job)
                job["status"] = "completed" if success else "failed"
            save_jobs(jobs)
            print(f"Processed {len(pending)} job(s)")
        else:
            print("No pending jobs")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    if "--once" in sys.argv:
        jobs = load_jobs()
        pending = [j for j in jobs if j.get("status") == "pending"]
        for job in pending:
            process_job(job)
            job["status"] = "completed"
        save_jobs(jobs)
        print(f"Processed {len(pending)} job(s), exiting.")
    else:
        run_worker()
