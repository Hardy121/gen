
import { User } from "./users.schema.js";
import type {
  CreateUserInput,
  UpdateUserInput,
} from "./users.types.js";

export const usersService = {
  async create(data: CreateUserInput) {
    return User.create(data);
  },

  async findAll() {
    return User.find().sort({ createdAt: -1 }).lean();
  },

  async findById(id: string) {
    return User.findById(id);
  },

  async update(id: string, data: UpdateUserInput) {
    return User.findByIdAndUpdate(id, data, {
      new: true,
      runValidators: true,
    });
  },

  async delete(id: string) {
    return User.findByIdAndDelete(id);
  },
};
