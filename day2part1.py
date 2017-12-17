fileName = 'input.txt'
result = 0

f = open(fileName)
f.seek(0)
for line in f:
    line = [int(i) for i in line.split()]
    result += (max(line) - min(line))
print result
