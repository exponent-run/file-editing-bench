interface DataPoint {
    timestamp: number;
    value: number;
    label: string;
}

export function calculateAverage(data: DataPoint[]): number {
    if (data.length === 0) return 0;
    return data.reduce((sum, point) => sum + point.value, 0) / data.length;
}

export function findMinValue(data: DataPoint[]): number {
    if (data.length === 0) throw new Error("Empty dataset");
    return Math.min(...data.map(point => point.value));
}

export function findMaxValue(data: DataPoint[]): number {
    if (data.length === 0) throw new Error("Empty dataset");
    return Math.max(...data.map(point => point.value));
}

export function normalizeValues(data: DataPoint[]): DataPoint[] {
    const maxValue = Math.max(...data.map(point => point.value));
    return data.map(point => ({
        ...point,
        value: point.value / maxValue
    }));
}

export function sortByTimestamp(data: DataPoint[]): DataPoint[] {
    return [...data].sort((a, b) => a.timestamp - b.timestamp);
}

export function filterByTimeRange(data: DataPoint[], start: number, end: number): DataPoint[] {
    return data.filter(point => point.timestamp >= start && point.timestamp <= end);
}

export function findOutliers(data: DataPoint[], threshold: number): DataPoint[] {
    const avg = calculateAverage(data);
    return data.filter(point => Math.abs(point.value - avg) > threshold);
}

export function groupByLabel(data: DataPoint[]): Map<string, DataPoint[]> {
    return data.reduce((groups, point) => {
        const currentGroup = groups.get(point.label) || [];
        groups.set(point.label, [...currentGroup, point]);
        return groups;
    }, new Map<string, DataPoint[]>());
}