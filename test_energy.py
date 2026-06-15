import unittest

from energy_logic import (
    calculate_energy_financials
)


class TestEnergyFinancials(
    unittest.TestCase
):
    """
    Test energy calculations.
    """

    def test_no_discount(self):
        """
        Consumption below 50,000.
        """
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 1000,
                "new_index": 11000,
                "status": "Normal"
            }
        ]

        result = (
            calculate_energy_financials(
                devices
            )
        )

        self.assertEqual(
            result,
            (
                10000,
                0,
                30000000
            )
        )

    def test_discount_applied(self):
        """
        Consumption above threshold.
        """
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 60000,
                "status": "Normal"
            }
        ]

        result = (
            calculate_energy_financials(
                devices
            )
        )

        self.assertEqual(
            result,
            (
                60000,
                3,
                174600000
            )
        )

    def test_exact_threshold(self):
        """
        Consumption exactly 50,000.
        """
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 50000,
                "status": "Normal"
            }
        ]

        result = (
            calculate_energy_financials(
                devices
            )
        )

        self.assertEqual(
            result,
            (
                50000,
                3,
                145500000
            )
        )


if __name__ == "__main__":
    unittest.main()
