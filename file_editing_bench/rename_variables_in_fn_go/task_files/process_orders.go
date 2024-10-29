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
	var t float64
	var n int
	var f []Order

	for _, v := range o {
		if v.CreatedAt.After(time.Now().Add(-24 * time.Hour)) {
			if v.Status == "completed" {
				t += v.Total
				n++
				f = append(f, v)
			}
		}
	}

	return t, n, nil
}