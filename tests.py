import random
import unittest
from credit_card_validator import credit_card_validator


def random_digits(k: int) -> str:
    """Return a random string of k decimal digits."""
    return "".join(random.choices("0123456789", k=k))


class TestCase(unittest.TestCase):
    def test_random_card_numbers(self):
        """
        Test the credit_card_validator function with random card numbers of varying lengths.
        """
        total_cases = 500000

        edge_lengths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 19, 20, 21, 30, 40]

        for i in range(total_cases):
            if random.randint(0, 1) == 1:
                length = random.choice(edge_lengths)
            else:
                # length = random.randint(13, 18) # 
                length = random.randint(13, 18)
            s = random_digits(length if length > 0 else 0)
            with self.subTest(case=i, length=length):
                credit_card_validator(s)


if __name__ == "__main__":
    unittest.main()
