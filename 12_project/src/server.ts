
import app from "./app.js";
import { connectDatabase } from "./config/database.js";
import { env } from "./config/env.js";

async function startServer(): Promise<void> {
  try {
    await connectDatabase();

    const server = app.listen(env.PORT, () => {
      console.log(`Server running at http://localhost:${env.PORT}`);
    });

    const shutdown = () => {
      console.log("Shutting down server...");

      server.close(() => {
        console.log("HTTP server closed");
        process.exit(0);
      });
    };

    process.on("SIGINT", shutdown);
    process.on("SIGTERM", shutdown);
  } catch (error) {
    console.error("Failed to start server:", error);
    process.exit(1);
  }
}

void startServer();
