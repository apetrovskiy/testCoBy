import pytest
from src.main.java.challenges.medium.BracketMatcher.bracket_matcher \
    import BracketMatcher


test_data = [
    ("Argument goes here", 1),
    ("(coder)(byte))", 0),
    ("(c(oder)) b(yte)", 1),
    ("the color re(d))()(()", 0)
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_bracket_matcher(input: str, expected_result: int):
    assert expected_result == BracketMatcher(input)
