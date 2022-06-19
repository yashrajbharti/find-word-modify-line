
import fileinput
import sys

text = "DATE"   # if any line contains this text, I want to modify the whole line.

x = fileinput.input(files="/Users/yashraj/Desktop/python/Located_Events.txt", inplace=1)
for line in x:
    if text in line:
        new_text = "<TimeSpan><begin>" + [ t for t in line.split() if t.startswith('2021-') ][0] + "</begin></TimeSpan>"
        line += new_text
    sys.stdout.write(line)
x.close()