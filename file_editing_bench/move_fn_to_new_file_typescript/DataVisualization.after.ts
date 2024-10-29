import { ChartData, ChartOptions } from './types';
import { preprocessTimeSeriesData } from './timeSeriesUtils';

export class DataVisualization {
    private chartData: ChartData;
    private options: ChartOptions;

    constructor(data: ChartData, options: ChartOptions) {
        this.chartData = data;
        this.options = options;
    }

    public renderChart(): void {
        const processedData = preprocessTimeSeriesData(this.chartData);
        // ... rendering logic
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