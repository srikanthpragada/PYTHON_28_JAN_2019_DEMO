import os

for (dn,dlist,flist) in os.walk(r"e:\classroom\python\jan28\demo"):
    if dn.find(".git") >= 0 or dn.find("__") >= 0 :
        continue

    print(dn)
    print("===========================")
    for f in flist:
        if f.endswith(".py"):
            print(f)



