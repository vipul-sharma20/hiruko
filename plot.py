from datetime import datetime

import matplotlib.pyplot as plt


colors = {
            'ENTRY': 'yellow',
            'ACQUIRE': 'green',
            'RELEASE': 'red',
            'REQUEST': 'black'
        }

data_file = open('/Users/vipul/cpython/history3.6.txt', 'r')
data = data_file.readlines()

data_dict = {}
date_sanitize = lambda date: float(datetime.fromtimestamp(
                                            float(date)).strftime('%S.%f'))

for i in range(len(data)-1):
    thread, event, tstamp = data[i].rstrip().split()
    next_tstamp = date_sanitize(data[i+1].rstrip().split()[2])
    tstamp = date_sanitize(tstamp)
    try:
        data_dict[thread]['points'].append((tstamp, next_tstamp))
        data_dict[thread]['colors'].append(colors[event])
    except KeyError:
        data_dict[thread] = dict(points=[], colors=[])

fig, ax = plt.subplots()
for idx, thread in enumerate(data_dict):
    ax.broken_barh(data_dict[thread]['points'], ((idx+1)*10, 9),
                   facecolors=data_dict[thread]['colors'])

ax.set_ylim(5, 55)
ax.set_xlim(54, 60)

ax.set_xlabel('seconds since start')
ax.set_yticks([15, 0.1])
ax.set_yticklabels(list(data_dict.keys()))
ax.grid(True)

plt.show()
