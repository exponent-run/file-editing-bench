interface UserCredentials {
  email: string;
  password: string;
}

export class AuthenticationService {
  private readonly tokenExpirationMs = 3600000; // 1 hour

  async validateUserCredentials(p: UserCredentials, t: number = this.tokenExpirationMs): Promise<{
    isValid: boolean;
    token?: string;
    expiresAt?: Date;
  }> {
    if (!this.isValidEmail(p.email) || !this.isStrongPassword(p.password)) {
      return { isValid: false };
    }

    const token = await this.generateSecureToken();
    const expiresAt = new Date(Date.now() + t);

    return {
      isValid: true,
      token,
      expiresAt,
    };
  }

  private isValidEmail(email: string): boolean {
    return email.includes('@') && email.includes('.');
  }

  private isStrongPassword(password: string): boolean {
    return password.length >= 8;
  }

  private async generateSecureToken(): Promise<string> {
    return 'generated-token-' + Math.random().toString(36);
  }
}