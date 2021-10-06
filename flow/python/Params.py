##
# @file Params.py
# @author Keren Zhu
# @date 06/27/2019
# @brief The parameters of the flow
#

import json
import math

class Params:
    """
    @brief Parameter class
    """
    def __init__(self):
        """
        @brief initialization
        """
        self.spectre_netlist = None # Input spectre netlist file
        self.hspice_netlist = None # Input hspice netlist file
        self.simple_tech_file = "" # Input simple tech file
        self.techfile = ""
        self.lef = ""
        self.vddNetNames = ["VDD", "vdd", "vdda", "vddd"]
        self.vssNetNames = ["VSS", "GND", "vss", "gnd", "vssa", "vssd"]
        self.digitalNetNames = ["clk"]
        self.stdCells = []
        self.resultDir = None
        self.powerLayer = 4 # m6
        self.psubLayer = self.powerLayer # same as power pin
        self.smallModuleAreaThreshold = 600 # um^2
        # [um in length, um in width]
        self.signalAnalogWireWidthTable = \
        [ [0, 0.33],  [120, 0.66]]
        self.signalDigitalWireWidthTable = \
        [ [0, 0.33],  [100, 0.66]]
        self.powerWireWidthTable = \
        [[0, 0.33]]
        self.dpowerWireWidthTable = \
        [[0, 0.33]]
        # via  [um in length, # of cuts, # of rols, # of cols]
        self.signalAnalogViaCutsTable = \
        [[0, 2, 1, 2], [80, 4, 2, 2], [120, 9, 3, 3]]
        self.signalDigitalViaCutsTable = \
        [[0, 2, 1, 2], [120, 4, 2, 2]]
        self.powerViaCutsTable = \
        [[0, 4, 2, 2], [100, 9, 3, 3]]
        # Additional spacing
        # increase module spacing by area [um^2, um]
        self.blockSpacingFromAreaTableX = \
        [[0.0, 0.66], [100, 2.64]]
        self.blockSpacingFromAreaTableY = \
        [[0.0, 0.66], [100, 1.32]]

    def printWelcome(self):
        """
        @brief print welcome message
        """
        content = """\
========================================================
    MAGICAL: Machine Generated Analog IC Layout            
        https://github.com/magical-eda/MAGICAL
========================================================"""
        print(content)

    def printHelp(self):
        """
        @brief print help message for JSON parameters
        """
        content = """\
                    JSON Parameters
========================================================
spectre_netlist [required for spectre netlist]    | input .sp file 
hspice_netlist [required for hspice netlist]    | input .sp file 
simple_tech_file [required]    | input simple techfile 
        """ % (self.spectre_netlist,
                self.hspice_netlist,
                self.simple_tech_file
                )
        print(content)


    def toJson(self):
        """
        @brief convert to json  
        """
        data = dict()
        data['spectre_netlist'] = self.spectre_netlist
        data['hspice_netlist'] = self.hspice_netlist
        data['simple_tech_file'] = self.simple_tech_file
        data['resultDir'] = self.resultDir
        return data 

    def fromJson(self, data):
        """
        @brief load form json 
        """
        if 'spectre_netlist' in data: self.spectre_netlist = data['spectre_netlist']
        if 'hspice_netlist' in data: self.hspice_netlist = data['hspice_netlist']
        if 'simple_tech_file' in data: self.simple_tech_file = data['simple_tech_file']
        if 'resultDir' in data: self.resultDir = data['resultDir']
        if 'lef' in data : self.lef = data['lef']
        if 'techfile' in data : self.techfile = data['techfile']
        if 'vddNetNames' in data : self.vddNetNames = data['vddNetNames']
        if 'vssNetNames' in data : self.vssNetNames = data['vssNetNames']

    def dump(self, filename):
        """
        @brief dump to json file 
        """
        with open(filename, 'w') as f:
            json.dump(self.toJson(), f)

    def load(self, filename):
        """
        @brief load from json file 
        """
        with open(filename, 'r') as f:
            self.fromJson(json.load(f))

    def __str__(self):
        """
        @brief string 
        """
        return str(self.toJson())

    def __repr__(self):
        """
        @brief print 
        """
        return self.__str__()
