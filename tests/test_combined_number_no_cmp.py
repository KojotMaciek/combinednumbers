from combined_number_no_cmp import combine_elements

def test_combine_elements():
    assert combine_elements([50, 2, 1, 9]) == "95021"


def test_combine_with_duplicates():
    """Test combining numbers with duplicate values."""
    assert combine_elements([3, 3, 3]) == "333"


def test_combine_single_element():
    """Test with a list containing only one element."""
    assert combine_elements([42]) == "42"


def test_combine_with_leading_zeros():
    """Test combining numbers where arrangement matters."""
    assert combine_elements([3, 30, 34, 5, 9]) == "9534330"


def test_combine_with_similar_numbers():
    """Test with numbers that are similar (9, 90, 900)."""
    assert combine_elements([9, 90, 900]) == "990900"


def test_combine_two_elements():
    """Test with two elements."""
    assert combine_elements([3, 30]) == "330"
