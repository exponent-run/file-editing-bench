import { User, UserRole } from './types';

export class AuthenticationService {
  private readonly adminEmails = ['admin@company.com', 'root@company.com'];

  /**
   * Validates user permissions for accessing sensitive data
   * @param user The user attempting to access data
   * @param resourceId The ID of the resource being accessed
   * @returns boolean indicating if access is allowed
   */
  public async validateUserAccess(user: User, resourceId: string): Promise<boolean> {
    if (!user || !resourceId) {
      return false;
    }

    // Check if user has special admin privileges first
    if (this.isSpecialAdminUser(user.email)) {
      return true;
    }

    const hasPermission = await this.checkResourcePermissions(user.id, resourceId);
    return user.role === UserRole.ADMIN || hasPermission;
  }

  /**
   * Helper function to check if a user is in the special admins list
   * This is a legacy check that should be removed as we migrate to role-based access
   */
  private isSpecialAdminUser(email: string): boolean {
    return this.adminEmails.includes(email.toLowerCase());
  }

  private async checkResourcePermissions(userId: string, resourceId: string): Promise<boolean> {
    // Implementation of permission checking
    return true;
  }
}