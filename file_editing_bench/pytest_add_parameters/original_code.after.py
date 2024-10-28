import pytest
from datetime import datetime, timedelta


def calculate_age(birthdate: datetime) -> int:
    today = datetime.now()
    if birthdate > today:
        raise ValueError("Birthdate cannot be in the future")
    age = today.year - birthdate.year
    if today.month < birthdate.month or (
        today.month == birthdate.month and today.day < birthdate.day
    ):
        age -= 1
    return age


@pytest.mark.parametrize(
    "birthdate,expected_age",
    [
        (datetime(1990, 1, 1), 33),
        (datetime(2000, 12, 31), 22),
        (datetime(1985, 6, 15), 38),
        (datetime(1995, 8, 20), 28),
    ],
)
def test_calculate_age(birthdate: datetime, expected_age: int):
    age = calculate_age(birthdate)
    assert isinstance(age, int)
    assert age == expected_age


@pytest.mark.parametrize(
    "invalid_date",
    [
        datetime.now() + timedelta(days=1),
        datetime.now() + timedelta(days=365),
        datetime.now() + timedelta(days=3650),
    ],
    ids=["tomorrow", "next_year", "ten_years"],
)
def test_future_date(invalid_date: datetime):
    with pytest.raises(ValueError, match="Birthdate cannot be in the future"):
        calculate_age(invalid_date)
