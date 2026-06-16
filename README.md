# fmt 12.2 release – faster type‑safe formatting

**Categoria**: notizia  
**Difficoltà**: Facile  

## Descrizione

Nuova versione della libreria {fmt} con API C11 type‑safe, formattazione float più veloce e miglior supporto ai moduli C++20. Può ridurre il tempo di logging e di stampa dei risultati nei tool C++ di Silvio, migliorando le performance complessive del pipeline locale.

## Obiettivo del progetto

Questo repository contiene gli script e gli esempi per:
- Scaricare e verificare la release 12.2 di {fmt}
- Compilare un esempio C++20 che utilizza le nuove API type‑safe
- Eseguire un benchmark manuale delle performance di formattazione
- Aggiornare il vault di sistema con le informazioni sul progetto

## Struttura

- `download_fmt.sh` – script di download e verifica hash
- `example.cpp` – esempio di utilizzo delle API C11 type‑safe
- `benchmark_cpu.sh` – script di benchmark comparativo
- `PROGRESS.md` – tracciamento dello stato di avanzamento

## Licenza

Questo progetto è rilasciato sotto licenza MIT – vedi file LICENSE per dettagli.
