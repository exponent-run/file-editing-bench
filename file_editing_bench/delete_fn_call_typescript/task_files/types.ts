export enum UserRole {
    GUEST = 0,
    USER = 1,
    ADMIN = 2
}

export interface User {
    id: string;
    role: UserRole;
    name: string;
    email: string;
    updatedAt: Date;
}