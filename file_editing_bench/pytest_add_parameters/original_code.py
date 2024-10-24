import pytest
from datetime import datetime, timedelta

def calculate_age(birthdate: datetime) -> int:
    today = datetime.now()
    age = today.year - birthdate.year
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1
    return age

def test_calculate_age():
    birthdate = datetime(1990, 6, 15)
    age = calculate_age(birthdate)
    assert isinstance(age, int)
    assert age >= 0

def test_future_date():
    future_date = datetime.now() + timedelta(days=365)
    with pytest.raises(ValueError):
        calculate_age(future_date)