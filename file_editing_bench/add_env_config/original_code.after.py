import os
from typing import Dict, Any, Optional
import yaml

def get_env_value(key: str, default: Any = None, required: bool = False) -> Optional[Any]:
    value = os.environ.get(key)
    if value is None and required:
        raise ValueError(f"Required environment variable {key} is not set")
    return value if value is not None else default

def load_config() -> Dict[str, Any]:
    config = {
        'app': {
            'name': get_env_value('APP_NAME', 'myapp'),
            'debug': get_env_value('APP_DEBUG', 'false').lower() == 'true',
            'secret_key': get_env_value('APP_SECRET_KEY', 'default-secret-key', required=True)
        },
        'database': {
            'host': get_env_value('DB_HOST', 'localhost'),
            'port': int(get_env_value('DB_PORT', '5432')),
            'name': get_env_value('DB_NAME', 'myapp'),
            'user': get_env_value('DB_USER', 'admin'),
            'password': get_env_value('DB_PASSWORD', 'admin-password', required=True)
        },
        'email': {
            'smtp_server': get_env_value('SMTP_SERVER', 'smtp.gmail.com'),
            'smtp_port': int(get_env_value('SMTP_PORT', '587')),
            'sender': get_env_value('SMTP_SENDER', 'noreply@example.com'),
            'username': get_env_value('SMTP_USERNAME', required=True),
            'password': get_env_value('SMTP_PASSWORD', required=True)
        }
    }
    
    return config

def save_config(config: Dict[str, Any], filename: str):
    with open(filename, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

if __name__ == "__main__":
    config = load_config()
    save_config(config, 'config.yaml')