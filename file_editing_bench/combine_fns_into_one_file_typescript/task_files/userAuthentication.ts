import { User } from './types';

/**
 * Validates a user's password against stored hash
 * @param password The plain text password to validate
 * @param storedHash The stored password hash
 * @returns boolean indicating if the password is valid
 */
export function validateUserPassword(password: string, storedHash: string): boolean {
    // Simulated password validation logic
    const salt = storedHash.split('.')[0];
    const hash = computeHash(password, salt);
    return hash === storedHash;
}

function computeHash(password: string, salt: string): string {
    // Simulated hash computation
    return `${salt}.${password.split('').reverse().join('')}`;
}