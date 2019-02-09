def kw_only(*, n1, n2=2):  # Keyword only arguments
    pass


def print_details(v, **details):
    print(details)


kw_only(n1=10, n2=20)
kw_only(n1=10)

print_details(10, name='Abc', phone="3343434", email='abc@gmail.com')
