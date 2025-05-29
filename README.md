# EcoWatch Streaming

## Objetivo
Sistema modular y escalable que simula el monitoreo ambiental en tiempo real con almacenamiento histórico y cache de 5 minutos.

## Estructura
- **data_simulator.py**: Simula sensores enviando datos cada 10 segundos.
- **Ingestor**: Valida datos, guarda en SQLite y actualiza cache.
- **Cache**: Guarda los últimos 5 minutos en memoria.
- **SQLiteStorage**: Guarda todos los logs en base histórica.

## Ejecución
1. Corre `main.py` para iniciar el sistema.
2. En otra terminal, ejecuta `data_sources/data_simulator.py`.

## Requisitos cumplidos
- Step 1: Ingesta modular y validación.
- Step 2: Cache temporal (5 minutos).
- Step 3: Modularización, POO, extensibilidad.
- Step 4: Módulo de reportes disponible pero opcional.
- Step 5: Documentación clara y decisiones justificadas.
