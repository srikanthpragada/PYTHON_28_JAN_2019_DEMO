import pickle
import json

class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"


t = Time(10,20,30)
print(t)

jstr = json.dumps(t.__dict__)
print(jstr)
# Create dict from json str
td = json.loads(jstr)
print(type(td), td)

f = open("time.dat",'wb')
pickle.dump(t,f)
f.close()

