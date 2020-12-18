# Описание формата входного файла `input.json` для запуска расчёта в `PyHyCarSim`

Примеры файлов находятся в этом же репозитории. 

**Содержание `input.py` и `input.json` относятся к разным случаям и не являются идентичными друг другу! Выложены в качестве первых подвернувшихся под руку.**

## Входной файл `input.py`

Решение использовать входные файлы в формате `json` было принято после длительного использования в этом качестве питоновских файлов. Внутри `input.py` создаются объекты импортируемого питоновского модуля `HyCarSim`, описывающие расчётную модель скважины или ГСС.

Пример запуска из терминала

```shell
PyHyCarSim.exe input.py
```

Примеры питоновских файлов прилагаются.

<details>
<summary> Расчёт скважины, композиционная модель </summary>

```python

import HyCarSim as hcs
import math


components = [

    hcs.PureComponentProperties(name="C1",
                                carbon_number=1, molar_mass=0.0160428, pres_critical=4599200, temp_critical=190.564,
                                vol_critical=0.00009862, acentric_factor=0.0104, heat_capacity_gas=2224.67,
                                heat_capacity_liq=3299.30, evaporation_heat=511000, viscosity_gas=1.11e-5,
                                viscosity_liq=1.17e-4),

    hcs.PureComponentProperties(name="C2",
                                carbon_number=2, molar_mass=0.03007, pres_critical=4871800, temp_critical=305.33,
                                vol_critical=0.00014319, acentric_factor=0.0991, heat_capacity_gas=1745.59,
                                heat_capacity_liq=2278.02, evaporation_heat=487000, viscosity_gas=9.30e-6,
                                viscosity_liq=1.67e-4),

    hcs.PureComponentProperties(name="C3",
                                carbon_number=3, molar_mass=0.044096, pres_critical=4247660, temp_critical=369.85,
                                vol_critical=2e-4, acentric_factor=0.152, heat_capacity_gas=1669.09,
                                heat_capacity_liq=2230.59, evaporation_heat=428000, viscosity_gas=8.1e-6,
                                viscosity_liq=1.98e-4),

    hcs.PureComponentProperties(name="C4",
                                carbon_number=4, molar_mass=0.05812, pres_critical=3796000, temp_critical=425.16,
                                vol_critical=2.55e-4, acentric_factor=0.1985, heat_capacity_gas=1694.60,
                                heat_capacity_liq=2278.39, evaporation_heat=386098, viscosity_gas=7.35e-6,
                                viscosity_liq=2.04e-4),

    hcs.PureComponentProperties(name="iC4",
                                carbon_number=4, molar_mass=0.05812, pres_critical=3640000, temp_critical=407.85,
                                vol_critical=0.000256, acentric_factor=0.1844, heat_capacity_gas=1638.16,
                                heat_capacity_liq=2231.59, evaporation_heat=366483, viscosity_gas=7.44e-6,
                                viscosity_liq=2.14e-4),

    hcs.PureComponentProperties(name="C5",
                                carbon_number=5, molar_mass=0.07215, pres_critical=3366500, temp_critical=469.7,
                                vol_critical=0.000310991, acentric_factor=0.2513, heat_capacity_gas=1664.17,
                                heat_capacity_liq=2317.26, evaporation_heat=357450, viscosity_gas=7.37e-6,
                                viscosity_liq=2.20e-4),

    hcs.PureComponentProperties(name="iC5",
                                carbon_number=5, molar_mass=0.07215, pres_critical=3377000, temp_critical=460.45,
                                vol_critical=0.000306, acentric_factor=0.227, heat_capacity_gas=1664.17,
                                heat_capacity_liq=2284.82, evaporation_heat=342204, viscosity_gas=7.5e-6,
                                viscosity_liq=2.14e-4),

    hcs.PureComponentProperties(name="C6",
                                carbon_number=6, molar_mass=0.08618, pres_critical=3018100, temp_critical=507.82,
                                vol_critical=0.00037, acentric_factor=0.2979, heat_capacity_gas=1692,
                                heat_capacity_liq=2293.57, evaporation_heat=334764, viscosity_gas=6.44e-6,
                                viscosity_liq=3.07e-4),

    hcs.PureComponentProperties(name="C7",
                                carbon_number=7, molar_mass=0.10021, pres_critical=2727000, temp_critical=540.13,
                                vol_critical=0.00043, acentric_factor=0.3498, heat_capacity_gas=1688,
                                heat_capacity_liq=2241.69, evaporation_heat=317034, viscosity_gas=7.16e-6,
                                viscosity_liq=4.14e-4),

    hcs.PureComponentProperties(name="C8",
                                carbon_number=8, molar_mass=0.11423, pres_critical=2497000, temp_critical=569.32,
                                vol_critical=0.000487, acentric_factor=0.396, heat_capacity_gas=1685.86,
                                heat_capacity_liq=2238.29, evaporation_heat=301234, viscosity_gas=7.55e-6,
                                viscosity_liq=5.46e-4)
]

binary_coefficients = [

    hcs.InteractionBinaryCoefficient(name1="C1", name2="C2", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C3", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="iC4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C2", name2="C3", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="iC4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C3", name2="C4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="iC4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C4", name2="iC4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="iC4", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC4", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC4", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC4", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC4", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C5", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C5", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C5", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C5", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="iC5", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC5", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC5", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C6", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C6", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C7", name2="C8", k=0)
]

water = hcs.Properties(viscosity=5.5e-4, density=1040, compressibility=4.4e-10, heat_capacity=4200, thermal_cond=0.6)
numerical_parameters = hcs.NumericalParameters(model='Base', wall_friction_factor=1, heat_transfer_factor=1)
solver = hcs.UpwindSolver(components, water, binary_coefficients, numerical_parameters)

T_wellhead = 316.6  # real data
T_bottom_hole = 378.5  # syntetic
P_wellhead = 2.81e7  # real data
P_bottom_hole = 3.91e7  # syntetic
Rough = 0.001
Diam = 0.0889
F_liq = 0
F_gas = 1
F_water = 0
Molar_frac = [0.82532, 0.08204, 0.03846, 0.01147, 0.00961, 0.00413, 0.00439, 0.0087, 0.00931, 0.00657]

solver.traverse_simple_circuit(units=[

    hcs.PressureBoundaryCondition('bc_left', pressure=P_wellhead, temperature=T_wellhead, frac_water=F_water,
                                  frac_liquid=F_liq, frac_gas=F_gas, molar_fraction=Molar_frac),
    hcs.Channel(name="channel", parts=[

        hcs.ChannelPart(
            PartName="1",
            length=1000,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-90)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=2.811e7,
            wall_temperature=331,
            temperature=331,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="2",
            length=55,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-83.3)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=2.83e7,
            wall_temperature=332,
            temperature=332,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="3",
            length=45,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-65.7)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=2.85e7,
            wall_temperature=333,
            temperature=333,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="4",
            length=80,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-69)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=2.88e7,
            wall_temperature=335,
            temperature=335,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="5",
            length=80,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-61)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=2.9e7,
            wall_temperature=336,
            temperature=336,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="6",
            length=30,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-58.3)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=2.93e7,
            wall_temperature=337,
            temperature=337,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="7",
            length=30,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-50)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=2.95e7,
            wall_temperature=338,
            temperature=338,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="8",
            length=228,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-53.1)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=2.98e7,
            wall_temperature=341,
            temperature=341,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="9",
            length=76,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-48.6)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3e7,
            wall_temperature=342,
            temperature=342,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="10",
            length=76,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-49.6)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.2e7,
            wall_temperature=343,
            temperature=343,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="11",
            length=759,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-47.5)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.3e7,
            wall_temperature=351,
            temperature=351,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="12",
            length=455,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-47.5)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.4e7,
            wall_temperature=356,
            temperature=356,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="13",
            length=456,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-49.7)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.5e7,
            wall_temperature=362,
            temperature=362,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="14",
            length=56,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-49)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.6e7,
            wall_temperature=363,
            temperature=363,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="15",
            length=279,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-58)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.65e7,
            wall_temperature=368,
            temperature=368,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="16",
            length=35,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-60.1)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.7e7,
            wall_temperature=369,
            temperature=369,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="17",
            length=35,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-70.6)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.75e7,
            wall_temperature=370,
            temperature=370,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="18",
            length=75,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-70.6)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.8e7,
            wall_temperature=371,
            temperature=371,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="19",
            length=150,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-76.7)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.85e7,
            wall_temperature=374,
            temperature=374,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="20",
            length=109,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-80.6)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.9e7,
            wall_temperature=376,
            temperature=376,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="21",
            length=121,
            ncells=1,
            roughness=Rough,
            sine=math.sin(math.radians(-90)),
            diameter=Diam,
            frac_liquid=F_liq,
            frac_gas=F_gas,
            frac_water=F_water,
            pressure=3.9e7,
            wall_temperature=378,
            temperature=378,
            molar_fraction=Molar_frac),
    ]),

    hcs.MassFlowBoundaryCondition('bc_rigth', flux=1.5, temperature=T_bottom_hole, frac_water=F_water,
                                  frac_liquid=F_liq, frac_gas=F_gas, molar_fraction=Molar_frac)

])

solver.compute_all(time=5000, dt=5e-3, dtmax=5e-2, delta_seconds=50, path_text='output.tsv')
```

