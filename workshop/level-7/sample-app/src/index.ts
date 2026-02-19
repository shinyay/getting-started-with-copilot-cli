/**
 * Application entry point.
 */

import express from "express";
import eventRoutes from "./routes/events";
import { errorHandler } from "./middleware/errorHandler";
import { logger } from "./utils/logger";

const app = express();
const PORT = parseInt(process.env.PORT || "3000");

app.use(express.json());
app.use("/api/events", eventRoutes);
app.use(errorHandler);

app.listen(PORT, () => {
  logger.info(`Event API listening on port ${PORT}`);
});

export default app;
