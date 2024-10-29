import { format } from 'date-fns';
import { z } from 'zod';
import { BigNumber } from 'bignumber.js';
import { Either, left, right } from 'fp-ts/Either';
import { pipe } from 'fp-ts/function';
import { isNil, isEmpty } from 'lodash';

// Validation utilities
export const validateAmount = (amount: string): Either<string, BigNumber> => {
  if (isEmpty(amount)) {
    return left('Amount cannot be empty');
  }
  const num = new BigNumber(amount);
  return num.isNaN() ? left('Invalid amount format') : right(num);
};

export const validateDate = (date: string): Either<string, Date> => {
  const parsed = new Date(date);
  return isNaN(parsed.getTime()) 
    ? left('Invalid date format')
    : right(parsed);
};

export const formatCurrency = (amount: BigNumber): string => {
  return `$${amount.toFormat(2)}`;
};

export const sanitizeInput = (input: string): string => {
  return input.trim().replace(/[<>]/g, '');
};

export const generateTransactionId = (): string => {
  return `TXN-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
};

export const parseCSVRow = (row: string): string[] => {
  return row
    .split(',')
    .map(cell => cell.trim())
    .filter(cell => !isEmpty(cell));
};