import pytest
from datetime import datetime
from freezegun import freeze_time
from task_files.order_processor import OrderProcessor, Order, OrderItem


@pytest.fixture
def processor():
    return OrderProcessor()


def test_calculate_discounted_price_exists(processor):
    """Test that the calculate_discounted_price method exists"""
    assert hasattr(processor, 'calculate_discounted_price'), "calculate_discounted_price method should exist"


def test_basic_order_processing(processor):
    """Test that basic order processing still works"""
    order = Order(
        order_id="123",
        customer_id="customer1",
        items=[
            OrderItem(
                product_id="prod1",
                quantity=2,
                unit_price=10.0,
                category="general"
            )
        ],
        created_at=datetime.now()
    )
    
    total = processor.process_order(order)
    assert total == 20.0


def test_electronics_bulk_discount(processor):
    """Test electronics bulk discount is applied correctly"""
    order = Order(
        order_id="124",
        customer_id="customer1",
        items=[
            OrderItem(
                product_id="prod2",
                quantity=3,
                unit_price=100.0,
                category="electronics"
            )
        ],
        created_at=datetime.now()
    )
    
    total = processor.process_order(order)
    assert total == 255.0  # 300 * 0.85


def test_books_bulk_discount(processor):
    """Test books bulk discount is applied correctly"""
    order = Order(
        order_id="125",
        customer_id="customer1",
        items=[
            OrderItem(
                product_id="prod3",
                quantity=5,
                unit_price=20.0,
                category="books"
            )
        ],
        created_at=datetime.now()
    )
    
    total = processor.process_order(order)
    assert total == 90.0  # 100 * 0.90


@freeze_time("2023-12-25")
def test_clothing_seasonal_discount(processor):
    """Test clothing seasonal discount is applied correctly in December"""
    order = Order(
        order_id="126",
        customer_id="customer1",
        items=[
            OrderItem(
                product_id="prod4",
                quantity=1,
                unit_price=100.0,
                category="clothing"
            )
        ],
        created_at=datetime.now()
    )
    
    total = processor.process_order(order)
    assert total == 95.0  # 100 * 0.95


def test_invalid_quantity(processor):
    """Test that invalid quantity raises ValueError"""
    item = OrderItem(
        product_id="prod5",
        quantity=0,
        unit_price=10.0,
        category="general"
    )
    with pytest.raises(ValueError, match="Invalid quantity for product prod5"):
        processor.calculate_discounted_price(item)


def test_invalid_price(processor):
    """Test that invalid price raises ValueError"""
    item = OrderItem(
        product_id="prod6",
        quantity=1,
        unit_price=-10.0,
        category="general"
    )
    with pytest.raises(ValueError, match="Invalid price for product prod6"):
        processor.calculate_discounted_price(item)


def test_empty_order(processor):
    """Test that empty order raises ValueError"""
    order = Order(
        order_id="127",
        customer_id="customer1",
        items=[],
        created_at=datetime.now()
    )
    with pytest.raises(ValueError, match="Order must contain at least one item"):
        processor.process_order(order)