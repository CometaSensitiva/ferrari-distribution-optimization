# Ferrari Distribution Network Optimization

[English](README.md) · **Italiano**

Un caso di studio di programmazione intera che ho sviluppato per **Investigación Operativa** durante l’Erasmus all’Universidad Alfonso X el Sabio, Madrid (gennaio 2025). È stato il mio primo progetto in Python: il corso era soprattutto teorico e il compito era applicare i modelli a un problema reale. Il progetto è stato valutato **10/10**.

Il modello descrive una rete distributiva a due livelli — **Maranello → quattro hub regionali → 15 gruppi di destinazioni** — con limiti di capacità, vincoli sulla domanda e conservazione dei flussi, confrontando due scenari di costo del trasporto.

> [!NOTE]
> Esercizio studentesco indipendente, basato su informazioni pubbliche e mie ipotesi di modellazione. Non è affiliato a Ferrari e non rappresenta le operazioni reali dell’azienda.

![Rete distributiva: Maranello, quattro hub regionali e i gruppi di destinazioni](docs/ferrari_logistics.svg)

## Contenuto

| File | Descrizione |
| --- | --- |
| [`ferrari.ipynb`](ferrari.ipynb) | **Consegna originale**, invariata: contesto, formulazione matematica, implementazione Pyomo e risultati dei due scenari, in spagnolo |
| [`data/ferrari.xlsx`](data/ferrari.xlsx) | Foglio in cui ho preparato i dati: modelli di auto, hub e punti vendita |
| [`model.py`](model.py) · [`run_scenarios.py`](run_scenarios.py) | Modello estratto dal notebook e reso riproducibile con il solver open source HiGHS, aggiunto successivamente |
| [`results/scenarios.json`](results/scenarios.json) | Risultati dello script riproducibile |
| [`ASSUMPTIONS.md`](ASSUMPTIONS.md) | Provenienza dei dati, incoerenze nelle tabelle originali e limiti dei risultati |

## Il modello

- **Decisioni:** 52 variabili intere per le spedizioni dei modelli agli hub, 15 per le spedizioni dagli hub alle destinazioni.
- **Vincoli:** limiti sulle spedizioni, capacità di hub e destinazioni, conservazione dei flussi in ogni hub.
- **Obiettivo:** massimizzare i valori ipotizzati dei veicoli meno i costi di trasporto. Il notebook lo chiama *ganancia*; non è un profitto verificato.
- **Scenario 2:** il coefficiente Maranello → Nord America passa da 0,00015 a 0,00035 EUR/(kg·km), a parità delle altre condizioni. È un’analisi di sensibilità, non una prova di risparmi reali.

## I dati

`data/ferrari.xlsx` contiene tre tabelle:

- **coches:** 13 modelli con linea di prodotto e consegne regionali stimate, 2023 e 2024.
- **hubs:** quattro hub con capacità, consegne, previsioni, distanza da Maranello e coefficiente di trasporto.
- **pos:** 15 gruppi di destinazioni con punti vendita, capacità, consegne, distanza dal proprio hub e coefficiente.

I totali regionali provengono dal [report annuale Ferrari 2023](https://www.ferrari.com/en-EN/corporate/financial-documents?year=2023); ripartizione per modello, capacità, distanze e coefficienti sono mie ipotesi.

## Esecuzione

Richiede Python 3.9 o successivo. Il notebook originale è in spagnolo.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_scenarios.py
```

Lo script stampa entrambe le distribuzioni, verifica tutti i vincoli e salva `results/scenarios.json`. Il notebook originale usava GLPK: per eseguirlo come consegnato servono Jupyter e l’eseguibile `glpsol`.

## Dopo il progetto

Un anno più tardi, al *Laboratorio di Strumenti di Ottimizzazione* dell’Università di Bologna, ho ripreso Python e Pyomo in modo più sistematico: knapsack, bin packing, colorazione di grafi, alberi ricoprenti minimi e cammini minimi. I notebook sono nel mio [repository universitario](https://github.com/CometaSensitiva/university/tree/main/3-anno/laboratorio-strumenti-ottimizzazione).

## Fonti

- Ferrari N.V., *2023 Annual Report and Form 20-F*: [documenti finanziari](https://www.ferrari.com/en-EN/corporate/financial-documents?year=2023)
- José Niño Mora, *Introducción a la optimización de decisiones* (2021)

Lavoro accademico originale: Michele Mazza, gennaio 2025. Rilasciato con [licenza MIT](LICENSE); nomi e marchi Ferrari appartengono ai rispettivi proprietari.
