# install GNU-octave
```
sudo apt-get install octave
```

# prepare benchmark
```
tar -zxvf benchmark-1.1.1.tar.gz
mv benchmark-1.1.1 octave-benchmark
```

# benchmark
run benchmark: 
```
phoronix-test-suite benchmark octave-benchmark
```
record syscall:
```
sudo sysdig proc.name=octave-cli and evt.type=execve > out
```
