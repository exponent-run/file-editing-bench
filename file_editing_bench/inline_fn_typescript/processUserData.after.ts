interface UserData {
    id: number;
    name: string;
    email: string;
    preferences: {
        theme: 'light' | 'dark';
        notifications: boolean;
    };
}

function processUserRegistration(userData: UserData): { success: boolean; message: string } {
    if (!userData.name || userData.name.length < 2) {
        return { success: false, message: 'Name must be at least 2 characters long' };
    }

    if (!((/^[^\s@]+@[^\s@]+\.[^\s@]+$/).test(userData.email) && userData.email.length <= 255)) {
        return { success: false, message: 'Invalid email format' };
    }

    // Process the valid user data
    return {
        success: true,
        message: `User ${userData.name} successfully registered with email ${userData.email}`
    };
}