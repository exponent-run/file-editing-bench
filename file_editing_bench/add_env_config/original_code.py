import os
from typing import Dict, Any
import yaml

def load_config() -> Dict[str, Any]:
    config = {
        'app': {
            'name': 'myapp',
            'debug': False,
            'secret_key': 'default-secret-key'
        },
        'database': {
            'host': 'localhost',
            'port': 5432,
            'name': 'myapp',
            'user': 'admin',
            'password': 'admin-password'
        },
        'email': {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'sender': 'noreply@example.com'
        }
    }
    
    return config

def save_config(config: Dict[str, Any], filename: str):
    with open(filename, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

if __name__ == "__main__":
    config = load_config()
    save_config(config, 'config.yaml')