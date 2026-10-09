from pyomo.environ import *
import pandas as pd

def build_ferrari_model(fna_transport_coefficient=0.00015):
    """Crea y devuelve el modelo Pyomo para el problema de distribución Ferrari."""

    model = ConcreteModel(name="Ferrari_Distribution_Optimization")
    model.M = Set(initialize=range(1,14))
    model.H = Set(initialize=[1, 2, 3, 4])
    hp_data = [
        (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
        (2,1),(2,2),(2,3),
        (3,1),(3,2),(3,3),
        (4,1),(4,2),(4,3)
    ]
    model.HP = Set(dimen=2, initialize=hp_data)

    w_data = {
        1:1470,  2:1540,  3:1570,  4:1670,  5:1570,  6:1545,  7:1600,
        8:2108,  9:1592, 10:1587, 11:1560, 12:1660, 13:1485
    }
    model.w = Param(model.M, initialize=w_data)

    model.w_medio = Param(initialize=1612)

    g_data = {
        1:275500,  2:320000,  3:430000,  4:473000,  5:220000,  
        6:284000,  7:336000,  8:450000,  9:499000, 10:645000,
        11:770000, 12:850000, 13:2000000
    }
    model.g = Param(model.M, initialize=g_data)

    d_h_data = {
        1:1200,  # EMEA
        2:7500,  # FNA
        3:9000,  # FGC
        4:8500   # APAC
    }
    model.d_h = Param(model.H, initialize=d_h_data)

    d_hp_data = {
        (1,1):1500,(1,2):600, (1,3):1300,(1,4):2000,(1,5):1000,(1,6):3500,
        (2,1):1000,(2,2):1500,(2,3):4500,
        (3,1):1000,(3,2):800, (3,3):1200,
        (4,1):5000,(4,2):1500,(4,3):6000
    }
    model.d_hp = Param(model.HP, initialize=d_hp_data)

    alpha_h_data = {
        1:0.00010,  # EMEA
        2:fna_transport_coefficient,  # FNA
        3:0.00025,  # FGC
        4:0.00020   # APAC
    }
    model.alpha_h = Param(model.H, initialize=alpha_h_data)

    alpha_hp_data = {
        (1,1):0.00006,(1,2):0.00005,(1,3):0.00007,(1,4):0.00008,(1,5):0.00006,(1,6):0.00010,
        (2,1):0.00008,(2,2):0.00009,(2,3):0.00012,
        (3,1):0.00008,(3,2):0.00007,(3,3):0.00009,
        (4,1):0.00015,(4,2):0.00010,(4,3):0.00016
    }
    model.alpha_hp = Param(model.HP, initialize=alpha_hp_data)

    c_h_data = {1:6600, 2:4500, 3:1700, 4:2500}
    model.c_h = Param(model.H, initialize=c_h_data)

    c_hp_data = {
        (1,1):1200,(1,2):1000,(1,3):1700,(1,4):1100,(1,5):1300,(1,6):800,
        (2,1):3900,(2,2):600, (2,3):700,
        (3,1):1300,(3,2):250, (3,3):75,
        (4,1):1200,(4,2):800, (4,3):800
    }
    model.c_hp = Param(model.HP, initialize=c_hp_data)

    e_mh_data = {
     (1,1):706,(1,2):444,(1,3):173,(1,4):267,
     (2,1):706,(2,2):444,(2,3):173,(2,4):267,
     (3,1):706,(3,2):444,(3,3):173,(3,4):267,
     (4,1):706,(4,2):444,(4,3):173,(4,4):267,
     (5,1):706,(5,2):444,(5,3):173,(5,4):267,
     (6,1):706,(6,2):444,(6,3):173,(6,4):267,
     (7,1):706,(7,2):444,(7,3):173,(7,4):267,

     (8,1):712,(8,2):444,(8,3):176,(8,4):270,

     (9,1):91,(9,2):57,(9,3):22,(9,4):34,
     (10,1):91,(10,2):57,(10,3):22,(10,4):34,
     (11,1):91,(11,2):57,(11,3):22,(11,4):34,

     (12,1):92,(12,2):58,(12,3):24,(12,4):36,

     (13,1):61,(13,2):39,(13,3):15,(13,4):23
    }
    model.e_mh = Param(model.M, model.H, initialize=e_mh_data, default=0)

    f_mh_data = {
     (1,1):777,(1,2):488,(1,3):190,(1,4):294,
     (2,1):777,(2,2):488,(2,3):190,(2,4):294,
     (3,1):777,(3,2):488,(3,3):190,(3,4):294,
     (4,1):777,(4,2):488,(4,3):190,(4,4):294,
     (5,1):777,(5,2):488,(5,3):190,(5,4):294,
     (6,1):777,(6,2):488,(6,3):190,(6,4):294,
     (7,1):777,(7,2):488,(7,3):190,(7,4):294,

     (8,1):887,(8,2):558,(8,3):222,(8,4):334,

     (9,1):100,(9,2):63,(9,3):24,(9,4):38,
     (10,1):100,(10,2):63,(10,3):24,(10,4):38,
     (11,1):100,(11,2):63,(11,3):24,(11,4):38,

     (12,1):104,(12,2):66,(12,3):27,(12,4):41,

     (13,1):66,(13,2):41,(13,3):19,(13,4):25
     }

    model.f_mh = Param(model.M, model.H, initialize=f_mh_data, default=999999)

    e_hp_data = {

      (1,1):991,(1,2):859,(1,3):1453,(1,4):925,(1,5):1123, (1,6):729,

      (2,1):3002,(2,2):341,(2,3):477,
      (3,1):1207,(3,2):213,(3,3):72,
      (4,1):973,(4,2):619,(4,3):708
    }
    model.e_hp = Param(model.HP, initialize=e_hp_data, default=0)

    f_hp_data = {
      (1,1):1108,(1,2):960,(1,3):1625,(1,4):1034,(1,5):1255,(1,6):814,
      (2,1):3355,(2,2):381,(2,3):534,
      (3,1):1351,(3,2):238,(3,3):81,
      (4,1):1088,(4,2):692,(4,3):792
    }
    model.f_hp = Param(model.HP, initialize=f_hp_data, default=999999)


    model.x = Var(model.M, model.H, within=NonNegativeIntegers)  # x_{m,h}
    model.y = Var(model.HP,         within=NonNegativeIntegers)   # y_{h,p}



    def total_profit_rule(mdl):
        ingreso = sum(mdl.g[m] * mdl.x[m,h] for m in mdl.M for h in mdl.H)
        cost_mh = sum(mdl.alpha_h[h] * mdl.d_h[h] * mdl.w[m] * mdl.x[m,h]
                      for m in mdl.M for h in mdl.H)
        cost_hp = sum(mdl.alpha_hp[h,p] * mdl.d_hp[h,p] * mdl.w_medio * mdl.y[h,p]
                      for (h,p) in mdl.HP)

        return ingreso - (cost_mh + cost_hp)

    model.obj = Objective(rule=total_profit_rule, sense=maximize)

    def min_demand_mh_rule(mdl, mm, hh):
        return mdl.x[mm, hh] >= mdl.e_mh[mm, hh]
    model.min_demand_mh = Constraint(model.M, model.H, rule=min_demand_mh_rule)

    def max_demand_mh_rule(mdl, mm, hh):
        return mdl.x[mm, hh] <= mdl.f_mh[mm, hh]
    model.max_demand_mh = Constraint(model.M, model.H, rule=max_demand_mh_rule)

    def min_demand_hp_rule(mdl, hh, pp):
        return mdl.y[hh, pp] >= mdl.e_hp[hh, pp]
    model.min_demand_hp = Constraint(model.HP, rule=min_demand_hp_rule)

    def max_demand_hp_rule(mdl, hh, pp):
        return mdl.y[hh, pp] <= mdl.f_hp[hh, pp]
    model.max_demand_hp = Constraint(model.HP, rule=max_demand_hp_rule)

    def capacity_h_rule(mdl, hh):
        return sum(mdl.x[m, hh] for m in mdl.M) <= mdl.c_h[hh]
    model.cap_h = Constraint(model.H, rule=capacity_h_rule)

    def capacity_hp_rule(mdl, hh, pp):
        return mdl.y[hh, pp] <= mdl.c_hp[hh, pp]
    model.cap_hp = Constraint(model.HP, rule=capacity_hp_rule)

    def flow_rule(mdl, hh):
        return sum(mdl.x[m, hh] for m in mdl.M) == sum(mdl.y[hh, p] for (h2,p) in mdl.HP if h2 == hh)
    model.flow_constraint = Constraint(model.H, rule=flow_rule)

    return model

def print_distribution(model):
    model_names = [
        "296 GTB V6 Hybrid", 
        "296 GTS V6 Hybrid", 
        "SF90 Stradale V8 Hybrid",
        "SF90 Spider V8 Hybrid", 
        "Roma V8", 
        "Portofino M V8", 
        "812 GTS V12",
        "Purosangue V12", 
        "812 Competizione", 
        "812 Competizione A",
        "SF90 XX Stradale", 
        "SF90 XX Spider", 
        "Daytona SP3"
    ]

    # Creación de un DataFrame para las x[m,h]
    x_data = {'Model': model_names}
    hubs = ['EMEA', 'FNA', 'FCG', 'APAC']
    for h in model.H:
        x_data[hubs[h-1]] = [model.x[m,h].value for m in model.M]
    df_x = pd.DataFrame(x_data)
    print("\n=== Distribución de modelos en Hubs ===")
    print(df_x)

    hub_pos_names = [
        "North Europe", 
        "Central Europe", 
        "West Europe", 
        "East Europe",
        "South Europe", 
        "Middle East", 
        "USA", 
        "Canada", 
        "Latin America",
        "Mainland China", 
        "Taiwan", 
        "Hong Kong", 
        "North East Asia",
        "South East Asia", 
        "Australasia"
    ]
    y_data = {'Hub': [], 'Region': [], 'Entregas': []}
    hub_idx = 0
    for (h, p) in model.HP:
        y_data['Hub'].append(hubs[h-1])
        y_data['Region'].append(hub_pos_names[hub_idx])
        y_data['Entregas'].append(model.y[h,p].value)
        hub_idx += 1
    df_y = pd.DataFrame(y_data)
    print("\n=== Entregas desde Hub hasta POS ===")
    print(df_y)

def print_ganancia_total(model):
    ganancia_total = value(model.obj)
    formatted_ganancia = f"{ganancia_total:,.2f}"
    print(f"Objective (assumed vehicle values minus transport): {formatted_ganancia} EUR")
    

