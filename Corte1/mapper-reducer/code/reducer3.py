import sys

current_word=None
current_count=500000000
word=None
total=0

for line in sys.stdin:
        word,count=line.split(":")
        total=int(count)
        if current_word==word:
                if total<current_count:
                        current_count=total
        else:
                if current_word:
                        print('%s\t\t\t%s'%(current_word,current_count))
                current_count=total
                current_word=word
if current_word == word:
        print('%s\t\t\t%s'%(current_word,current_count))
