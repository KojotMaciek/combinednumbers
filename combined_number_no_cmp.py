class CombineKey:
    """
    A custom key class that enables comparison-based sorting without cmp_to_key.
    
    This class wraps an integer and defines comparison operators that compare
    two numbers based on which concatenation order produces a larger result.
    """
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        """Equal if both produce the same concatenation result."""
        ab = str(self.value) + str(other.value)
        ba = str(other.value) + str(self.value)
        return ab == ba
    
    def __lt__(self, other):
        """Less than if ba > ab (meaning self should come after the other in descending order)."""
        ab = str(self.value) + str(other.value)
        ba = str(other.value) + str(self.value)
        # We return True if ba > ab (self is "less than" other in normal order,
        # so it comes after in reverse=True sorting)
        return ba > ab
    
    def __repr__(self): 
        """Return the string representation of the wrapped integer value."""
        return str(self.value)


def combine_elements(integers_list: list) -> str:
    """
    Combines integers from a list into the largest possible number.
    
    Version WITHOUT cmp_to_key - uses custom comparison operators instead.
    
    ALGORITHM EXPLANATION WITH EXAMPLE:
    Input: [3, 30, 34, 5, 9]
    
    The key insight: Compare how numbers concatenate!
    - For 3 and 30: "330" vs "303" → "330" is bigger, so 3 comes before 30
    - For 9 and 5: "95" vs "59" → "95" is bigger, so 9 comes before 5
    
    After sorting by this rule: [9, 5, 34, 3, 30]
    Final result: "9534330"
    
    Args:
        integers_list (list): A list of integers to combine.
        
    Returns:
        str: The largest possible number formed by arranging these integers.
    """
    # Wrap each integer with CombineKey, sort, then extract values
    sorted_keys = sorted((CombineKey(num) for num in integers_list), reverse=True)
    
    # Join all numbers into one string
    return ''.join(str(key.value) for key in sorted_keys)


if __name__ == "__main__":
    example = [3, 30, 34, 5, 9]
    result = combine_elements(example)
    print(f"Input: {example}")
    print(f"Output: {result}")
