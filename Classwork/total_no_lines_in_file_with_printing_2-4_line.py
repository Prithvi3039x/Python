filename = "C:/2_PYTHON/Classwork/sample.txt"

f = open(filename, 'r')
lines = f.readlines()
f.close()

print(f"Total lines: {len(lines)}")

if len(lines) >= 2:
    print(f"2nd line: {lines[1]}")

if len(lines) >= 4:
    print(f"4th line: {lines[3]}")