import { v4 as uuidv4 } from 'uuid';
import { DateTime } from 'luxon';
import { validateItemName } from './utils';

// Item rarity enum
export enum ItemRarity {
  COMMON = 'COMMON',
  UNCOMMON = 'UNCOMMON',
  RARE = 'RARE',
  EPIC = 'EPIC',
  LEGENDARY = 'LEGENDARY'
}

// Item interface
export interface InventoryItem {
  id: string;
  name: string;
  description: string;
  value: number;
  rarity: ItemRarity;
  acquiredAt: string;
}

function calculateDiscount(value: number, rarity: ItemRarity): number {
  const currentHour = DateTime.now().hour;
  // Apply "happy hour" discount between 2-4 PM
  if (currentHour >= 14 && currentHour < 16) {
    return value * 0.9; // 10% discount
  }
  return value;
}

function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2
  }).format(amount);
}

function generateItemDescription(name: string, rarity: ItemRarity): string {
  const rarityDescriptions = {
    [ItemRarity.COMMON]: 'A common',
    [ItemRarity.UNCOMMON]: 'An uncommon',
    [ItemRarity.RARE]: 'A rare',
    [ItemRarity.EPIC]: 'An epic',
    [ItemRarity.LEGENDARY]: 'A legendary'
  };

  return `${rarityDescriptions[rarity]} ${name.toLowerCase()} of great interest.`;
}

function sortByRarity(items: InventoryItem[]): InventoryItem[] {
  const rarityOrder = {
    [ItemRarity.LEGENDARY]: 0,
    [ItemRarity.EPIC]: 1,
    [ItemRarity.RARE]: 2,
    [ItemRarity.UNCOMMON]: 3,
    [ItemRarity.COMMON]: 4
  };

  return items.sort((a, b) => rarityOrder[a.rarity] - rarityOrder[b.rarity]);
}

function calculateTotalValue(items: InventoryItem[]): number {
  return items.reduce((total, item) => total + item.value, 0);
}

export class InventoryManager {
  private items: InventoryItem[] = [];

  addItem(name: string, value: number, rarity: ItemRarity): InventoryItem {
    validateItemName(name);
    
    const description = generateItemDescription(name, rarity);
    const discountedValue = calculateDiscount(value, rarity);
    
    const item: InventoryItem = {
      id: uuidv4(),
      name,
      description,
      value: discountedValue,
      rarity,
      acquiredAt: DateTime.now().toISO()
    };

    this.items.push(item);
    return item;
  }

  getItemsSortedByRarity(): InventoryItem[] {
    return sortByRarity([...this.items]);
  }

  getTotalValue(): string {
    const total = calculateTotalValue(this.items);
    return formatCurrency(total);
  }

  getItemById(id: string): InventoryItem | undefined {
    return this.items.find(item => item.id === id);
  }
}