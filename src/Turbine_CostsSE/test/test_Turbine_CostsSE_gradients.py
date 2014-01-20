
#!/usr/bin/env python
# encoding: utf-8
"""
test_Turbine_CostsSE.py

Created by Katherine Dykes on 2014-01-07.
Copyright (c) NREL. All rights reserved.
"""

import unittest
import numpy as np
from commonse.utilities import check_gradient_unit_test

from Turbine_CostsSE.Turbine_CostsSE.Tower_CostsSE import TowerCostAdder, TowerCost
from Turbine_CostsSE.Turbine_CostsSE.Rotor_CostsSE import BladeCost, HubCost, PitchSystemCost, SpinnerCost, \
                                                          HubSystemCostAdder, RotorCostAdder
from Turbine_CostsSE.Turbine_CostsSE.Nacelle_CostsSE import LowSpeedShaftCost, BearingsCost, GearboxCost, \
                                                            HighSpeedSideCost, GeneratorCost, BedplateCost, \
                                                            YawSystemCost, NacelleSystemCostAdder
from Turbine_CostsSE.Turbine_CostsSE.Turbine_CostsSE import TurbineCostAdder

from Turbine_CostsSE.NREL_CSM_TCC.tower_csm_component import tower_csm_component
from Turbine_CostsSE.NREL_CSM_TCC.blades_csm_component import blades_csm_component
from Turbine_CostsSE.NREL_CSM_TCC.hub_csm_component import hub_csm_component
from Turbine_CostsSE.NREL_CSM_TCC.nacelle_csm_component import nacelle_csm_component
from Turbine_CostsSE.NREL_CSM_TCC.nrel_csm_tcc import rotor_mass_adder, tcc_csm_component

# Turbine_CostsSE Model
# ----------------------------------------------------------
# Tower Components
class TestTowerCost(unittest.TestCase):

    def test1(self):

        tower = TowerCost()
    
        tower.tower_mass = 434559.0
        tower.curr_yr = 2009
        tower.curr_mon =  12

        check_gradient_unit_test(self, tower)

class TestTowerCostAdder(unittest.TestCase):

    def test1(self):

        tower = TowerCostAdder()
    
        tower.tower_cost = 1000000.0

        check_gradient_unit_test(self, tower)

#Rotor Components
class TestBladeCost(unittest.TestCase):

    def test1(self):

        blade = BladeCost()
    
        blade.blade_mass = 17650.67
        blade.curr_yr = 2009
        blade.curr_mon = 12

        check_gradient_unit_test(self, blade)

class TestHubCost(unittest.TestCase):

    def test1(self):

        hub = HubCost()
    
        hub.hub_mass = 31644.5
        hub.curr_yr = 2009
        hub.curr_mon = 12

        check_gradient_unit_test(self, hub)

class TestPitchSystemCost(unittest.TestCase):

    def test1(self):

        pitch = PitchSystemCost()
    
        pitch.pitch_system_mass = 17004.0
        pitch.curr_yr = 2009
        pitch.curr_mon = 12

        check_gradient_unit_test(self, pitch)

class TestSpinnerCost(unittest.TestCase):

    def test1(self):

        spinner = SpinnerCost()
    
        spinner.spinner_mass = 1810.5
        spinner.curr_yr = 2009
        spinner.curr_mon = 12

        check_gradient_unit_test(self, spinner)

class TestHubSystemCostAdder(unittest.TestCase):

    def test1(self):

        hub = HubSystemCostAdder()
    
        hub.hub_cost = 20000.0
        hub.pitch_system_cost = 20000.0
        hub.spinner_cost = 20000.0

        check_gradient_unit_test(self, hub)


class TestRotorCostAdder(unittest.TestCase):

    def test1(self):

        rotor = RotorCostAdder()
    
        rotor.blade_cost = 20000.0
        rotor.blade_number = 3
        rotor.hub_system_cost = 20000.0

        check_gradient_unit_test(self, rotor)


#Nacelle Components
class TestLowSpeedShaftCost(unittest.TestCase):

    def test1(self):

        lss = LowSpeedShaftCost()
    
        lss.low_speed_shaft_mass = 31257.3
        lss.curr_yr = 2009
        lss.curr_mon = 12

        check_gradient_unit_test(self, lss)

class TestBearingsCost(unittest.TestCase):

    def test1(self):

        bearings = BearingsCost()
    
        bearings.main_bearing_mass = 9731.41 / 2.0
        bearings.second_bearing_mass = 9731.41 / 2.0
        bearings.curr_yr = 2009
        bearings.curr_mon = 12

        check_gradient_unit_test(self, bearings)

class TestGearboxCost(unittest.TestCase):

    def test1(self):

        gearbox = GearboxCost()
    
        gearbox.gearbox_mass = 30237.60
        gearbox.curr_yr = 2009
        gearbox.curr_mon = 12
        gearbox.drivetrain_design = 1

        check_gradient_unit_test(self, gearbox)

