import pytest
from testingonly.mytest import Tester  # Import the Tester Class

# Default tests (test_mytest to test method f) to Ensure Pytest is working (From Docs https://docs.pytest.org/en/6.2.x/getting-started.html)


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


def test_tester(capsys):
    # Create the Tester Class
    te = Tester()
    # Get the captured output
    captured = capsys.readouterr()
    # Assert that the capture output is tested
    assert captured.out == "Hello\n"
