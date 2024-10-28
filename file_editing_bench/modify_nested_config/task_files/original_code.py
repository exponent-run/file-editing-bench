from typing import Dict, Any
import yaml

config = {
    "database": {"host": "localhost", "port": 5432, "name": "myapp", "user": "admin"},
    "cache": {"type": "redis", "host": "localhost", "port": 6379},
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    },
    "server": {"host": "0.0.0.0", "port": 8000, "workers": 4},
}


def save_config(config: Dict[str, Any], filename: str):
    with open(filename, "w") as f:
        yaml.dump(config, f, default_flow_style=False)


if __name__ == "__main__":
    save_config(config, "config.yaml")