class TestHighSpeedSideCost(unittest.TestCase):

    def test1(self):

        hss = HighSpeedSideCost()
    
        hss.high_speed_side_mass = 1492.45
        hss.curr_yr = 2009
        hss.curr_mon = 12

        check_gradient_unit_test(self, hss)

class TestGeneratorCost(unittest.TestCase):

    def test1(self):

        generator = GeneratorCost()
    
        generator.generator_mass = 16699.85
        generator.curr_yr = 2009
        generator.curr_mon = 12
        generator.drivetrain_design = 1
        generator.machine_rating = 5000.0

        check_gradient_unit_test(self, generator)

class TestBedplateCost(unittest.TestCase):

    def test1(self):

        bedplate = BedplateCost()
    
        bedplate.bedplate_mass = 93090.6
        bedplate.curr_yr = 2009
        bedplate.curr_mon = 12

        check_gradient_unit_test(self, bedplate)

class TestYawSystemCost(unittest.TestCase):

    def test1(self):

        yaw = YawSystemCost()
    
        yaw.yaw_system_mass = 11878.24
        yaw.curr_yr = 2009
        yaw.curr_mon = 12

        check_gradient_unit_test(self, yaw)

class TestNacelleSystemCostAdder(unittest.TestCase):

    def test1(self):

        nacelle = NacelleSystemCostAdder()

        nacelle.bedplate_mass = 93090.6    
        nacelle.machine_rating = 5000.0
        nacelle.drivetrainDesign = 1
        nacelle.crane = True
        nacelle.offshore = True
        nacelle.curr_yr = 2009
        nacelle.curr_mon = 12
        nacelle.lss_cost = 10000.0
        nacelle.bearings_cost = 10000.0
        nacelle.gearbox_cost = 10000.0
        nacelle.hss_cost = 10000.0
        nacelle.bedplate_cost = 10000.0
        nacelle.bedplateCost2002 = 8000.0
        nacelle.yaw_system_cost = 10000.0
        
        check_gradient_unit_test(self, nacelle, tol=1e-5)

#Turbine Components
class TestTurbineCostAdder(unittest.TestCase):

    def test1(self):

        turbine = TurbineCostAdder()

        turbine.offshore = True
        turbine.rotor_cost = 2000000.0
        turbine.nacelle_cost = 5000000.0
        turbine.tower_cost = 1000000.0

        check_gradient_unit_test(self, turbine)


# NREL CSM TCC Components
# ----------------------------------------------------------
# Tower Component
class Test_tower_csm_component(unittest.TestCase):

    def test1(self):

        tower = tower_csm_component()
    
        tower.rotor_diameter = 126.0
        tower.hub_height = 90.0
        tower.year = 2009
        tower.month = 12
        tower.advanced = False

        check_gradient_unit_test(self, tower)

#Rotor Components
class Test_blade_csm_component(unittest.TestCase):

    def test1(self):

        blades = blades_csm_component()
    
        blades.rotor_diameter = 126.0
        blades.advanced_blade = False
        blades.year = 2009
        blades.month = 12
        blades.advanced_blade = False

        check_gradient_unit_test(self, blades)

class Test_hub_csm_component(unittest.TestCase):

    def test1(self):

        hub = hub_csm_component()
    
        hub.blade_mass = 25614.377
        hub.rotor_diameter = 126.0
        hub.blade_number = 3
        hub.year = 2009
        hub.month = 12

        check_gradient_unit_test(self, hub)

# Nacelle Components
class Test_nacelle_csm_component(unittest.TestCase):

    def test1(self):

        nac = nacelle_csm_component()
    
        nac.rotor_diameter = 126.0
        nac.machine_rating = 5000.0
        nac.rotor_mass = 123193.30
        nac.rotor_thrust = 500930.1
        nac.rotor_torque = 4365249
        nac.drivetrain_design = 1
        nac.offshore = True
        nac.crane=True
        nac.advanced_bedplate=0
        nac.year = 2009
        nac.month = 12

        check_gradient_unit_test(self, nac, display=False)

#Turbine Components
class Test_rotor_mass_adder(unittest.TestCase):

    def test1(self):

        rotor = rotor_mass_adder()

        rotor.blade_mass = 17000.
        rotor.hub_system_mass = 35000.
        rotor.blade_number = 3

        check_gradient_unit_test(self, rotor)


#Turbine Components
class Test_tcc_csm_component(unittest.TestCase):

    def test1(self):

        trb = tcc_csm_component()

        trb.rotor_diameter = 126.0
        trb.advanced_blade = True
        trb.blade_number = 3
        trb.hub_height = 90.0    
        trb.machine_rating = 5000.0
        trb.offshore = True
        trb.year = 2009
        trb.month = 12

        check_gradient_unit_test(self, trb)

#----------------------------------------------------

if __name__ == "__main__":
    unittest.main()
    
