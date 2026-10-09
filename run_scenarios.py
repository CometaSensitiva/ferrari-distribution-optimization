"""Reproduce both academic scenarios with the open-source HiGHS solver."""
from pyomo.environ import Constraint, SolverFactory, Var, value
from pyomo.opt import TerminationCondition
from model import build_ferrari_model, print_distribution
import json
from pathlib import Path

def run():
    summary = []
    for name, coefficient in [("baseline", 0.00015), ("higher_fna_transport_cost", 0.00035)]:
        model = build_ferrari_model(coefficient)
        result = SolverFactory("appsi_highs").solve(model)
        if result.solver.termination_condition != TerminationCondition.optimal:
            raise RuntimeError(f"{name}: {result.solver.termination_condition}")
        # Check feasibility independently of the solver's reported termination.
        for constraint in model.component_data_objects(ctype=Constraint, active=True):
            body = value(constraint.body)
            if constraint.has_lb() and body < value(constraint.lower) - 1e-6:
                raise RuntimeError(f"Lower bound violation: {constraint.name}")
            if constraint.has_ub() and body > value(constraint.upper) + 1e-6:
                raise RuntimeError(f"Upper bound violation: {constraint.name}")
        for variable in model.component_data_objects(Var):
            if variable.is_integer() and abs(value(variable) - round(value(variable))) > 1e-6:
                raise RuntimeError(f"Integrality violation: {variable.name}")
        row = {"scenario": name, "fna_coefficient": coefficient,
               "objective_eur": value(model.obj),
               "vehicles_by_hub": {str(h): sum(round(value(model.x[m,h])) for m in model.M) for h in model.H}}
        summary.append(row)
        print(json.dumps(row, indent=2))
        print_distribution(model)
    Path("results").mkdir(exist_ok=True)
    Path("results/scenarios.json").write_text(json.dumps(summary, indent=2) + "\n")

if __name__ == "__main__":
    run()
