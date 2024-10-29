interface UserData {
    id: number;
    name: string;
    email: string;
    preferences: {
        theme: 'light' | 'dark';
        notifications: boolean;
    };
}

function validateEmailFormat(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email) && email.length <= 255;
}

function processUserRegistration(userData: UserData): { success: boolean; message: string } {
    if (!userData.name || userData.name.length < 2) {
        return { success: false, message: 'Name must be at least 2 characters long' };
    }

    if (!validateEmailFormat(userData.email)) {
        return { success: false, message: 'Invalid email format' };
    }

    // Process the valid user data
    return {
        success: true,
        message: `User ${userData.name} registered successfully with ${userData.preferences.theme} theme preference`
    };
}