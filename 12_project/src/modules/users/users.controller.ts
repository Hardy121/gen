
import type { Request, Response } from "express";
import mongoose from "mongoose";
import { usersService } from "./users.service.js";
import type {
  CreateUserInput,
  UpdateUserInput,
} from "./users.types.js";

export const usersController = {
  async create(req: Request, res: Response) {
    const user = await usersService.create(
      req.body as CreateUserInput
    );

    res.status(201).json({
      success: true,
      data: user,
    });
  },

  async findAll(_req: Request, res: Response) {
    const users = await usersService.findAll();

    res.status(200).json({
      success: true,
      data: users,
    });
  },

  async findById(req: Request, res: Response) {
    if (!mongoose.isValidObjectId(req.params.id)) {
      return res.status(400).json({
        success: false,
        message: "Invalid user ID",
      });
    }

    const user = await usersService.findById(req.params.id);

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found",
      });
    }

    return res.status(200).json({
      success: true,
      data: user,
    });
  },

  async update(req: Request, res: Response) {
    if (!mongoose.isValidObjectId(req.params.id)) {
      return res.status(400).json({
        success: false,
        message: "Invalid user ID",
      });
    }

    const user = await usersService.update(
      req.params.id,
      req.body as UpdateUserInput
    );

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found",
      });
    }

    return res.status(200).json({
      success: true,
      data: user,
    });
  },

  async delete(req: Request, res: Response) {
    if (!mongoose.isValidObjectId(req.params.id)) {
      return res.status(400).json({
        success: false,
        message: "Invalid user ID",
      });
    }

    const user = await usersService.delete(req.params.id);

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found",
      });
    }

    return res.status(200).json({
      success: true,
      message: "User deleted successfully",
    });
  },
};
