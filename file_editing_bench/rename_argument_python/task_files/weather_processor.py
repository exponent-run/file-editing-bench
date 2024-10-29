def process_weather_data(d, temp_threshold, include_metadata=False):
    """
    Process weather data to identify significant temperature changes.
    
    Args:
        d: List of hourly temperature readings
        temp_threshold: Minimum temperature change to be considered significant
        include_metadata: Whether to include processing metadata in output
    """
    significant_changes = []
    for i in range(1, len(d)):
        temp_diff = abs(d[i] - d[i-1])
        if temp_diff >= temp_threshold:
            significant_changes.append({
                'hour': i,
                'previous_temp': d[i-1],
                'current_temp': d[i],
                'change': temp_diff
            })
    
    if include_metadata:
        return {
            'changes': significant_changes,
            'total_readings': len(d),
            'changes_detected': len(significant_changes)
        }
    
    return significant_changes