</details>

<details>
<summary> Расчёт ГСС, модель black oil </summary>

```python

import HyCarSim as hcs
import math


fluid = hcs.Properties(viscosity=8e-3, density=760, compressibility=1e-10, heat_capacity=4200, thermal_cond=0.6)
gas = hcs.Properties(viscosity=1.05e-5, density=0.815157, compressibility=5 * 1e-8, heat_capacity=3200,
                     thermal_cond=0.3)
water = hcs.Properties(viscosity=5.5e-4, density=1040, compressibility=4.4e-10, heat_capacity=4200, thermal_cond=0.6)

numerical_parameters = hcs.NumericalParameters(model='BeggsBrill', wall_friction_factor=1, heat_transfer_factor=1.0)

solver = hcs.ComputationPipeLineCircuit(fluid, gas, water, numerical_parameters)

Pkoeff = 1
T_wall = 30
rough0 = 0.00000
rough1 = 0.000005 * 1  # 0.000005
rough2 = 0.0001 * 1  # 0.0001
rough3 = 0.000152 * 1  # 0.000152

f_l_sc = 0.0004  # frac liquid standard condition

solver.pipeline_circuit(

    pipes=[

        hcs.Pipe(name="pipe_2-28-01",
                 length=65,  # adaptible
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.191,  # GAP data
                 roughness=rough0,  # adaptible
                 frac_liquid=f_l_sc * 102.56,  # GAP data
                 frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                 frac_water=0,  # same as well
                 pressure=102.56 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=43.42 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="pipe_2-28-03",
                 length=65 + 35 * 2,  # adaptible
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.191,  # GAP data
                 roughness=rough0,  # adaptible
                 frac_liquid=f_l_sc * 102.56,  # GAP data
                 frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                 frac_water=0.00000,  # same as well
                 pressure=102.56 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=43.42 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="pipe_2-28-04",
                 length=65 + 35 * 3,  # adaptible
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.191,  # GAP data
                 roughness=rough0,  # adaptible
                 frac_liquid=f_l_sc * 102.56,  # GAP data
                 frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                 frac_water=0,  # same as well
                 pressure=102.56 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=43.42 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="pipe_2-28-05",
                 length=65 + 35 * 4,  # adaptible
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.191,  # GAP data
                 roughness=rough0,  # adaptible
                 frac_liquid=f_l_sc * 102.56,  # GAP data
                 frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                 frac_water=0,  # same as well
                 pressure=102.56 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=43.42 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="pipe_2-28-06",
                 length=65 + 35 * 5,  # adaptible
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.191,  # GAP data
                 roughness=rough0,  # adaptible
                 frac_liquid=f_l_sc * 102.56,  # GAP data
                 frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                 frac_water=0,  # same as well
                 pressure=102.56 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=43.42 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="pipe_2-28-07",
                 length=65 + 35 * 6,  # adaptible
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.191,  # GAP data
                 roughness=rough0,  # adaptible
                 frac_liquid=f_l_sc * 102.56,  # GAP data
                 frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                 frac_water=0,  # same as well
                 pressure=102.56 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=43.42 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="pipe_2-28-08",
                 length=65 + 35 * 7,  # adaptible
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.191,  # GAP data
                 roughness=rough0,  # adaptible
                 frac_liquid=f_l_sc * 102.56,  # GAP data
                 frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                 frac_water=0,  # same as well
                 pressure=102.56 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=43.42 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="PIPE_K-228_TVR-243",
                 length=4258,  # GAP data
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.191,  # GAP data
                 roughness=rough1,  # GAP data
                 frac_liquid=f_l_sc * 99,  # GAP data
                 frac_gas=1.0 - f_l_sc * 99,  # GAP data
                 frac_water=0.00000,  # GAP data
                 pressure=99 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=38 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="PIPE_TVR-243_TVR-226",
                 length=1497,  # GAP data
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.285,  # GAP data
                 roughness=rough1,  # GAP data
                 frac_liquid=f_l_sc * 92,  # GAP data
                 frac_gas=1.0 - f_l_sc * 92,  # GAP data
                 frac_water=0.000,  # GAP data
                 pressure=92 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=31.4 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="PIPE_K-226_TVR-226",
                 length=197,  # GAP data
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.139,  # GAP data
                 roughness=rough2,  # GAP data
                 frac_liquid=f_l_sc * 92.07,  # GAP data
                 frac_gas=1.0 - f_l_sc * 92.07,  # GAP data
                 frac_water=0.00000,  # GAP data
                 pressure=92.07 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=30.2 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="pipe_2-26-01",
                 length=65,  # adaptible
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.139,  # GAP data
                 roughness=rough0,  # adaptible
                 frac_liquid=f_l_sc * 92.14,  # GAP data
                 frac_gas=1.0 - f_l_sc * 92.14,  # GAP data
                 frac_water=0,  # GAP data
                 pressure=92.14 * 1e5 * Pkoeff,  # GAP data
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=30.36 + 273.15,  # GAP data
                 molar_fraction=[]),

        hcs.Pipe(name="pipe_2-26-03",
                 length=65 + 2 * 35,  # adaptible
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.139,  # GAP data
                 roughness=rough0,  # adaptible
                 frac_liquid=f_l_sc * 92.14,  # GAP data
                 frac_gas=1.0 - f_l_sc * 92.14,  # GAP data
                 frac_water=0,  # GAP data
                 pressure=92.14 * 1e5 * Pkoeff,  # GAP data
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=30.36 + 273.15,  # GAP data
                 molar_fraction=[]),

        hcs.Pipe(name="PIPE_PRM-6",
                 length=14,  # GAP data
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.285,  # GAP data
                 roughness=rough3,  # GAP data
                 frac_liquid=f_l_sc * 91.9,  # GAP data
                 frac_gas=1.0 - f_l_sc * 91.9,  # GAP data
                 frac_water=0.00000,  # GAP data
                 pressure=91.9 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=31.1 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="PIPE_PRM219_to_203",
                 length=35.27,  # GAP data
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.285,  # GAP data
                 roughness=rough1,  # GAP data
                 frac_liquid=f_l_sc * 91.86,  # GAP data
                 frac_gas=1.0 - f_l_sc * 91.86,  # GAP data
                 frac_water=0.00000,  # GAP data
                 pressure=91.86 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=31.1 + 273.15,  # same as well
                 molar_fraction=[]),

        hcs.Pipe(name="PIPE_PRM203_UKPG2",
                 length=538.97,  # GAP data
                 sine=math.sin(math.radians(0)),  # GAP data
                 diameter=0.285,  # GAP data
                 roughness=rough2,  # GAP data
                 frac_liquid=f_l_sc * 91.8,  # GAP data
                 frac_gas=1.0 - f_l_sc * 91.8,  # GAP data
                 frac_water=0.00000,  # GAP data
                 pressure=91.8 * 1e5 * Pkoeff,  # same as well
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=30.7 + 273.15,  # same as well
                 molar_fraction=[])

    ],
    nodes=[

        hcs.PressureBoundNode(name="well_2-28-01",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 102.56,  # GAP data
                              frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                              frac_water=0,  # GAP data
                              pressure=102.56 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=43.42 + 273.15,  # GAP data
                              molar_fraction=[]),

        hcs.PressureBoundNode(name="well_2-28-03",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 102.56,  # GAP data
                              frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                              frac_water=0.00,  # GAP data
                              pressure=102.56 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=43.42 + 273.15,  # GAP data
                              molar_fraction=[]),

        hcs.PressureBoundNode(name="well_2-28-04",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 102.56,  # GAP data
                              frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                              frac_water=0,  # GAP data
                              pressure=102.56 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=43.42 + 273.15,  # GAP data
                              molar_fraction=[]),

        hcs.PressureBoundNode(name="well_2-28-05",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 102.56,  # GAP data
                              frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                              frac_water=0,  # GAP data
                              pressure=102.56 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=43.42 + 273.15,  # GAP data
                              molar_fraction=[]),

        hcs.PressureBoundNode(name="well_2-28-06",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 102.56,  # GAP data
                              frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                              frac_water=0,  # GAP data
                              pressure=102.56 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=43.42 + 273.15,  # GAP data
                              molar_fraction=[]),

        hcs.PressureBoundNode(name="well_2-28-07",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 102.56,  # GAP data
                              frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                              frac_water=0,  # GAP data
                              pressure=102.56 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=43.42 + 273.15,  # GAP data
                              molar_fraction=[]),

        hcs.PressureBoundNode(name="well_2-28-08",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 102.56,  # GAP data
                              frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                              frac_water=0,  # GAP data
                              pressure=102.56 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=43.42 + 273.15,  # GAP data
                              molar_fraction=[]),

        hcs.Node(name="K-228",
                 length=1,  # fictional
                 sine=math.sin(math.radians(0)),  # fictional
                 diameter=0.159,  # fictional
                 roughness=rough0,  # fictional
                 frac_liquid=f_l_sc * 102.56,  # GAP data
                 frac_gas=1.0 - f_l_sc * 102.56,  # GAP data
                 frac_water=0.00000,  # GAP data
                 pressure=102.56 * 1e5 * Pkoeff,  # variable
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=43.42 + 273.15,  # variable
                 molar_fraction=[]),

        hcs.Node(name="TVR-243",
                 length=1,  # fictional
                 sine=math.sin(math.radians(0)),  # fictional
                 diameter=0.159,  # fictional
                 roughness=rough0,  # fictional
                 frac_liquid=f_l_sc * 92.5,  # GAP data
                 frac_gas=1.0 - f_l_sc * 92.5,  # GAP data
                 frac_water=0.00000,  # GAP data
                 pressure=92.5 * 1e5 * Pkoeff,  # variable
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=33.25 + 273.15,  # variable
                 molar_fraction=[]),

        hcs.Node(name="TVR-226",
                 length=1,  # fictional
                 sine=math.sin(math.radians(0)),  # fictional
                 diameter=0.159,  # fictional
                 roughness=rough0,  # fictional
                 frac_liquid=f_l_sc * 91.89,  # GAP data
                 frac_gas=1.0 - f_l_sc * 91.89,  # GAP data
                 frac_water=0.00000,  # GAP data
                 pressure=91.89 * 1e5 * Pkoeff,  # variable
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=31.2 + 273.15,  # variable
                 molar_fraction=[]),

        hcs.Node(name="K-226",
                 length=1,  # fictional
                 sine=math.sin(math.radians(0)),  # fictional
                 diameter=0.159,  # fictional
                 roughness=rough0,  # fictional
                 frac_liquid=f_l_sc * 92.14,  # GAP data
                 frac_gas=1.0 - f_l_sc * 92.14,  # GAP data
                 frac_water=0,  # GAP data
                 pressure=92.14 * 1e5 * Pkoeff,  # variable
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=30.36 + 273.15,  # variable
                 molar_fraction=[]),

        hcs.PressureBoundNode(name="well_2-26-01",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 92.14,  # GAP data
                              frac_gas=1.0 - f_l_sc * 92.14,  # GAP data
                              frac_water=0,  # GAP data
                              pressure=92.14 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=30.36 + 273.15,  # GAP data
                              molar_fraction=[]),

        hcs.PressureBoundNode(name="well_2-26-03",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 92.14,  # GAP data
                              frac_gas=1.0 - f_l_sc * 92.14,  # GAP data
                              frac_water=0,  # GAP data
                              pressure=92.14 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=30.36 + 273.15,  # GAP data
                              molar_fraction=[]),

        hcs.Node(name="PRM-6",
                 length=1,  # fictional
                 sine=math.sin(math.radians(0)),  # fictional
                 diameter=0.159,  # fictional
                 roughness=rough0,  # fictional
                 frac_liquid=f_l_sc * 91.88,  # GAP data
                 frac_gas=1.0 - f_l_sc * 91.88,  # GAP data
                 frac_water=0.00000,  # GAP data
                 pressure=91.88 * 1e5 * Pkoeff,  # variable
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=31.16 + 273.15,  # variable
                 molar_fraction=[]),

        hcs.Node(name="TVR_PRM_to_UKPG2",
                 length=1,  # fictional
                 sine=math.sin(math.radians(0)),  # fictional
                 diameter=0.159,  # fictional
                 roughness=rough0,  # fictional
                 frac_liquid=f_l_sc * 91.86,  # GAP data
                 frac_gas=1.0 - f_l_sc * 91.86,  # GAP data
                 frac_water=0.00000,  # variable
                 pressure=91.86 * 1e5 * Pkoeff,  # variable
                 wall_temperature=T_wall + 273.15,  # GAP data
                 temperature=31.08 + 273.15,  # variable
                 molar_fraction=[]),

        hcs.PressureBoundNode(name="UKPG_VU_OLD",
                              length=1,  # fictional
                              sine=math.sin(math.radians(0)),  # fictional
                              diameter=0.159,  # fictional
                              roughness=rough0,  # fictional
                              frac_liquid=f_l_sc * 91.4,  # GAP data
                              frac_gas=1.0 - f_l_sc * 91.4,  # GAP data
                              frac_water=0.0,  # GAP data
                              pressure=91.4 * 1e5 * Pkoeff,  # GAP data
                              wall_temperature=T_wall + 273.15,  # GAP data
                              temperature=30.3 + 273.15,  # GAP data
                              molar_fraction=[])
    ],
    connections=[

        hcs.Connection(node_name="well_2-28-01",
                       input_pipes=[],
                       output_pipes=["pipe_2-28-01"]),

        hcs.Connection(node_name="well_2-28-03",
                       input_pipes=[],
                       output_pipes=["pipe_2-28-03"]),

        hcs.Connection(node_name="well_2-28-04",
                       input_pipes=[],
                       output_pipes=["pipe_2-28-04"]),

        hcs.Connection(node_name="well_2-28-05",
                       input_pipes=[],
                       output_pipes=["pipe_2-28-05"]),

        hcs.Connection(node_name="well_2-28-06",
                       input_pipes=[],
                       output_pipes=["pipe_2-28-06"]),

        hcs.Connection(node_name="well_2-28-07",
                       input_pipes=[],
                       output_pipes=["pipe_2-28-07"]),

        hcs.Connection(node_name="well_2-28-08",
                       input_pipes=[],
                       output_pipes=["pipe_2-28-08"]),

        hcs.Connection(node_name="well_2-26-01",
                       input_pipes=[],
                       output_pipes=["pipe_2-26-01"]),

        # hcs.Connection(node_name = "well_2-26-02",
        # input_pipes = [],
        # output_pipes = ["pipe_2-26-02"]),

        hcs.Connection(node_name="well_2-26-03",
                       input_pipes=[],
                       output_pipes=["pipe_2-26-03"]),

        hcs.Connection(node_name="K-228",
                       input_pipes=["pipe_2-28-01", "pipe_2-28-03", "pipe_2-28-04", "pipe_2-28-05", "pipe_2-28-06",
                                    "pipe_2-28-07", "pipe_2-28-08"],
                       output_pipes=["PIPE_K-228_TVR-243"]),

        hcs.Connection(node_name="TVR-243",
                       input_pipes=["PIPE_K-228_TVR-243"],
                       output_pipes=["PIPE_TVR-243_TVR-226"]),

        hcs.Connection(node_name="TVR-226",
                       input_pipes=["PIPE_TVR-243_TVR-226", "PIPE_K-226_TVR-226"],
                       output_pipes=["PIPE_PRM-6"]),

        hcs.Connection(node_name="K-226",
                       input_pipes=["pipe_2-26-01", "pipe_2-26-03"],
                       output_pipes=["PIPE_K-226_TVR-226"]),

        hcs.Connection(node_name="PRM-6",
                       input_pipes=["PIPE_PRM-6"],
                       output_pipes=["PIPE_PRM219_to_203"]),

        hcs.Connection(node_name="TVR_PRM_to_UKPG2",
                       input_pipes=["PIPE_PRM219_to_203"],
                       output_pipes=["PIPE_PRM203_UKPG2"]),

        hcs.Connection(node_name="UKPG_VU_OLD",
                       input_pipes=["PIPE_PRM203_UKPG2"],
                       output_pipes=[])

    ])

solver.compute_all(time=30000, dt=1e-2, dtmax=0.5, delta_seconds=100, path_text='output.tsv', path_CSV='output.csv')
```

