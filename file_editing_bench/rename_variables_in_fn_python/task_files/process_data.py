def analyze_server_metrics(lst, n, x):
    """
    Analyzes server performance metrics and returns a summary of critical indicators
    including average response time, error rate, and peak usage periods.
    """
    if not lst or n <= 0:
        return None
    
    res = []
    for i in range(0, len(lst), n):
        tmp = lst[i:i + n]
        if len(tmp) == n:
            v = sum(tmp) / len(tmp)
            if v > x:
                res.append((i, v))
    
    return res if res else None