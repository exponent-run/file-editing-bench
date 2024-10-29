package orders

import (
	"time"
)

type Order struct {
	ID        int64
	Total     float64
	CreatedAt time.Time
	Status    string
}

func ProcessDailyOrders(o []Order) (float64, int, error) {
	var totalRevenue float64
	var orderCount int
	var completedOrders []Order

	for _, v := range o {
		if v.CreatedAt.After(time.Now().Add(-24 * time.Hour)) {
			if v.Status == "completed" {
				totalRevenue += v.Total
				orderCount++
				completedOrders = append(completedOrders, v)
			}
		}
	}

	return totalRevenue, orderCount, nil
}