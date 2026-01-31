# Combined Number

A Python utility that combines integers from a list into the largest possible number.

## Overview

This function takes a list of integers and rearranges them to form the largest number when concatenated together.

**Two versions available:**
1. **`combined_number.py`** - Uses `cmp_to_key` from `functools` for comparison-based sorting
2. **`combined_number_no_cmp.py`** - Alternative version without any imports, uses a custom key class with comparison operators

**Example:**
```python
from combined_number import combine_elements

result = combine_elements([3, 30, 34, 5, 9])
print(result)  # Output: "9534330"
```

## How It Works

The algorithm compares each pair of numbers by checking which concatenation order produces a larger result:
- For numbers `a` and `b`, it compares `"a+b"` vs `"b+a"`
- If `"a+b"` is larger, `a` comes first
- This is repeated for all numbers using a custom sort comparator

**Example comparison:**
- `3` vs `30`: `"330"` > `"303"` → 3 comes before 30
- `9` vs `5`: `"95"` > `"59"` → 9 comes before 5

## Installation

Clone the repository and navigate to the project directory:
```bash
git clone <repository-url>
cd combinednumber
```

## Usage

Run the main script (original version with cmp_to_key):
```bash
python combined_number.py
```

Run the alternative version (no imports):
```bash
python combined_number_no_cmp.py
```

Use in your code:
```python
# Using the original version with cmp_to_key
from combined_number import combine_elements
result = combine_elements([50, 2, 1, 9])
print(result)  # Output: "95021"

# Or using the version without imports
from combined_number_no_cmp import combine_elements
result = combine_elements([50, 2, 1, 9])
print(result)  # Output: "95021"
```

## Testing

Run the test suite with pytest:
```bash
# Test the original version
pytest tests/test_combined_number.py -v

# Test the version without imports
pytest tests/test_combined_number_no_cmp.py -v

# Run all tests
pytest -v
```

## Tests Included

- Basic combination test
- Duplicate values
- Single element
- Numbers with similar patterns
- Two-element comparison
