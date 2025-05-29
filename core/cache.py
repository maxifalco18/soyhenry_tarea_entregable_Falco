from datetime import datetime, timedelta

class Cache:
    def __init__(self):
        self.registros = []

    def agregar_log(self, log):
        self.registros.append(log)
        self._limpiar_cache()

    def _limpiar_cache(self):
        umbral = datetime.now() - timedelta(minutes=5)
        self.registros = [r for r in self.registros if datetime.fromisoformat(r['timestamp']) >= umbral]

    def obtener_por_sala(self, sala):
        return [r for r in self.registros if r["sala"] == sala]

    def obtener_por_timestamp(self, ts):
        return [r for r in self.registros if r["timestamp"] == ts]
