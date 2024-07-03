# Stable Matching Algorithm

## Overview

This Python script implements the Gale-Shapley algorithm for stable matching. It matches hospitals and residents based on their preferences, ensuring that each resident is paired with a hospital they prefer and each hospital is paired with a resident they prefer, resulting in a stable match where no two entities would prefer to be matched with each other over their current match.

## Features

- Create preference matrices for hospitals and residents.
- Perform stable matching based on these preferences.
- Output the matched pairs in a readable format.

## Requirements

- Python 3.x

## How It Works

1. **Create Preference Matrices**:
   - The user inputs the number of hospitals and residents.
   - Preference lists are created for both hospitals and residents. Preferences should be numeric, starting with 0.

2. **Stable Matching Algorithm**:
   - Uses the Gale-Shapley algorithm to perform the matching based on the provided preferences.
   - Outputs one possible stable matching where each hospital is paired with a resident.

## Functions

### `create_Matrix_hospital(no_hospital, no_residents)`

Creates a matrix representing hospital preferences for residents.

**Args**:
- `no_hospital` (int): Number of hospitals.
- `no_residents` (int): Number of residents.

**Returns**:
- List of lists: Hospital preferences matrix.

### `create_Matrix_residents(no_hospital, no_residents)`

Creates a matrix representing resident preferences for hospitals.

**Args**:
- `no_hospital` (int): Number of hospitals.
- `no_residents` (int): Number of residents.

**Returns**:
- List of lists: Resident preferences matrix.

### `stable_matching(n, hospital_preferences, resident_preferences)`

Performs the stable matching algorithm to find a stable set of pairs.

**Args**:
- `n` (int): Number of hospitals/residents.
- `hospital_preferences` (list of lists): Hospital preferences matrix.
- `resident_preferences` (list of lists): Resident preferences matrix.

**Returns**:
- List: Pairs representing the stable matching.

## How to Use

1. Run the script.
2. Enter the number of hospitals and residents.
3. Provide the preferences for each hospital and resident as prompted.
4. The script will display the preferences and the resulting stable match.

