import { Router } from "express";
import { z } from "zod";
import { asyncHandler } from "../../utils/async-handler.js";
import { usersController } from "./users.controller.js";

const router = Router();

const createUserSchema = z.object({
  name: z.string().trim().min(2).max(100),
  email: z.string().trim().email().max(254),
}).strict();

const updateUserSchema = z.object({
  name: z.string().trim().min(2).max(100).optional(),
  email: z.string().trim().email().max(254).optional(),
}).strict().refine(
  (data) => Object.keys(data).length > 0,
  "Provide at least one field to update"
);

router.post(
  "/",
  (req, res, next) => {
    const result = createUserSchema.safeParse(req.body);

    if (!result.success) {
      return res.status(400).json({
        success: false,
        errors: result.error.issues,
      });
    }

    req.body = result.data;
    next();
  },
  asyncHandler(usersController.create)
);

router.get("/", asyncHandler(usersController.findAll));

router.get("/:id", asyncHandler(usersController.findById));

router.patch(
  "/:id",
  (req, res, next) => {
    const result = updateUserSchema.safeParse(req.body);

    if (!result.success) {
      return res.status(400).json({
        success: false,
        errors: result.error.issues,
      });
    }

    req.body = result.data;
    next();
  },
  asyncHandler(usersController.update)
);

router.delete("/:id", asyncHandler(usersController.delete));

export default router;
