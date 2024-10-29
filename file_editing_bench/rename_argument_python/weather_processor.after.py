def process_weather_data(temperature_readings, temp_threshold, include_metadata=False):
    """
    Process weather data to identify significant temperature changes.
    
    Args:
        temperature_readings: List of hourly temperature readings
        temp_threshold: Minimum temperature change to be considered significant
        include_metadata: Whether to include processing metadata in output
    """
    significant_changes = []
    for i in range(1, len(temperature_readings)):
        temp_diff = abs(temperature_readings[i] - temperature_readings[i-1])
        if temp_diff >= temp_threshold:
            significant_changes.append({
                'hour': i,
                'previous_temp': temperature_readings[i-1],
                'current_temp': temperature_readings[i],
                'change': temp_diff
            })
    
    if include_metadata:
        return {
            'changes': significant_changes,
            'total_readings': len(temperature_readings),
            'changes_detected': len(significant_changes)
        }
    
    return significant_changes