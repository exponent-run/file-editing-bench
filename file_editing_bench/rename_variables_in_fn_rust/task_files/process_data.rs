use std::collections::HashMap;

pub fn analyze_server_metrics(x: Vec<i32>, m: HashMap<String, i32>, t: i32) -> f64 {
    let mut s = 0;
    
    // Calculate sum of all values above threshold
    for n in x.iter() {
        if *n > t {
            s += n;
        }
    }

    // Apply weights from the mapping
    let mut r = 0.0;
    for (k, v) in m.iter() {
        if let Some(n) = x.get(*v as usize) {
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