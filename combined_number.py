from functools import cmp_to_key

def combine_elements(integers_list: list) -> str:
    """
    Combines integers from a list into the largest possible number.
    
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
    def compare(a, b):
        """
        Custom comparison function.
        
        Compares two numbers by checking which order makes a bigger result:
        - If "a+b" > "b+a": a should come FIRST, return -1
        - If "b+a" > "a+b": b should come FIRST, return 1
        
        Example: compare(3, 30)
        - "3" + "30" = "330"
        - "30" + "3" = "303"
        - "330" > "303", so return -1 (3 comes before 30)
        """
        ab = str(a) + str(b)  # Concatenate a then b
        ba = str(b) + str(a)  # Concatenate b then a
        
        if ab > ba:
            return -1  # a should come first
        elif ab < ba:
            return 1   # b should come first
        return 0       # they produce the same result
    
    # Sort the entire list using our custom comparison
    integers_list.sort(key=cmp_to_key(compare))
    
    # Join all numbers into one string
    return ''.join(str(num) for num in integers_list)

def main():
    """Main function to demonstrate the combine_elements function."""
    result = combine_elements([3, 30, 34, 5, 9])
    print(f"Result: {result}")

if __name__ == "__main__":
    main()