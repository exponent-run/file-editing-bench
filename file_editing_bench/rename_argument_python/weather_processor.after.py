def process_weather_data(weather_entries, temp_threshold, include_precipitation=False):
    """Process weather station data and identify significant weather events."""
    processed_data = []
    
    for entry in weather_entries:
        if entry['temperature'] > temp_threshold:
            event = {
                'timestamp': entry['timestamp'],
                'station_id': entry['station_id'],
                'event_type': 'high_temperature',
                'value': entry['temperature']
            }
            
            if include_precipitation and entry.get('precipitation', 0) > 0:
                event['precipitation_mm'] = entry['precipitation']
            
            processed_data.append(event)
    
    return processed_data