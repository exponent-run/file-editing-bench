import sys
import os
import pytest
from typing import List, Dict, Any

# Mock the TypeScript interfaces and classes in Python
class UserEvent:
    def __init__(self, user_id: str, event_type: str, timestamp: int, platform: str, session_duration: int):
        self.userId = user_id
        self.eventType = event_type
        self.timestamp = timestamp
        self.metadata = {
            "platform": platform,
            "deviceType": "mobile",
            "country": "US",
            "sessionDuration": session_duration
        }

def create_test_events() -> List[Dict[str, Any]]:
    return [
        UserEvent("user1", "interaction", 1000, "web", 120),
        UserEvent("user1", "purchase", 1100, "web", 180),
        UserEvent("user2", "interaction", 1200, "mobile", 300),
        UserEvent("user3", "interaction", 1300, "desktop", 150),
        UserEvent("user2", "purchase", 1400, "mobile", 250),
    ]

def test_analytics_processor():
    # Import the TypeScript file using node
    test_events = create_test_events()
    
    # Convert test events to JSON string
    events_str = str(test_events)
    
    # Create a temporary test file that will import and use the analytics.ts file
    test_code = f'''
    const {{ AnalyticsProcessor }} = require('./analytics.ts');
    
    const testEvents = {events_str};
    const processor = new AnalyticsProcessor();
    const result = processor.processUserEngagement(testEvents);
    
    console.log(JSON.stringify(result));
    '''
    
    with open('temp_test.js', 'w') as f:
        f.write(test_code)
    
    # Run the test file using Node.js and capture output
    result = os.popen('node -r ts-node/register temp_test.js').read()
    
    # Parse the result
    import json
    output = json.loads(result)
    
    # Verify the output matches expected values
    assert output['totalEngagement'] == 5
    assert abs(output['avgSessionTime'] - 200.0) < 0.01  # Average of all session durations
    assert set(output['topPlatforms']) == {'mobile', 'web', 'desktop'}  # All platforms used
    assert set(output['activeUsers']) == {'user1', 'user2', 'user3'}  # All users who interacted or purchased

    # Clean up
    os.remove('temp_test.js')

if __name__ == "__main__":
    test_analytics_processor()