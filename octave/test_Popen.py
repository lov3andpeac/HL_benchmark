#!/usr/bin/python3

import os
import time
import subprocess

cmd = "sudo sysdig proc.name = sudo > out_test"
p = subprocess.Popen(cmd, shell=True)

p.terminate()
