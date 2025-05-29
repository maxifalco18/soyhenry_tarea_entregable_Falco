import logging

logger = logging.getLogger(__name__)

class Ingestor:
    CAMPOS_OBLIGATORIOS = {"timestamp", "tipo", "sala", "temperatura", "humedad", "co2"}

    def __init__(self, cache, storage):
        self.cache = cache
        self.storage = storage

    def validar_log(self, log):
        return self.CAMPOS_OBLIGATORIOS.issubset(log.keys())

    def ingestar(self, log):
        if not self.validar_log(log):
            logger.warning(f"Log mal formado: {log}")
            return

        logger.info(f"Log recibido: {log}")
        self.cache.agregar_log(log)
        self.storage.guardar_log(log)
