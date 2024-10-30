import { User } from './types';

const maxLoginAttempts = 3;

export class AuthenticationService {
    private loginAttempts: Map<string, number> = new Map();

    async authenticateUser(username: string, password: string): Promise<User | null> {
        const currentAttempts = this.loginAttempts.get(username) || 0;
        
        if (currentAttempts >= maxLoginAttempts) {
            throw new Error('Account locked due to too many failed attempts');
        }

        // Simulate authentication logic
        if (password === 'correct-password') {
            this.loginAttempts.delete(username);
            return { id: '123', username, roles: ['user'] };
        }

        this.loginAttempts.set(username, currentAttempts + 1);
        
        if (currentAttempts + 1 >= maxLoginAttempts) {
            console.log(`User ${username} reached maximum login attempts of ${maxLoginAttempts}`);
        }

        return null;
    }

    resetLoginAttempts(username: string): void {
        if (this.loginAttempts.get(username) >= maxLoginAttempts) {
            console.log(`Resetting attempts counter from ${maxLoginAttempts} to 0`);
        }
        this.loginAttempts.delete(username);
    }
}

export function getMaxAttempts(): number {
    return maxLoginAttempts;
}