#!/usr/bin/python3

import os
import time
import subprocess


LOOP = 1
CONNECTION = 1000
DURATION = 5
NRCPUS = os.cpu_count()
URL = "http://127.0.0.1/cgi-bin/hello.cgi"
cmd = "/home/jhl/桌面/benchmark/nginx/wrk_/wrk -t %d -c %d -d %d --timeout %d %s" % (NRCPUS, CONNECTION, DURATION, DURATION, URL)

def log_start():
	cmd = "sudo sysdig proc.name = sudo > out_test"
	p = subprocess.Popen(cmd, shell=True)
	return p


def log_end(p):
	p.terminate()
	

def prepare():
    subprocess.run("sudo /usr/sbin/apachectl -k start", shell=True)
    # time.sleep(1)


def execute_wrk():
    f = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)


def finish():
    subprocess.run("sudo /usr/sbin/apachectl -k stop", shell=True)
    # time.sleep(1)
    # subprocess.run("rm -f apache2/httpd_/logs/*", shell=True)

res = []
print(cmd)
try:
    for i in range(LOOP):
        prepare()
        execute_wrk()
        print("loop %d ..." % i, flush=True)
        finish()

except Exception as e:
    print(e)
