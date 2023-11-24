#!/usr/bin/python3

import os, signal
import time
import subprocess


LOOP = 1
CONNECTION = 10
DURATION = 30
NRCPUS = os.cpu_count()
URL = "http://127.0.0.1/cgi-bin/hello.cgi"
cmd = "./wrk -t %d -c %d -d %d --timeout %d %s" % (NRCPUS, CONNECTION, DURATION, DURATION, URL)

def record_syscall():
	subprocess.Popen("touch out_apache", shell=True)
	print(1)
	p = subprocess.Popen("sudo sysdig proc.name=apache2 and evt.type=clone > out_apache", shell=True)
	return p

def prepare():
    subprocess.run("sudo /usr/sbin/apachectl -k start", shell=True)
    # time.sleep(1)


def execute_wrk():
    f = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)


def finish(p):
    subprocess.run("sudo /usr/sbin/apachectl -k stop", shell=True)
    os.killpg(p.pid, signal.SIGUSR1)
    # time.sleep(1)
    # subprocess.run("rm -f apache2/httpd_/logs/*", shell=True)

res = []
print(cmd)
try:
    for i in range(LOOP):
        p = record_syscall()
        prepare()
        print("loop %d ..." % i, flush=True)
        execute_wrk()
        finish(p)

except Exception as e:
    print(e)