</details>


## Входной файл `input.json`

Структура джсона сделана на основе `input.py`, но структурирована иерархически.
Количество объектов на одному уровне не ограничено, основное условие - они должны быть взаимонезависимы.
Если объект_2 зависит от объекта_1, он должен находиться ниже по структуре, в ключе объекта_1.

Главный объект расчёта - **солвер**, расчёт проводится внутри его логики. Основное внимание нужно уделять именно солверу.

На данный момент реализовано пять солверов
* UpwindSolver: скважина
* ComputationPipeLineCircuit: наземная сеть  
* DiagramSolver: диаграмма фазового равновесия
* CorrelationSolver: корреляционный расчёт скважины
* CorrelationSolverGSS: корреляционный расчёт наземной сети

### Верхний уровень джсона определяет солвер и сопутствующую информацию
```json
{
  "template_version": 0.1,  // версия формата json, для отслеживания изменений в нотации
  "meta": {},               // человекочитаемая информация о расчёте
  "solver": {},             // тип солвера и все его параметры
  "output_regulations": {}, // [в разработке] правила, определяющие формат выходных данных
  "GlobalLogger": {}        // запись отладочных логов
}
```

### Уровень солвера в джсоне определяет все параметры расчёта, сгруппированные по вторичным объектам
```json
{
  "solver": {
    "type": "UpwindSolver",   // тип солвера
    "pvt_model": { },         // модель материала
    "numerical_params": { },  // численные параметры расчёта
    "solver_methods": { }     // методы расчёта
  }
}
```

