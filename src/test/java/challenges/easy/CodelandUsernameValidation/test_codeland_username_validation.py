from src.main.java.challenges.easy.CodelandUsernameValidation.codeland_username_validation import CodelandUsernameValidation
import pytest


test_data = [
    ("aa_", "false"),
    ("u__hello_world123", "true"),
    ("oooooooooooooooooo________a", "false"),
    ("a______b_________555555555555aaaa", "false")
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_codeland_username_validation(input: str, expected_result: str):
    assert expected_result == CodelandUsernameValidation(input)
