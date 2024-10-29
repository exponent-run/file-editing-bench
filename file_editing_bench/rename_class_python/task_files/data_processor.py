import json
from datetime import datetime
from typing import List, Dict, Optional

class ConfigManager:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.settings = self._load_config()
    
    def _load_config(self) -> Dict:
        with open(self.config_path) as f:
            return json.load(f)
    
    def get_setting(self, key: str) -> Optional[str]:
        return self.settings.get(key)

class X:
    def __init__(self):
        self.records: List[Dict] = []
        self.last_processed = None
    
    def add_record(self, data: Dict):
        data['timestamp'] = datetime.now().isoformat()
        self.records.append(data)
        self.last_processed = data['timestamp']
    
    def get_records_since(self, timestamp: str) -> List[Dict]:
        return [r for r in self.records if r['timestamp'] > timestamp]
    
    def clear_old_records(self, days: int = 30):
        cutoff = (datetime.now() - datetime.timedelta(days=days)).isoformat()
        self.records = [r for r in self.records if r['timestamp'] > cutoff]

class DataValidator:
    @staticmethod
    def validate_record(record: Dict) -> bool:
        required_fields = ['id', 'value', 'source']
        return all(field in record for field in required_fields)
    
    @staticmethod
    def sanitize_record(record: Dict) -> Dict:
        return {k: str(v).strip() for k, v in record.items()}