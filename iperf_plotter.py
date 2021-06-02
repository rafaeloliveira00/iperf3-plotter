import matplotlib.pyplot as plt
import datetime
import json
import sys
import os

if len(sys.argv) <= 1:
    print('Missing file name argument\nUsage: python3 iperf_plotter.py file.json')
    sys.exit(0)

input_file_name = sys.argv[1]
output_file_name = os.path.splitext(input_file_name)[0]

with open(input_file_name) as json_file:
    json_data = json.load(json_file)

time_intervals = json_data['intervals']
time_intervals_sum = [item['sum'] for item in time_intervals]

date = json_data['start']['timestamp']['timesecs']
date = datetime.datetime.fromtimestamp(date)

start_time = [int(item['start']) for item in time_intervals_sum]
end_time = [int(item['end']) for item in time_intervals_sum]
total_bytes = [item['bytes'] / 1000000 for item in time_intervals_sum]
bits_per_second = [item['bits_per_second'] / 1000000 for item in time_intervals_sum]

plt.figure(1)
plt.title('Throughput')
plt.subplots_adjust(bottom=0.2)
plt.plot(end_time, bits_per_second)
plt.xlabel(f"Time (s)\n\n{date.strftime('%d-%m-%y %H:%M')}")
plt.ylabel('Mbits/s')
plt.savefig(f'{output_file_name}_throughput.png')

plt.figure(2)
plt.title('Total megabytes transferred')
plt.subplots_adjust(bottom=0.2)
plt.plot(end_time, total_bytes)
plt.xlabel(f"Time (s)\n\n{date.strftime('%d-%m-%y %H:%M')}")
plt.ylabel('Megabytes')
plt.savefig(f'{output_file_name}_total_bytes.png')

print('Completed.')
