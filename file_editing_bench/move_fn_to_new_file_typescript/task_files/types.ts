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