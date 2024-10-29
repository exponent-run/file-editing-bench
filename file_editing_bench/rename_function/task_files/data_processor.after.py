def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def filter_negative_values(data):
    """
    Removes all negative values from a list.
    """
    return [x for x in data if x >= 0]

def process_time_series(timestamps, values):
    """
    Combines timestamp and value lists into a list of tuples,
    sorted by timestamp.
    """
    return sorted(zip(timestamps, values))

def gen_report(data, include_summary=True):
    """
    Generates a report from the processed data including
    basic statistics and filtered values.
    """
    filtered_data = filter_negative_values(data)
    stats = {
        'original_count': len(data),
        'filtered_count': len(filtered_data),
        'average': calculate_average(filtered_data)
    }
    
    if include_summary:
        stats['summary'] = f"Processed {len(data)} values, removed {len(data) - len(filtered_data)} negative values"
    
    return stats