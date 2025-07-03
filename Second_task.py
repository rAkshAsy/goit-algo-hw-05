import re
from typing import Callable, Generator
from decimal import Decimal

def generator_numbers(text: str) -> Generator[str, None, None]:

    # Pattern for floating-point numbers with two decimal places
    pattern = r' \d+\.\d* '

    # Find and yield all matched numbers one by one
    for number in re.findall(pattern, text):
        yield number


def sum_profit(text: str, operation: Callable[[str], Generator[str, None, None]]) -> Decimal:

    # Convert strings to Decimal and return the sum of all numbers yielded by the generator
    return sum(Decimal(num) for num in operation(text))


# Test cases and a loop to run them

texts = [
    "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.",
    "Компанія виплатила 230.50 як зарплату, а ще 15.00 — як бонус за відпустку.",
    "Надходження включають: 100.00, 200.00, 50.00 — разом утворюють повний дохід.",
    "У звіті зазначено лише одне джерело прибутку: 9999.99.",
    "Цього разу прибутків не було. Все 10.00.",
    "Тимчасово доступні лише такі кошти: 13.37 і 42.00."
]

for text in texts:
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
