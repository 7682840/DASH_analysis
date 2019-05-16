import matplotlib
import matplotlib.pyplot as plt
import re

# Capture file
fileToOpen = 'capture.csv'

lineVals = []
timeVals = []
repVals = []
repRate = ''

# Open file and get time and representation rate
with open(fileToOpen) as f:
    for idx, line in enumerate(f):
        lineVals = line.strip().split(",")

        if lineVals[0].startswith('#'):
            continue

        timeVals.append(float(lineVals[1].replace('"','')))

        repRate = lineVals[6].split('/')[1]
        repRate = repRate.replace('bunny_','').replace('bps','')
        repVals.append(float(repRate))

# Tile and Labels
plt.title('DASH Representation Rate over Time - provided capture')
plt.xlabel('Time (secs)')
plt.ylabel('Representation Rate (kbps)')

# Plot vals
plt.plot(timeVals, repVals, '.-')
plt.grid()
plt.show()
