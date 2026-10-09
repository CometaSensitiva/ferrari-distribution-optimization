# Data provenance and interpretation

The original notebook combines information attributed to the 2023 annual report with assumptions about model allocation, forecasts, capacities, distances, transport coefficients and vehicle values. It does not establish source provenance for every individual parameter. Treat the detailed network as an illustrative dataset, not observed company operations.

## Issues preserved from the academic submission

- The narrative cites 13,662 vehicles in 2023, while summing the executable model's shipment lower bounds gives 13,692. Those totals must not be presented as interchangeable.
- The hub capacities in code sum to 15,300, while the original markdown total row says 5,300. Destination counts in the tables also do not consistently reproduce the narrative total of 196 points of sale.
- Some mathematical lists and total rows disagree with the code. The reproducible runner uses the original executable parameters; it does not silently correct the submitted formulation.
- `g` is described as “ganancia” in the original notebook, but no production-cost or margin derivation is provided. The objective is assumed vehicle value minus transport, not verified company profit.
- Destination flows aggregate all vehicle models. Conservation holds by hub, but the model cannot track model-specific composition at each destination.
- No explicit global production capacity, inventory dynamics, lead times, demand uncertainty or route choice is modelled.

## What verification means

HiGHS solves both parameterized integer models. The runner checks constraint feasibility. This confirms computational reproducibility of the exercise; it does not validate the assumptions or certify an economically correct representation of Ferrari.

Alternative optimal distributions may exist. Compare feasibility, objective and hub totals rather than requiring every destination variable to match a historical solver run.
