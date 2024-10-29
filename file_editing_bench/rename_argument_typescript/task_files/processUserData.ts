interface UserStats {
  totalLogins: number;
  lastLoginDate: Date;
  accountType: 'free' | 'premium';
}

/**
 * Processes user statistics and returns a formatted summary
 * for administrative purposes.
 */
function generateUserStatsSummary(stats: UserStats, d: number): string {
  const daysAgo = new Date();
  daysAgo.setDate(daysAgo.getDate() - d);
  
  const isRecentlyActive = stats.lastLoginDate >= daysAgo;
  const accountStatus = stats.accountType === 'premium' ? 'Premium Member' : 'Free Tier';
  
  const activityLevel = 
    stats.totalLogins > d * 2 ? 'High' :
    stats.totalLogins > d ? 'Medium' : 'Low';

  return `User Activity Summary:
    Account Type: ${accountStatus}
    Activity Level: ${activityLevel}
    Recently Active: ${isRecentlyActive ? 'Yes' : 'No'}
    Login Frequency: ${(stats.totalLogins / d).toFixed(2)} logins/day`;
}