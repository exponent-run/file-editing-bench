pub struct Metric {
    index: usize,
    value: f64,
}

fn calculate_weight(val: f64) -> f64 {
    (val * 100.0).round() / 100.0
}

pub fn analyze_server_metrics(values: Vec<f64>, metric_indices: Vec<usize>, threshold: f64) -> Option<f64> {
    if values.is_empty() || metric_indices.is_empty() {
        return None;
    }

    let mut weighted_sum = 0.0;
    for index in metric_indices.iter() {
        if *index >= values.len() {
            return None;
        }
        
        if values[*index] > threshold {
            weighted_sum += calculate_weight(values[*index]);
        }
    }

    if weighted_sum > 0.0 {
        Some(weighted_sum)
    } else {
        None
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_analyze_metrics() {
        let values = vec![1.5, 2.7, 3.2, 4.8, 5.1];
        let indices = vec![1, 3, 4];
        assert_eq!(analyze_server_metrics(values, indices, 3.0), Some(12.60));
    }
}