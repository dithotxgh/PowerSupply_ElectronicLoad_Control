#!/usr/bin/python

import os
import visa
import sys
import time
sys.path.insert(0, './Electronic Loads')

"""
To add electronic load, simply add the object class python script for the electronic load into the
Electronic Loads subdirectory following the same structure of other files, then add the import
and constructor to this file as seen below
"""


import generic_scpi
import array3721a


class ELECTRONICLOAD:
    def __init__(self):
        # find all devices defined
        self.files = []
        for files in os.listdir():
            self.files.append(files)

        self.rm = visa.ResourceManager()
        self.idn = []
        self.threads = []
        # find all scpi devices
        self.device_count = 0
        for i in self.rm.list_resources():
            self.inst = self.rm.open_resource(i)
            self.inst.timeout = 100
            try:
                self.idn = self.inst.query("*IDN?")
                if(self.idn in self.files):
                    break
            except:
                pass

        self.inst.timeout = 500
        self.name = str(self.idn).split(',')[0] + str(self.idn).split(',')[1]
        self.com_port = "COM" + str(self.inst.interface_number)

        if(self.name == "ARRAY3721A"):
            self.electronicload = array3721a.ARRAY3721A(self.inst)
        else:
            self.electronicload = generic_scpi.GENERIC_SCPI(self.inst)
