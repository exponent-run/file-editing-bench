interface UserEvent {
  userId: string;
  eventType: string;
  timestamp: number;
  metadata: {
    platform: string;
    deviceType: string;
    country: string;
    sessionDuration: number;
  };
}

export class AnalyticsProcessor {
  private calculatePlatformMetrics(events: UserEvent[]): [{ [key: string]: number }, number, Set<string>] {
    const uniqueUsers = new Set<string>();
    let totalSessionTime = 0;
    const platformCounts: { [key: string]: number } = {};
    
    for (const event of events) {
      const platform = event.metadata.platform;
      platformCounts[platform] = (platformCounts[platform] || 0) + 1;
      
      if (event.metadata.sessionDuration > 0) {
        totalSessionTime += event.metadata.sessionDuration;
      }
      
      if (event.eventType === 'interaction' || event.eventType === 'purchase') {
        uniqueUsers.add(event.userId);
      }
    }

    return [platformCounts, totalSessionTime, uniqueUsers];
  }

  processUserEngagement(events: UserEvent[]): { 
    totalEngagement: number;
    avgSessionTime: number;
    topPlatforms: string[];
    activeUsers: string[];
  } {
    const [platformCounts, totalSessionTime, uniqueUsers] = this.calculatePlatformMetrics(events);

    const sortedPlatforms = Object.entries(platformCounts)
      .sort(([, a], [, b]) => b - a)
      .slice(0, 3)
      .map(([platform]) => platform);

    return {
      totalEngagement: events.length,
      avgSessionTime: totalSessionTime / events.length,
      topPlatforms: sortedPlatforms,
      activeUsers: Array.from(uniqueUsers)
    };
  }
}