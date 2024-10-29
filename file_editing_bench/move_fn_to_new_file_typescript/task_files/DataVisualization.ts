import { ChartData, ChartOptions } from './types';

export class DataVisualization {
    private chartData: ChartData;
    private options: ChartOptions;

    constructor(data: ChartData, options: ChartOptions) {
        this.chartData = data;
        this.options = options;
    }

    public renderChart(): void {
        const processedData = this.preprocessTimeSeriesData(this.chartData);
        // ... rendering logic
    }

    private preprocessTimeSeriesData(data: ChartData): ChartData {
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
}

export interface ChartData {
    values: number[];
    labels?: string[];
    timeRange?: [Date, Date];
}

export interface ChartOptions {
    width: number;
    height: number;
    backgroundColor: string;
    showLegend: boolean;
}