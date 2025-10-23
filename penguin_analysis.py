"""
SI 201 Project 1 - Data Analysis
Student Name: Jalen Muse
Dataset: Palmer Penguins
Collaborators: None
GenAI tools used: ChatGPT (for project structure and starter code)

This program analyzes the Palmer Penguins dataset to calculate:
1. The average body mass for each species-sex combination.
2. The average flipper length for each species-island combination.

Each function is modular, tested, and contributes to the final analysis.
Results are written to an output CSV file.
"""

import csv
from collections import defaultdict


def read_penguin_data(filename):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    Each dictionary represents a penguin entry.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        list[dict]: List of dictionaries with penguin data.
    """
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def calculate_avg_body_mass(data):
    """
    Calculates the average body mass (g) for each species-sex combination.

    Args:
        data (list[dict]): List of penguin records.

    Returns:
        dict[tuple, float]: Mapping of (species, sex) → average body mass.
    """
    body_mass = defaultdict(list)
    for penguin in data:
        species = penguin.get('species')
        sex = penguin.get('sex')
        mass = penguin.get('body_mass_g')

        if species and sex and mass:
            try:
                body_mass[(species, sex)].append(float(mass))
            except ValueError:
                continue

    avg_mass = {k: sum(v) / len(v) for k, v in body_mass.items() if v}
    return avg_mass


def calculate_avg_flipper_length(data):
    """
    Calculates the average flipper length (mm) for each species-island combination.

    Args:
        data (list[dict]): List of penguin records.

    Returns:
        dict[tuple, float]: Mapping of (island, species) → average flipper length.
    """
    flipper_data = defaultdict(list)
    for penguin in data:
        island = penguin.get('island')
        species = penguin.get('species')
        flipper = penguin.get('flipper_length_mm')

        if island and species and flipper:
            try:
                flipper_data[(island, species)].append(float(flipper))
            except ValueError:
                continue

    avg_flipper = {k: sum(v) / len(v) for k, v in flipper_data.items() if v}
    return avg_flipper


def write_results_to_csv(results, filename):
    """
    Writes a dictionary of results to a CSV file.

    Args:
        results (dict): Dictionary with tuple keys and numeric values.
        filename (str): Name of the output CSV file.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Category 1", "Category 2", "Average Value"])
        for (a, b), value in results.items():
            writer.writerow([a, b, round(value, 2)])


def main():
    """
    Coordinates reading data, performing calculations,
    and writing results to output files.
    """
    data = read_penguin_data('penguins.csv')

    # Perform calculations
    avg_body_mass = calculate_avg_body_mass(data)
    avg_flipper_length = calculate_avg_flipper_length(data)

    # Write results to CSV files
    write_results_to_csv(avg_body_mass, 'avg_body_mass_results.csv')
    write_results_to_csv(avg_flipper_length, 'avg_flipper_length_results.csv')

    print("✅ Analysis complete! Results saved to CSV files.")


if __name__ == "__main__":
    main()
