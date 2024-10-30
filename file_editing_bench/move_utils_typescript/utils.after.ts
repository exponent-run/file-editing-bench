import { z } from 'zod';

// Schema for item name validation
const itemNameSchema = z.string()
  .min(3, 'Item name must be at least 3 characters')
  .max(50, 'Item name must not exceed 50 characters')
  .regex(/^[a-zA-Z0-9\s-]+$/, 'Item name can only contain letters, numbers, spaces, and hyphens');

export function validateItemName(name: string): void {
  try {
    itemNameSchema.parse(name);
  } catch (error) {
    if (error instanceof z.ZodError) {
      throw new Error(`Invalid item name: ${error.errors[0].message}`);
    }
    throw error;
  }
}