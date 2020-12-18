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
