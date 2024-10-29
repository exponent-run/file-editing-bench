import { User } from './types';

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