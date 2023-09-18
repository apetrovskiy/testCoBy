import pytest
from typing import List
from src.main.java.challenges.medium.MinWindowSubstring.someone_elses import (
    MinWindowSubstring1,
)
from src.main.java.challenges.medium.MinWindowSubstring.solution_min_window_substring import (
    MinWindowSubstring,
)


test_data = [
    (["aaabaaddae", "aed"], "dae"),
    (["aabdccdbcacd", "aad"], "aabd"),
    (["ahffaksfajeeubsne", "jefaa"], "aksfaje"),
    (["aaffhkksemckelloe", "fhea"], "affhkkse"),
    (["aaffsfsfasfasfasfasfasfacasfafe", "fafe"], "fafe"),
    (["aaffsfsfasfasfasfasfasfacasfafe", "fafsf"], "affsf"),
    (["vvavereveaevafefaef", "vvev"], "vvave"),
    (["caae", "cae"], "caae"),
    (["cccaabbbbrr", "rbac"], "caabbbbr"),
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_min_window_substring(input_array: List[str], expected_result: str):
    assert expected_result == MinWindowSubstring(input_array)


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_min_window_substring_someone_elses(
    input_array: List[str], expected_result: str
):
    assert expected_result == MinWindowSubstring1(input_array)
