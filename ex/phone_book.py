# Phone book ver 1.0
pb = {}

while True:
    name = input("Enter name : ")
    if name == 'end':
        break

    phone = input("Enter phone number :")
    pb[name] = phone

for (n,p) in sorted(pb.items()):
    print( f"{n:20s} {p}")

