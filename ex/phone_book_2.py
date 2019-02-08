# Phone book ver 2.0
pb = {}
while True:
    name = input("Enter name : ")
    if name == 'end':
        break

    phone = input("Enter phone number :")
    if name in pb:
        pb[name].add(phone)  # Add phone to existing set
    else:
        pb[name] = {phone}  # Place name and a set

for (n, p) in sorted(pb.items()):
    print(f"{n:20s} {','.join(p)}")
