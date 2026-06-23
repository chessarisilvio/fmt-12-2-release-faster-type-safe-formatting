# fmt 12.2 release – faster type‑safe formatting

**Categoria**: notizia  
**Difficoltà**: Facile

## Descrizione

Release della libreria {fmt} 12.2 con API C11 type‑safe, formattazione float più veloce e pieno supporto ai moduli C++20. Consente logging e stampa più rapidi nei tool C++.

## Architettura

- `download_fmt.sh`: scarica e verifica l'archivio sorgente.
- `example.cpp`: esempio C++20 che utilizza le nuove API type‑safe.
- `benchmark_cpu.sh`: script di benchmark comparativo (senza esecuzione automatica).
- `CMakeLists.txt`: configurazione di build CMake per l'esempio.

## Installazione

```bash
# Clona il repository
git clone <repo-url> fmt-122-release-faster-typesafe-formatting
cd fmt-122-release-faster-typesafe-formatting

# Scarica la release di {fmt}
./download_fmt.sh

# Compila l'esempio (richiede C++20 e CMake)
mkdir -p build && cd build
cmake ..
make
```

## Uso

1. Esegui `./download_fmt.sh` per ottenere i sorgenti.
2. Compila con CMake come mostrato sopra.
3. Avvia l'esempio:
   ```bash
   ./example
   ```
4. (Opzionale) Esegui il benchmark:
   ```bash
   ./benchmark_cpu.sh
   ```

## Esempi

```cpp
#include <fmt/core.h>
#include <fmt/format.h>

int main() {
    // API type‑safe C11
    fmt::print("Valore: {}\n", 3.14159);
    return 0;
}
```

## Stato

✅ COMPLETATO — 2026-06-17
