import { Database } from './types';

interface MetricPayload {
  name: string;
  value: number;
  timestamp: number;
  tags?: Record<string, string>;
}

// Helper class for data validation
class ValidationUtils {
  static isValidMetricName(name: string): boolean {
    return /^[a-zA-Z][a-zA-Z0-9_\.]*$/.test(name);
  }

  static isValidTimestamp(timestamp: number): boolean {
    return timestamp > 0 && timestamp <= Date.now();
  }
}

// This class processes and batches metrics
class MetricBatchProcessor {
  private db: Database;
  private readonly batchSize: number = 100;
  private metricQueue: MetricPayload[] = [];
  
  constructor(db: Database, batchSize?: number) {
    this.db = db;
    if (batchSize) this.batchSize = batchSize;
  }

  async addMetric(metric: MetricPayload): Promise<void> {
    if (!ValidationUtils.isValidMetricName(metric.name)) {
      throw new Error('Invalid metric name');
    }
    if (!ValidationUtils.isValidTimestamp(metric.timestamp)) {
      throw new Error('Invalid timestamp');
    }

    this.metricQueue.push(metric);
    
    if (this.metricQueue.length >= this.batchSize) {
      await this.flush();
    }
  }

  async flush(): Promise<void> {
    if (this.metricQueue.length === 0) return;

    const metrics = [...this.metricQueue];
    this.metricQueue = [];
    
    await this.db.batchInsert('metrics', metrics);
  }

  getQueueSize(): number {
    return this.metricQueue.length;
  }
}

// Analytics dashboard configuration
class DashboardConfig {
  constructor(
    public readonly refreshInterval: number = 60000,
    public readonly defaultTimeRange: string = '24h'
  ) {}
}

export { MetricBatchProcessor, ValidationUtils, DashboardConfig, MetricPayload };