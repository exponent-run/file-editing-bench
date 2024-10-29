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

/**
 * Creates a new session token for a user
 * @param userId The ID of the user to create a session for
 * @param deviceId Optional device identifier
 * @returns The generated session token
 */
export function createSessionToken(userId: string, deviceId?: string): string {
    const timestamp = Date.now();
    const randomPart = Math.random().toString(36).substring(2);
    const sessionData = `${userId}-${timestamp}-${deviceId || 'web'}-${randomPart}`;
    return Buffer.from(sessionData).toString('base64');
}