import { User } from './types';
import { validateEmail } from './validation';
import { hashPassword } from './security';
import { DatabaseConnection } from './database';
import { sendWelcomeEmail } from './notifications';

export async function createUser(email: string, password: string): Promise<User> {
    if (!validateEmail(email)) {
        throw new Error('Invalid email format');
    }
    
    const hashedPassword = await hashPassword(password);
    const db = new DatabaseConnection();
    
    const user = await db.users.create({
        email,
        password: hashedPassword,
    });
    
    await sendWelcomeEmail(user.email);
    return user;
}

export async function deleteUser(userId: string): Promise<void> {
    const db = new DatabaseConnection();
    await db.users.delete({ id: userId });
}

export async function sendPasswordReset(email: string): Promise<void> {
    if (!validateEmail(email)) {
        throw new Error('Invalid email format');
    }
    
    const db = new DatabaseConnection();
    const user = await db.users.findOne({ email });
    
    if (!user) {
        throw new Error('User not found');
    }
    
    await sendWelcomeEmail(user.email);
}