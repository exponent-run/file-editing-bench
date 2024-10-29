interface UserStats {
  totalLogins: number;
  lastLoginDate: Date;
  accountType: 'free' | 'premium';
}

/**
 * Processes user statistics and returns a formatted summary
 * for administrative purposes.
 */
function generateUserStatsSummary(stats: UserStats, lookbackDays: number): string {
  const daysAgo = new Date();
  daysAgo.setDate(daysAgo.getDate() - lookbackDays);
  
  const isRecentlyActive = stats.lastLoginDate >= daysAgo;
  const accountStatus = stats.accountType === 'premium' ? 'Premium Member' : 'Free Tier';
  
  const activityLevel = 
    stats.totalLogins > lookbackDays * 2 ? 'High' :
    stats.totalLogins > lookbackDays ? 'Medium' : 'Low';

  return `User Activity Summary:
    Account Type: ${accountStatus}
    Activity Level: ${activityLevel}
    Recently Active: ${isRecentlyActive ? 'Yes' : 'No'}
    Login Frequency: ${(stats.totalLogins / lookbackDays).toFixed(2)} logins/day`;
}