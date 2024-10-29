import { v4 as uuidv4 } from 'uuid';
import { trackEvent } from '@segment/analytics-node';
import { Logger } from './logger';

const logger = new Logger('analytics');

export async function trackPageView(url: string, userId?: string): Promise<void> {
    const eventId = uuidv4();
    try {
        await trackEvent({
            event: 'page_view',
            userId: userId || 'anonymous',
            properties: {
                url,
                timestamp: new Date().toISOString(),
                eventId
            }
        });
        logger.info(`Tracked page view: ${url}`);
    } catch (error) {
        logger.error(`Failed to track page view: ${error}`);
    }
}

export async function trackUserEngagement(
    userId: string,
    actionType: 'click' | 'scroll' | 'hover',
    elementId: string
): Promise<void> {
    try {
        await trackEvent({
            event: 'user_engagement',
            userId,
            properties: {
                actionType,
                elementId,
                timestamp: new Date().toISOString()
            }
        });
        logger.debug(`Tracked user engagement: ${actionType} on ${elementId}`);
    } catch (error) {
        logger.error(`Failed to track user engagement: ${error}`);
    }
}