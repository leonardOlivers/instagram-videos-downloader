thonpython
import json
from pathlib import Path

class Exporter:
    @staticmethod
    def save_json(data, out_path: str):
        path = Path(out_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)