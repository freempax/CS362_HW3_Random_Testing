import random
import unittest

from credit_card_validator import credit_card_validator


def random_digits(k: int) -> str:
    """Return a random string of k decimal digits (leading zeros allowed)."""
    return "" if k <= 0 else "".join(random.choices("0123456789", k=k))


class TestCase(unittest.TestCase):
    def test_random_card_numbers(self):
        # total_cases = 450000  # a little overtime
        total_cases = 400000

        for i in range(total_cases):
            length = random.randint(1, 17)
            s = random_digits(length)
            with self.subTest(case=i, length=length):
                credit_card_validator(s)

        # Prefixes
        visa = 4
        mc = random.choice([51, 52, 53, 54, 55])
        amex = random.choice([34, 37])

        for prefix in [visa, mc, amex]:
            for i in range(total_cases // 3):
                length = random.randint(1, 17)
                s = str(prefix) + random_digits(length - len(str(prefix)))
                with self.subTest(case=i, prefix=prefix, length=length):
                    credit_card_validator(s)


if __name__ == "__main__":
    unittest.main()
