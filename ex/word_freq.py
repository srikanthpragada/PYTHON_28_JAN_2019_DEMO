# Program to display frequency of each word

f = open("test.txt")

freq = {}
for line in f.readlines():
    words = line.split(" ")
    for w in words:
       w = w.strip("\n").strip(".")
       if w in freq:
           freq[w] = freq[w] + 1  # increment count
       else:
           freq[w] = 1   # insert new entry

for (w,c) in sorted(freq.items()):
    print(w,c)
