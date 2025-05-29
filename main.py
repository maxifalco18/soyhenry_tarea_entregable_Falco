import time
import os
import json
import logging
from core.ingestor import Ingestor
from core.cache import Cache
from storage.sqlite_storage import SQLiteStorage

logging.basicConfig(
    filename='ecowatch.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

EVENT_FILE = "eventos.jsonl"

def seguir_archivo(path):
    with open(path, "r", encoding="utf-8") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            yield line.strip()

def main():
    cache = Cache()
    storage = SQLiteStorage("ecowatch.db")
    ingestor = Ingestor(cache=cache, storage=storage)

    print("Escuchando logs desde eventos.jsonl...")
    for line in seguir_archivo(EVENT_FILE):
        try:
            log = json.loads(line)
            ingestor.ingestar(log)
        except json.JSONDecodeError:
            logging.warning(f"Línea no válida ignorada: {line}")

if __name__ == "__main__":
    main()
