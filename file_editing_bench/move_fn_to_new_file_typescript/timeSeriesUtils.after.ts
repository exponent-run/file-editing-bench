import { ChartData } from './types';

export function preprocessTimeSeriesData(data: ChartData): ChartData {
    const movingAverageWindow = 7;
    const result = { ...data };
    
    if (Array.isArray(data.values)) {
        result.values = data.values.map((value, index) => {
            const windowStart = Math.max(0, index - movingAverageWindow + 1);
            const windowValues = data.values.slice(windowStart, index + 1);
            const sum = windowValues.reduce((acc, val) => acc + val, 0);
            return sum / windowValues.length;
        });
    }

    return result;
}