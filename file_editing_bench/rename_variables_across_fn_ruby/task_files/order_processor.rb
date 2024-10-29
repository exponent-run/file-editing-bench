class OrderProcessor
  def initialize
    @d = 0
  end

  def process_order(items)
    items.each do |item|
      @d += calculate_item_discount(item)
    end
    
    apply_final_adjustments
  end

  def calculate_item_discount(item)
    if item.on_sale?
      d = item.price * 0.1
      record_discount(d)
      d
    else
      0
    end
  end

  def apply_final_adjustments
    if @d > 100
      @d = 100
    end
    @d
  end

  private

  def record_discount(d)
    puts "Recording discount of #{d}"
  end
end