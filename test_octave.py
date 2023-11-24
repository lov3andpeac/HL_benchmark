#!/usr/bin/python3

import os
import time
import subprocess

cmd = "phoronix-test-suite benchmark octave-benchmark"
try:
	p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.stdin.write(b'n')
	p.stdin.flush()

except Exception as e:
    print(e)
    
out, _ = p.communicate()
print('output: ', out.decode())
