interface DataPoint {
    timestamp: number;
    value: number;
    label?: string;
}

export function calculateAverage(data: DataPoint[]): number {
    if (data.length === 0) return 0;
    return data.reduce((sum, point) => sum + point.value, 0) / data.length;
}

export function filterByTimeRange(data: DataPoint[], startTime: number, endTime: number): DataPoint[] {
    return data.filter(point => point.timestamp >= startTime && point.timestamp <= endTime);
}

export function findMaxValue(data: DataPoint[]): number {
    if (data.length === 0) throw new Error("Empty dataset");
    return Math.max(...data.map(point => point.value));
}

export function normalizeData(data: DataPoint[]): DataPoint[] {
    const maxVal = findMaxValue(data);
    return data.map(point => ({
        ...point,
        value: point.value / maxVal
    }));
}

export function groupByLabel(data: DataPoint[]): Map<string, DataPoint[]> {
    return data.reduce((groups, point) => {
        const label = point.label || 'undefined';
        const group = groups.get(label) || [];
        groups.set(label, [...group, point]);
        return groups;
    }, new Map<string, DataPoint[]>());
}

export function findMinValue(data: DataPoint[]): number {
    if (data.length === 0) throw new Error("Empty dataset");
    return Math.min(...data.map(point => point.value));
}

export function standardizeData(data: DataPoint[]): DataPoint[] {
    const avg = calculateAverage(data);
    const squaredDiffs = data.map(point => Math.pow(point.value - avg, 2));
    const stdDev = Math.sqrt(squaredDiffs.reduce((sum, diff) => sum + diff, 0) / data.length);
    
    return data.map(point => ({
        ...point,
        value: (point.value - avg) / stdDev
    }));
}

export function sortByTimestamp(data: DataPoint[]): DataPoint[] {
    return [...data].sort((a, b) => a.timestamp - b.timestamp);
}