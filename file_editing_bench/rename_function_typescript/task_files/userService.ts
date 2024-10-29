import { User, UserPreferences } from './types';
import { DatabaseClient } from './database';

export class UserService {
  private db: DatabaseClient;
  
  constructor(db: DatabaseClient) {
    this.db = db;
  }

  async getUser(userId: string): Promise<User | null> {
    return this.db.findOne('users', { id: userId });
  }

  async p(userId: string, preferences: Partial<UserPreferences>): Promise<void> {
    const user = await this.getUser(userId);
    if (!user) {
      throw new Error('User not found');
    }

    const updatedPreferences = {
      ...user.preferences,
      ...preferences,
      lastModified: new Date()
    };

    await this.db.update('users', 
      { id: userId },
      { preferences: updatedPreferences }
    );
  }

  async deleteUser(userId: string): Promise<void> {
    await this.db.delete('users', { id: userId });
  }
}