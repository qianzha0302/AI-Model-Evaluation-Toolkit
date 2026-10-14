
import pytest
from evaluator import calculate_accuracy


# Test 1: Normal accuracy calculation
def test_normal_accuracy():
    y_true = [1, 0, 1, 1]
    y_pred = [1, 0, 0, 1]

    assert calculate_accuracy(y_true, y_pred) == 0.75


# Test 2: Mismatched input lengths
def test_mismatched_lengths():
    y_true = [1, 0, 1]
    y_pred = [1, 0]

    with pytest.raises(ValueError):
        calculate_accuracy(y_true, y_pred)


# Test 3: Empty input lists
def test_empty_lists():
    y_true = []
    y_pred = []

    with pytest.raises(ValueError):
        calculate_accuracy(y_true, y_pred)

