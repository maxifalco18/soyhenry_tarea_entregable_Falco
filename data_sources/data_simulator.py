import time
import random
from datetime import datetime
import json
import os

EVENT_FILE = os.path.join(os.path.dirname(__file__), '..', 'eventos.jsonl')

SALAS = ["Sala A", "Sala B", "Sala C"]
TIPOS = ["sensor_temp", "sensor_hum", "sensor_co2"]

def generar_log():
    return {
        "timestamp": datetime.now().isoformat(),
        "tipo": random.choice(TIPOS),
        "sala": random.choice(SALAS),
        "temperatura": round(random.uniform(20, 60), 2),
        "humedad": round(random.uniform(30, 90), 2),
        "co2": round(random.uniform(300, 2000), 2)
    }

if __name__ == "__main__":
    while True:
        log = generar_log()
        with open(EVENT_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(log) + "\n")
        print(f"Log generado y escrito en {EVENT_FILE}")
        time.sleep(10)
