import { UserSession } from './types';

// Global configuration for authentication
const maxLoginAttempts = 3;

export class AuthenticationService {
    private currentAttempts: number = 0;

    constructor() {
        this.resetAttempts();
    }

    async authenticateUser(username: string, password: string): Promise<UserSession | null> {
        if (this.currentAttempts >= maxLoginAttempts) {
            throw new Error('Account locked due to too many failed attempts');
        }

        // Simulate authentication logic
        if (username === 'admin' && password === 'secret') {
            this.resetAttempts();
            return {
                id: '123',
                username,
                lastLoginTimestamp: Date.now(),
                remainingAttempts: maxLoginAttempts
            };
        }

        this.currentAttempts++;
        const remainingTries = maxLoginAttempts - this.currentAttempts;
        throw new Error(`Invalid credentials. ${remainingTries} attempts remaining before lockout`);
    }

    private resetAttempts(): void {
        this.currentAttempts = 0;
        console.log(`Login attempts reset. Maximum of ${maxLoginAttempts} attempts allowed`);
    }
}

export function getMaxAttempts(): number {
    return maxLoginAttempts;
}