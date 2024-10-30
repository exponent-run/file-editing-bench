import { z } from 'zod';
import { DateTime } from 'luxon';
import { ItemRarity, InventoryItem } from './inventory';

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

export function calculateDiscount(value: number, rarity: ItemRarity): number {
  const currentHour = DateTime.now().hour;
  // Apply "happy hour" discount between 2-4 PM
  if (currentHour >= 14 && currentHour < 16) {
    return value * 0.9; // 10% discount
  }
  return value;
}

export function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2
  }).format(amount);
}

export function generateItemDescription(name: string, rarity: ItemRarity): string {
  const rarityDescriptions = {
    [ItemRarity.COMMON]: 'A common',
    [ItemRarity.UNCOMMON]: 'An uncommon',
    [ItemRarity.RARE]: 'A rare',
    [ItemRarity.EPIC]: 'An epic',
    [ItemRarity.LEGENDARY]: 'A legendary'
  };

  return `${rarityDescriptions[rarity]} ${name.toLowerCase()} of great interest.`;
}

export function sortByRarity(items: InventoryItem[]): InventoryItem[] {
  const rarityOrder = {
    [ItemRarity.LEGENDARY]: 0,
    [ItemRarity.EPIC]: 1,
    [ItemRarity.RARE]: 2,
    [ItemRarity.UNCOMMON]: 3,
    [ItemRarity.COMMON]: 4
  };

  return items.sort((a, b) => rarityOrder[a.rarity] - rarityOrder[b.rarity]);
}

export function calculateTotalValue(items: InventoryItem[]): number {
  return items.reduce((total, item) => total + item.value, 0);
}