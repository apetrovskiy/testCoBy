import pytest
from typing import List
from src.main.java.challenges.medium.TreeConstructor.tree_constructor \
    import TreeConstructor


test_data = [
    (["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"], "true"),
    (["(1,2)", "(3,2)", "(2,12)", "(5,2)"], "false"),
    (["(2,5)", "(2,6)"], "false"),
    (["(1,2)", "(2,4)", "(7,2)"], "true"),
    (["(10,20)"], "true"),
    (["(10,20)", "(20,50)"], "true")
]


@pytest.mark.parametrize("input_data,expected_result", test_data)
def test_tree_constructor(input_data: List[str], expected_result: str):
    assert expected_result == TreeConstructor(input_data)
