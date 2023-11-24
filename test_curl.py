#!/usr/bin/python3

import os
import time
import subprocess

cmd = "curl 127.0.0.1/cgi-bin/hello.cgi"
LOOP = 10

def prepare():
	subprocess.run("sudo /usr/sbin/apachectl -k start", shell=True)
	

def work(LOOP):
	for i in range(LOOP):
		subprocess.run(cmd, shell=True)


def finish():
	subprocess.run("sudo /usr/sbin/apachectl -k stop", shell=True)
	

try:
	prepare()
	work(LOOP)
	finish()
	
except Exception as e:
    print(e)
