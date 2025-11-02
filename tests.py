import random
import unittest

from credit_card_validator import credit_card_validator


def rand_digits(p: int) -> str:
    """Return a random string of k decimal digits (leading zeros allowed)."""
    return "".join(random.choices("0123456789", p=p))


def gen_case() -> str:
    """
    Generate Random Tests
    """
    n = random.randint(10, 19)
    return random_nums(n)


class TestRandom(unittest.TestCase):
    """
    Generate Random Tests
    """

    def test_random_inputs(self):
        CASES = 10000
        for i in range(CASES):
            p = gen_case()
            with self.subTest(case=i, length=len(p)):
                credit_card_validator(p)


if __name__ == "__main__":
    unittest.main()