import { BigNumber } from 'bignumber.js';
import { Either, left, right } from 'fp-ts/Either';
import { isEmpty } from 'lodash';

export const validateAmount = (amount: string): Either<string, BigNumber> => {
  if (isEmpty(amount)) {
    return left('Amount cannot be empty');
  }
  const num = new BigNumber(amount);
  return num.isNaN() ? left('Invalid amount format') : right(num);
};