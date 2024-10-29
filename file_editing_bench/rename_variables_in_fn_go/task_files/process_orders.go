package orders

import (
	"time"
)

// ProcessDailyOrders calculates total revenue and generates summary statistics
// for orders processed within the last 24 hours
func ProcessDailyOrders(orders []Order) (*DailySummary, error) {
	var t float64
	var n int
	var f []*Order

	for _, o := range orders {
		if time.Since(o.CreatedAt) <= 24*time.Hour {
			t += o.Amount
			n++
			if o.Status == "completed" {
				f = append(f, &o)
			}
		}
	}

	if n == 0 {
		return nil, ErrNoOrders
	}

	return &DailySummary{
		TotalRevenue:      t,
		ProcessedOrders:   n,
		CompletedOrders:   f,
		AverageOrderValue: t / float64(n),
	}, nil
}