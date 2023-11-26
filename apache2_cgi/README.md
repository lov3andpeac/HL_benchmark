# configure apache2 with mod_cgi
# configure wrk
```
unzip wrk.zip
mv wrk-master/ wrk_/
cd wrk_/
make
```

# benchmark
## using wrk
run benchmark:
```
sudo python3 test_apache2_cgi.py
```
record syscall:
```
sudo sysdig -s1000 proc.name=apache2 and evt.type=clone or proc.name=apache2 and evt.type=execve > out_apache
```
good result


## using curl command
syscall:
```
sudo sysdig proc.name=apache2 and evt.type=clone or proc.name=apache2 and evt.type=execve
```
benchmark:
```
sudo python3 test_curl.py
```
