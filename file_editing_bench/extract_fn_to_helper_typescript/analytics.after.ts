interface UserEvent {
  userId: string;
  eventType: string;
  timestamp: number;
  metadata: Record<string, any>;
}

interface ProcessedAnalytics {
  userId: string;
  totalEvents: number;
  lastEventTime: number;
  eventBreakdown: Record<string, number>;
  averageEventsPerDay: number;
  mostFrequentEvent: string;
  hasRecentActivity: boolean;
}

function findMostFrequentEvent(eventCounts: Record<string, number>): string {
  let maxCount = 0;
  let mostFrequentEvent = '';
  Object.entries(eventCounts).forEach(([eventType, count]) => {
    if (count > maxCount) {
      maxCount = count;
      mostFrequentEvent = eventType;
    }
  });
  return mostFrequentEvent;
}

export function processUserAnalytics(events: UserEvent[]): ProcessedAnalytics {
  const userId = events[0]?.userId || '';
  const eventCounts: Record<string, number> = {};
  let lastEventTime = 0;

  // Count events and track the last event time
  events.forEach(event => {
    eventCounts[event.eventType] = (eventCounts[event.eventType] || 0) + 1;
    lastEventTime = Math.max(lastEventTime, event.timestamp);
  });

  const mostFrequentEvent = findMostFrequentEvent(eventCounts);

  // Calculate events per day
  const firstEventTime = Math.min(...events.map(e => e.timestamp));
  const daysDifference = (lastEventTime - firstEventTime) / (1000 * 60 * 60 * 24);
  const averageEventsPerDay = events.length / (daysDifference || 1);

  // Check for recent activity (within last 24 hours)
  const now = Date.now();
  const hasRecentActivity = (now - lastEventTime) < (24 * 60 * 60 * 1000);

  return {
    userId,
    totalEvents: events.length,
    lastEventTime,
    eventBreakdown: eventCounts,
    averageEventsPerDay,
    mostFrequentEvent,
    hasRecentActivity
  };
}