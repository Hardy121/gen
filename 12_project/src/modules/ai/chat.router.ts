import { Router } from "express";
import { z } from "zod";
import { asyncHandler } from "../../utils/async-handler.js"; 
import { create } from "./chat.controller.js";

const router = Router();

// router.get("/chat", asyncHandler(create));


export default router;
