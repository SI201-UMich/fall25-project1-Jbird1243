"""
Unit Tests for penguin_analysis.py
Author: Jalen Muse
Description: Tests all major functions in the Penguin Data Analysis project.
"""

import unittest
from penguin_analysis import (
    calculate_avg_body_mass,
    calculate_avg_flipper_length,
    read_penguin_data,
)


class TestPenguinAnalysis(unittest.TestCase):

    def setUp(self):
        """Set up small sample datasets for testing."""
        self.sample_data = [
            {"species": "Adelie", "island": "Biscoe", "sex": "Male", "body_mass_g": "4000", "flipper_length_mm": "190"},
            {"species": "Adelie", "island": "Biscoe", "sex": "Female", "body_mass_g": "3700", "flipper_length_mm": "185"},
            {"species": "Gentoo", "island": "Dream", "sex": "Male", "body_mass_g": "5200", "flipper_length_mm": "215"},
            {"species": "Gentoo", "island": "Dream", "sex": "Female", "body_mass_g": "5000", "flipper_length_mm": "210"},
        ]

    # -----------------------------
    # Tests for calculate_avg_body_mass
    # -----------------------------
    def test_avg_body_mass_general(self):
        """General test: average body mass per species-sex combo."""
        result = calculate_avg_body_mass(self.sample_data)
        expected = {("Adelie", "Male"): 4000.0, ("Adelie", "Female"): 3700.0,
                    ("Gentoo", "Male"): 5200.0, ("Gentoo", "Female"): 5000.0}
        self.assertEqual(result, expected)

    def test_avg_body_mass_multiple_entries(self):
        """General test: multiple entries per group."""
        data = self.sample_data + [{"species": "Adelie", "island": "Biscoe", "sex": "Male", "body_mass_g": "4200"}]
        result = calculate_avg_body_mass(data)
        self.assertAlmostEqual(result[("Adelie", "Male")], (4000 + 4200) / 2)

    def test_avg_body_mass_missing_values(self):
        """Edge case: ignore missing mass values."""
        data = self.sample_data + [{"species": "Adelie", "island": "Biscoe", "sex": "Male", "body_mass_g": ""}]
        result = calculate_avg_body_mass(data)
        self.assertIn(("Adelie", "Male"), result)  # should still compute average
        self.assertTrue(result[("Adelie", "Male")] > 0)

    def test_avg_body_mass_empty_data(self):
        """Edge case: empty dataset returns empty dict."""
        result = calculate_avg_body_mass([])
        self.assertEqual(result, {})

    # -----------------------------
    # Tests for calculate_avg_flipper_length
    # -----------------------------
    def test_avg_flipper_length_general(self):
        """General test: average flipper length per island-species combo."""
        result = calculate_avg_flipper_length(self.sample_data)
        expected = {("Biscoe", "Adelie"): 187.5, ("Dream", "Gentoo"): 212.5}
        self.assertEqual(result, expected)

    def test_avg_flipper_length_multiple_entries(self):
        """General test: multiple entries per group."""
        data = self.sample_data + [{"species": "Adelie", "island": "Biscoe", "sex": "Male", "flipper_length_mm": "195"}]
        result = calculate_avg_flipper_length(data)
        self.assertAlmostEqual(result[("Biscoe", "Adelie")], (190 + 185 + 195) / 3)

    def test_avg_flipper_length_missing_values(self):
        """Edge case: skip rows with missing flipper length."""
        data = self.sample_data + [{"species": "Adelie", "island": "Biscoe", "flipper_length_mm": ""}]
        result = calculate_avg_flipper_length(data)
        self.assertIn(("Biscoe", "Adelie"), result)

    def test_avg_flipper_length_empty_data(self):
        """Edge case: empty dataset returns empty dict."""
        result = calculate_avg_flipper_length([])
        self.assertEqual(result, {})

    # -----------------------------
    # Basic test for CSV reading
    # -----------------------------
    def test_read_penguin_data(self):
        """Simple check that CSV reading returns a list."""
        result = read_penguin_data("penguins.csv")
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)


if __name__ == "__main__":
    unittest.main()
