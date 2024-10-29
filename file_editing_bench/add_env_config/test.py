import os
import pytest
from task_files.config import load_config


@pytest.fixture
def clean_env():
    """Fixture to clean environment variables before each test"""
    # Store original environment
    original_env = dict(os.environ)

    # Clear relevant environment variables
    env_vars = [
        "APP_NAME",
        "APP_DEBUG",
        "APP_SECRET_KEY",
        "DB_HOST",
        "DB_PORT",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD",
        "SMTP_SERVER",
        "SMTP_PORT",
        "SMTP_SENDER",
        "SMTP_USERNAME",
        "SMTP_PASSWORD",
    ]
    for var in env_vars:
        if var in os.environ:
            del os.environ[var]

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


def test_load_config_defaults(clean_env):
    """Test that default values are used when environment variables are not set"""
    # Set only required environment variables
    os.environ["APP_SECRET_KEY"] = "test-secret"
    os.environ["DB_PASSWORD"] = "test-db-password"
    os.environ["SMTP_USERNAME"] = "test-username"
    os.environ["SMTP_PASSWORD"] = "test-password"

    config = load_config()

    assert config["app"]["name"] == "myapp"
    assert config["app"]["debug"] is False
    assert config["app"]["secret_key"] == "test-secret"

    assert config["database"]["host"] == "localhost"
    assert config["database"]["port"] == 5432
    assert config["database"]["name"] == "myapp"
    assert config["database"]["user"] == "admin"
    assert config["database"]["password"] == "test-db-password"

    assert config["email"]["smtp_server"] == "smtp.gmail.com"
    assert config["email"]["smtp_port"] == 587
    assert config["email"]["sender"] == "noreply@example.com"
    assert config["email"]["username"] == "test-username"
    assert config["email"]["password"] == "test-password"


def test_load_config_custom_values(clean_env):
    """Test that environment variables override default values"""
    os.environ.update(
        {
            "APP_NAME": "customapp",
            "APP_DEBUG": "true",
            "APP_SECRET_KEY": "custom-secret",
            "DB_HOST": "custom-host",
            "DB_PORT": "5433",
            "DB_NAME": "customdb",
            "DB_USER": "customuser",
            "DB_PASSWORD": "custom-password",
            "SMTP_SERVER": "custom.smtp.com",
            "SMTP_PORT": "25",
            "SMTP_SENDER": "custom@example.com",
            "SMTP_USERNAME": "custom-username",
            "SMTP_PASSWORD": "custom-smtp-pass",
        }
    )

    config = load_config()

    assert config["app"]["name"] == "customapp"
    assert config["app"]["debug"] is True
    assert config["app"]["secret_key"] == "custom-secret"

    assert config["database"]["host"] == "custom-host"
    assert config["database"]["port"] == 5433
    assert config["database"]["name"] == "customdb"
    assert config["database"]["user"] == "customuser"
    assert config["database"]["password"] == "custom-password"

    assert config["email"]["smtp_server"] == "custom.smtp.com"
    assert config["email"]["smtp_port"] == 25
    assert config["email"]["sender"] == "custom@example.com"
    assert config["email"]["username"] == "custom-username"
    assert config["email"]["password"] == "custom-smtp-pass"


def test_load_config_missing_required(clean_env):
    """Test that missing required values raise ValueError"""
    # Test missing APP_SECRET_KEY
    with pytest.raises(
        ValueError, match="Required environment variable APP_SECRET_KEY is not set"
    ):
        load_config()

    # Set APP_SECRET_KEY but missing DB_PASSWORD
    os.environ["APP_SECRET_KEY"] = "test-secret"
    with pytest.raises(
        ValueError, match="Required environment variable DB_PASSWORD is not set"
    ):
        load_config()

    # Set DB_PASSWORD but missing SMTP_USERNAME
    os.environ["DB_PASSWORD"] = "test-password"
    with pytest.raises(
        ValueError, match="Required environment variable SMTP_USERNAME is not set"
    ):
        load_config()

    # Set SMTP_USERNAME but missing SMTP_PASSWORD
    os.environ["SMTP_USERNAME"] = "test-username"
    with pytest.raises(
        ValueError, match="Required environment variable SMTP_PASSWORD is not set"
    ):
        load_config()
