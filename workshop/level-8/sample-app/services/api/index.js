/**
 * Simple API service — Level 8 sample.
 * Intentionally minimal: the focus is on Copilot CLI features, not the app.
 */

const http = require("http");

const PORT = process.env.PORT || 3000;

const routes = {
  "GET /": () => ({ status: "ok", service: "api", version: "1.0.0" }),
  "GET /health": () => ({ healthy: true, uptime: process.uptime() }),
  "GET /events": () => ({
    events: [
      { id: 1, title: "Workshop A", date: "2026-03-01" },
      { id: 2, title: "Workshop B", date: "2026-03-15" },
    ],
  }),
};

const server = http.createServer((req, res) => {
  const key = `${req.method} ${req.url}`;
  const handler = routes[key];

  res.setHeader("Content-Type", "application/json");

  if (handler) {
    res.writeHead(200);
    res.end(JSON.stringify(handler()));
  } else {
    res.writeHead(404);
    res.end(JSON.stringify({ error: "Not found" }));
  }
});

if (require.main === module) {
  server.listen(PORT, () => {
    console.log(`API service listening on port ${PORT}`);
  });
}

module.exports = { server, routes };
