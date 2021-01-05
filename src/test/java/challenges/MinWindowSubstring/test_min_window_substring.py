import pytest
from typing import List
from src.main.java.challenges.MinWindowSubstring.solution_min_window_substring import MinWindowSubstring


test_data = [
    (["ahffaksfajeeubsne", "jefaa"], "aksfaje"),
    (["aaffhkksemckelloe", "fhea"], "affhkkse"),
    (["aaabaaddae", "aed"], "dae"),
    (["aabdccdbcacd", "aad"], "aabd")
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_min_window_substring(input_array: List[str], expected_result: str):
    assert expected_result == MinWindowSubstring(input_array)
