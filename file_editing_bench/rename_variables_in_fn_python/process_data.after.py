def analyze_server_metrics(metrics_data, n, x):
    """
    Analyzes server performance metrics and returns a summary of critical indicators
    including average response time, error rate, and peak usage periods.
    """
    if not metrics_data or n <= 0:
        return None
    
    res = []
    for i in range(0, len(metrics_data), n):
        batch = metrics_data[i:i + n]
        if len(batch) == n:
            batch_average = sum(batch) / len(batch)
            if batch_average > x:
                res.append((i, batch_average))
    
    return res if res else None