from typing import List
from src.main.java.challenges.medium.TreeConstructor.tree_constructor import TreeConstructor
import pytest


test_data = [
    (["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"], True),
    (["(1,2)", "(3,2)", "(2,12)", "(5,2)"], False)
]


@pytest.mark.parametrize("input_data,expected_result", test_data)
def test_tree_constructor(input_data: List[str], expected_result: bool):
    assert expected_result == TreeConstructor(input_data)
