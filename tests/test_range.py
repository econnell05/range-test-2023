from src.range_function import ranges
import pytest

def test_poit():
    assert ranges([[-3, 0], [0, 4.5]]) == [0, 0]

