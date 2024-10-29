import { format } from 'date-fns';
import { BigNumber } from 'bignumber.js';
import { Either, left, right } from 'fp-ts/Either';
import { pipe } from 'fp-ts/function';
import { z } from 'zod';
import { readFileSync } from 'fs';
import { 
  validateAmount, 
  validateDate, 
  formatCurrency, 
  sanitizeInput,
  generateTransactionId,
  parseCSVRow
} from './utils';

// Types
interface Transaction {
  id: string;
  date: Date;
  amount: BigNumber;
  description: string;
  category: string;
}

interface ProcessedTransaction extends Transaction {
  formattedAmount: string;
  formattedDate: string;
}

// Schema for CSV validation
const TransactionSchema = z.object({
  date: z.string(),
  amount: z.string(),
  description: z.string(),
  category: z.string()
});

export class TransactionProcessor {
  private transactions: Transaction[] = [];

  public processTransaction(rawData: unknown): Either<string, ProcessedTransaction> {
    const result = TransactionSchema.safeParse(rawData);
    
    if (!result.success) {
      return left('Invalid transaction format');
    }

    const { date, amount, description, category } = result.data;

    return pipe(
      validateDate(date),
      Either.chain(validDate => 
        pipe(
          validateAmount(amount),
          Either.map(validAmount => ({
            id: generateTransactionId(),
            date: validDate,
            amount: validAmount,
            description: sanitizeInput(description),
            category: sanitizeInput(category),
            formattedAmount: formatCurrency(validAmount),
            formattedDate: format(validDate, 'yyyy-MM-dd')
          }))
        )
      )
    );
  }

  public importTransactionsFromCSV(filePath: string): Either<string, ProcessedTransaction[]> {
    try {
      const fileContent = readFileSync(filePath, 'utf-8');
      const rows = fileContent.split('\n').slice(1); // Skip header
      
      const processedTransactions: ProcessedTransaction[] = [];
      
      for (const row of rows) {
        const [date, amount, description, category] = parseCSVRow(row);
        
        const result = this.processTransaction({
          date,
          amount,
          description,
          category
        });
        
        if (Either.isLeft(result)) {
          return left(`Error processing row: ${row}`);
        }
        
        processedTransactions.push(result.right);
      }
      
      return right(processedTransactions);
    } catch (error) {
      return left(`Failed to read CSV file: ${error.message}`);
    }
  }

  public getTransactionsByCategory(category: string): ProcessedTransaction[] {
    return this.transactions.filter(t => t.category === sanitizeInput(category))
      .map(t => ({
        ...t,
        formattedAmount: formatCurrency(t.amount),
        formattedDate: format(t.date, 'yyyy-MM-dd')
      }));
  }
}