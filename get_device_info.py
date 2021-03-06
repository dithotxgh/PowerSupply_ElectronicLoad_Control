#!/usr/bin/python
"""
written by Jake Pring from CircuitSpecialists.com
licensed as GPLv3
"""

import os
import visa
import serial
import serial.tools.list_ports
import sys
import time
import ElectronicLoads as electronicload
import PowerSupplies as powersupply


class SCPI_ID:
    def __init__(self):
        device_type = 'electronicload'
        if(device_type == 'electronicload'):
            # find all devices defined
            self.files = []
            self.rm = visa.ResourceManager()
            self.threads = []
            # find all scpi devices
            self.device_count = 0
            for i in self.rm.list_resources():
                self.inst = self.rm.open_resource(i)
                self.inst.timeout = 100
                try:
                    self.idn = self.inst.query("*IDN?")
                    break
                except:
                    pass

            self.inst.timeout = 500
            print(self.inst.query("*IDN?"))
            print(self.idn)
            print()
            print(str(self.idn).split(',')[0] + str(self.idn).split(',')[1])
        else:
            com_ports = list(serial.tools.list_ports.comports())
            for p in com_ports:
                print(str(p.hwid))
        sys.exit()


if __name__ == "__main__":
    test = SCPI_ID()