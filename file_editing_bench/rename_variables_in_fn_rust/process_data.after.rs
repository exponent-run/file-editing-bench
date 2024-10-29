use std::collections::HashMap;

pub fn analyze_server_metrics(metrics_values: Vec<i32>, metric_indices: HashMap<String, i32>, threshold: i32) -> f64 {
    let mut s = 0;
    
    // Calculate sum of all values above threshold
    for n in metrics_values.iter() {
        if *n > threshold {
            s += n;
        }
    }

    // Apply weights from the mapping
    let mut r = 0.0;
    for (k, v) in metric_indices.iter() {
        if let Some(n) = metrics_values.get(*v as usize) {
            r += *n as f64 * calculate_weight(k);
        }
    }

    // Return weighted average
    if s > 0 {
        r / s as f64
    } else {
        0.0
    }
}

fn calculate_weight(metric_name: &str) -> f64 {
    match metric_name {
        "cpu" => 2.0,
        "memory" => 1.5,
        _ => 1.0,
    }
}