import sys

header = sys.stdin.readline()

for line in sys.stdin:
    words=line.split(",")
    price, city = words[1], words[6].strip()
    date = words[2].split('-')
    print("{}:{}:{}".format(city, date[0], price))
