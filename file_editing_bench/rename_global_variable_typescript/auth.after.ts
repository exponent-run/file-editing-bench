import { UserSession } from './types';

// Global configuration for authentication
const MAX_LOGIN_ATTEMPTS = 3;

export class AuthenticationService {
    private currentAttempts: number = 0;

    constructor() {
        this.resetAttempts();
    }

    async authenticateUser(username: string, password: string): Promise<UserSession | null> {
        if (this.currentAttempts >= MAX_LOGIN_ATTEMPTS) {
            throw new Error('Account locked due to too many failed attempts');
        }

        // Simulate authentication logic
        if (username === 'admin' && password === 'secret') {
            this.resetAttempts();
            return {
                id: '123',
                username,
                lastLoginTimestamp: Date.now(),
                remainingAttempts: MAX_LOGIN_ATTEMPTS
            };
        }

        this.currentAttempts++;
        const remainingTries = MAX_LOGIN_ATTEMPTS - this.currentAttempts;
        throw new Error(`Invalid credentials. ${remainingTries} attempts remaining before lockout`);
    }

    private resetAttempts(): void {
        this.currentAttempts = 0;
        console.log(`Login attempts reset. Maximum of ${MAX_LOGIN_ATTEMPTS} attempts allowed`);
    }
}

export function getMaxAttempts(): number {
    return MAX_LOGIN_ATTEMPTS;
}