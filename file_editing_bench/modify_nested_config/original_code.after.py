from typing import Dict, Any
import yaml

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp",
        "user": "admin",
        "pool": {"min_size": 5, "max_size": 20, "timeout": 30},
        "ssl": {"enabled": True, "verify": True, "ca_cert": "/path/to/ca.crt"},
    },
    "cache": {
        "type": "redis",
        "host": "localhost",
        "port": 6379,
        "sentinel": {
            "enabled": True,
            "masters": ["mymaster"],
            "nodes": [
                {"host": "sentinel1", "port": 26379},
                {"host": "sentinel2", "port": 26379},
            ],
        },
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "handlers": {
            "file": {
                "enabled": True,
                "path": "/var/log/myapp.log",
                "max_size": "100MB",
                "backup_count": 5,
            },
            "syslog": {"enabled": False, "host": "localhost", "port": 514},
        },
    },
    "server": {"host": "0.0.0.0", "port": 8000, "workers": 4},
}


def save_config(config: Dict[str, Any], filename: str):
    with open(filename, "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    save_config(config, "config.yaml")
