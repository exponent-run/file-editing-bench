interface DataPoint {
    timestamp: number;
    value: number;
}

class Util {
    static formatTimestamp(timestamp: number): string {
        return new Date(timestamp).toISOString();
    }

    static calculateAverage(values: number[]): number {
        return values.reduce((a, b) => a + b, 0) / values.length;
    }
}

class Proc {
    private dataPoints: DataPoint[] = [];
    private readonly maxDataPoints: number;

    constructor(maxPoints: number = 1000) {
        this.maxDataPoints = maxPoints;
    }

    addDataPoint(value: number): void {
        const point: DataPoint = {
            timestamp: Date.now(),
            value: value
        };

        this.dataPoints.push(point);
        if (this.dataPoints.length > this.maxDataPoints) {
            this.dataPoints.shift();
        }
    }

    getAverageValue(): number {
        return Util.calculateAverage(this.dataPoints.map(p => p.value));
    }

    getFormattedData(): string[] {
        return this.dataPoints.map(point => 
            `${Util.formatTimestamp(point.timestamp)}: ${point.value}`
        );
    }
}

class DataVisualizer {
    private readonly processor: Proc;

    constructor(maxDataPoints: number) {
        this.processor = new Proc(maxDataPoints);
    }

    addValue(value: number): void {
        this.processor.addDataPoint(value);
    }

    generateReport(): string {
        const avg = this.processor.getAverageValue();
        const formattedData = this.processor.getFormattedData();
        
        return `
Data Points:
${formattedData.join('\n')}

Average Value: ${avg}
        `.trim();
    }
}

export { DataPoint, Util, Proc, DataVisualizer };