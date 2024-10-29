pub struct Metric {
    index: usize,
    value: f64,
}

fn calculate_weight(val: f64) -> f64 {
    (val * 100.0).round() / 100.0
}

pub fn analyze_server_metrics(x: Vec<f64>, m: Vec<usize>, t: f64) -> Option<f64> {
    if x.is_empty() || m.is_empty() {
        return None;
    }

    let mut result = 0.0;
    for i in m.iter() {
        if *i >= x.len() {
            return None;
        }
        
        if x[*i] > t {
            result += calculate_weight(x[*i]);
        }
    }

    if result > 0.0 {
        Some(result)
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