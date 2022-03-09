import sys

current_word = None
current_precio = []
word = None
precio = 0
total=0
for line in sys.stdin:
    city,year,price = line.split(":")
    if city == "STAMFORD" and year == "2015":
        current_precio.append(int(price))
current_precio.sort()
for i in current_precio:
    print ("{}\t{}\t{}".format("STAMFORD",i,"2015"))
