import { User, UserRole } from './types';

export class UserService {
    private validateUserPermissions(user: User, requiredRole: UserRole): boolean {
        if (!user || !user.role) {
            return false;
        }
        
        return user.role >= requiredRole;
    }

    async updateUserProfile(userId: string, profileData: Partial<User>): Promise<User> {
        const user = await this.getUserById(userId);
        
        if (!this.validateUserPermissions(user, UserRole.USER)) {
            throw new Error('Insufficient permissions to update profile');
        }

        // Remove sensitive fields that shouldn't be updated
        delete profileData.role;
        delete profileData.id;

        const updatedUser = {
            ...user,
            ...profileData,
            updatedAt: new Date()
        };

        return await this.saveUser(updatedUser);
    }

    private async getUserById(id: string): Promise<User> {
        // Implementation omitted for brevity
        return {} as User;
    }

    private async saveUser(user: User): Promise<User> {
        // Implementation omitted for brevity
        return user;
    }
}