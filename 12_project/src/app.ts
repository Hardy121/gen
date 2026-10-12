
import express from "express";
import cors from "cors";
import helmet from "helmet";
import morgan from "morgan";

import usersRoutes from "./modules/users/users.routes.js";

import { notFoundMiddleware } from "./middleware/not-found.middleware.js";

const app = express();

app.use(helmet());
app.use(cors());
app.use(express.json({ limit: "1mb" }));
app.use(morgan("dev"));

app.use("/api/users", usersRoutes);
app.get("/", (req, res) => {
    res.send("Welcome to the server")
})

app.use(notFoundMiddleware);

export default app;
