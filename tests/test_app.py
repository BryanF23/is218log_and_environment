"""
This module contains unit tests for the App class, testing its environment
variable retrieval, REPL exit command handling, and response to unknown commands.
"""
import pytest

from app import App

def test_app_get_environment_variable():
    """Test retrieving the environment variable and checking if it is valid."""
    app = App()
#   Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"



def test_app_start_exit_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()


    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