[Отрисовка jsona для скважины](http://www.plantuml.com/plantuml/uml/xPXTRzis58Rlyoi2NzS2FqHzzAf81Woz6GeClHeAWQQERMuIfP6qss3eVnzfdyocd4OU6g30bW858hwl3W-F7bB7UkUyjFvtDvYRlsvkRnTkwFPW5szlurMuzWyZXAl5n_6pDkslH_NDKHltlkc75Zgq9pUeeHy7fpsWEqWzU8bM76cbXqPPa1xQU1CZZ2mfMvBgbXPlcNYRyqnGUWo1yRNl87hlambG_VdZ-v-YM01PYxQkG2ZPAYvaoTUrOYKXWfTrAt9AoweWxUbUpDY0yIv4-0t73yfdwUEgpuVkwUIQJQxvuf_BJ_ZNLtIS5GVBaSnp6aeA-i4E8rYlmQKpxRLJCTP3C96C4294ehTWKAKa9uaKqx3Wd5xfxcZ9inoMD7LjGVf6oL4gz32I6lmMR2-xHWscFIHHe8fBdgblijpWCxAF2qvBd9PYP-7-CLfIbyIkf5qDfZ6xVdKeAvte_T19s_JIkMFfQ45oLarCiK01KUsraX7qNDGr8sIQ6VJZkOlM91D5Fd7jX-xSL6TLmM19nCGc5HXljMhMKld1Od9a6YrvBir6nbKmnlAiA9zrTlhFuEIihZC-CS9UZeELNeUonPk2Jr1AakKcpE6qDACqMKXYmpaHJqfBT24Wyo2m5mQ1pO302IddCAXAMirYm8d8E7-M0YnApcbz3GPrJQ_0W9Qvo4Hz1GQCbLL6s3m7OS7p70IY0WR5LHWK_ne3_i8Oy1aCyfpKnHm7B2-BOfQ38knrSGK7x0e6g63N8524ESbr2722iCmWmAfv1AgCNer0NPqZS7fVdhqqLjf8-z2e0TPhhVIpRu-4YVV6WvKgvdztY75_2f60WOJHv9MJIEpfG-YFk8w4uH-G5VznMR7loUgoERevotOHzYZOk36QKLhPk_CEyx7bNDp1PkFkhEwwKu_vMNPTixRwi9ZpNIFGWdl0MsdS6kp9GiyJm3wuwS5lXpQPtbiP50UDq_tOGQEqLJljqqvkfPeErlxRlHmujxDmD-nCUwYtQNNC61SoEVamMYgE62COMCu9IROcda5WfJzQE2qITMsbQXxxJN8fXMswq-tJ6XumGPYUdMkaADsYuH_9AYOuUpCPf5o8Waz72Q_J9k7Ja_ta_LOQa_puI8gcK4wB9crwWAJROlgSS8eFqeRYJqrnz1USZ5pA7PYDtmPH478X6WLTvw9u8TbXjzaQS575fchYSDh4IPVqGccr3CG2zWfbZgMTVRZp3tW6cWiYAqeZaTdKXJjq2cVzX77UCuFTC-XTuZU3O88XelZ23D5NXbuP-aw6s2j3_pk6Pb-KAzLOlTc-N3U2uRxLZd11oAJebtNC_oCDoPFVzdOUce1NsXDwVQXV-ZbbqNhyEIIImLv-YRiIbkny63el6mTgCErXnKcaKVfju-5B3BWOTZvaaNctNwGDzaty__Nc7PWsVlNz6m00)

