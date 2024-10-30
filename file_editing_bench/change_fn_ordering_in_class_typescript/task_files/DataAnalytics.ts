class DataAnalytics {
    private data: number[];
    private processedData: Map<string, number>;

    constructor(initialData: number[]) {
        this.data = initialData;
        this.processedData = new Map();
    }

    calculateMedian(): number {
        const sorted = [...this.data].sort((a, b) => a - b);
        const mid = Math.floor(sorted.length / 2);
        return sorted.length % 2 === 0
            ? (sorted[mid - 1] + sorted[mid]) / 2
            : sorted[mid];
    }

    private validateData(): boolean {
        return this.data.every(item => typeof item === 'number' && !isNaN(item));
    }

    getProcessedResults(): Map<string, number> {
        return this.processedData;
    }

    calculateMean(): number {
        return this.data.reduce((sum, val) => sum + val, 0) / this.data.length;
    }

    addDataPoint(value: number): void {
        this.data.push(value);
        this.processData();
    }

    private processData(): void {
        if (!this.validateData()) {
            throw new Error("Invalid data detected");
        }
        this.processedData.set('mean', this.calculateMean());
        this.processedData.set('median', this.calculateMedian());
        this.processedData.set('stdDev', this.calculateStandardDeviation());
    }

    calculateStandardDeviation(): number {
        const mean = this.calculateMean();
        const squareDiffs = this.data.map(value => {
            const diff = value - mean;
            return diff * diff;
        });
        return Math.sqrt(squareDiffs.reduce((sum, val) => sum + val, 0) / this.data.length);
    }

    getData(): number[] {
        return [...this.data];
    }
}