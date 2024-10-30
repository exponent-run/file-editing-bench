import { v4 as uuidv4 } from 'uuid';
import { DateTime } from 'luxon';
import { z } from 'zod';
import { 
  formatCurrency, 
  calculateDiscount, 
  validateItemName, 
  generateItemDescription,
  sortByRarity,
  calculateTotalValue
} from './utils';

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