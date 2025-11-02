import random
import unittest

from credit_card_validator import credit_card_validator


def random_nums(k: int) -> str:
    """Return a random string of k decimal digits (leading zeros allowed)."""
    return "".join(random.choices("0123456789", k=k))


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
        cases = 10000
        for i in range(cases):
            l = gen_case()
            with self.subTest(case=i, length=len(l)):
                credit_card_validator(l)


if __name__ == "__main__":
    unittest.main()
