# iPerf3 plotter
Python script that plots iPerf3's JSON file

# Install
Matplot is required to run this script

```
pip install matplot
```

# Usage
Sample output is provided (sample.json) to plot it run:

```
python3 iperf_plotter.py sample.json
```

# Results
Two graphs will be generated, one with the throughput along the time, and other with the number of Megabytes sent.

## Throughput
![Throughput](results/sample_throughput.png)
log_throughput
## Total bytes
![Total bytes](results/sample_total_bytes.png)
