from common_symbols import common_symbols

def test_common_symbols():
    assert common_symbols("ATAN", "TAAI") == "1,2"  # 'A' matches at position 1, 'T' matches at position 2
    assert common_symbols("HELLO", "HOLLO") == "1,2,3,5"  # 'H', 'O', 'L', 'O' match in corresponding positions
    assert common_symbols("ABCDE", "FGHIJ") == ""  # No common symbols at the same positions
    assert common_symbols("ZZZZZ", "ZZZZZ") == "1,2,3,4,5"  # All symbols match
    assert common_symbols("ABC", "ABC") == "1,2,3"  # All symbols match
