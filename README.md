# octave-benchmark
run benchmark: 
```
phoronix-test-suite benchmark octave-benchmark
```
record syscall:
```
sudo sysdig proc.name=octave-cli and evt.type=execve > out
```

# apache2-cgi-benchmark
run benchmark:
```
sudo python3 test_apache2_cgi.py
```
record syscall:
```
sudo sysdig -s1000 proc.name=apache2 and evt.type=clone or proc.name=apache2 and evt.type=execve > out_apache
```
good result


Using curl command, will get good result:
syscall:
```
sudo sysdig proc.name=apache2 and evt.type=clone or proc.name=apache2 and evt.type=execve
```
benchmark:
```
sudo python3 test_curl.py
```


