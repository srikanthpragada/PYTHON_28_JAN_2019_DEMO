names = ['Java', 'Python', 'C#', 'TypeScript', 'Sql','c']


def get_length(n):
    return len(n)


for n in sorted(names, key=lambda v : len(v)):
    print(n)

for n in sorted(names, key=len):
    print(n)



# for n in sorted(names):
#     print(n)
