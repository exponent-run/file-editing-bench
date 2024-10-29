package orders

import (
	"time"
)

// ProcessDailyOrders calculates total revenue and generates summary statistics
// for orders processed within the last 24 hours
func ProcessDailyOrders(orders []Order) (*DailySummary, error) {
	var totalRevenue float64
	var orderCount int
	var completedOrders []*Order

	for _, o := range orders {
		if time.Since(o.CreatedAt) <= 24*time.Hour {
			totalRevenue += o.Amount
			orderCount++
			if o.Status == "completed" {
				completedOrders = append(completedOrders, &o)
			}
		}
	}

	if orderCount == 0 {
		return nil, ErrNoOrders
	}

	return &DailySummary{
		TotalRevenue:      totalRevenue,
		ProcessedOrders:   orderCount,
		CompletedOrders:   completedOrders,
		AverageOrderValue: totalRevenue / float64(orderCount),
	}, nil
}