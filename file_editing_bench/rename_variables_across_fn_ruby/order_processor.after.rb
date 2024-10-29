class OrderProcessor
  def initialize
    @discount_amount = 0
  end

  def process_order(items)
    items.each do |item|
      @discount_amount += calculate_item_discount(item)
    end
    
    apply_final_adjustments
  end

  def calculate_item_discount(item)
    if item.on_sale?
      discount_amount = item.price * 0.1
      record_discount(discount_amount)
      discount_amount
    else
      0
    end
  end

  def apply_final_adjustments
    if @discount_amount > 100
      @discount_amount = 100
    end
    @discount_amount
  end

  private

  def record_discount(discount_amount)
    puts "Recording discount of #{discount_amount}"
  end
end