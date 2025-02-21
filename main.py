from i18n import lang, t
Ln = t[lang]

name = input(f"{Ln['name']}? ")
if name:
    print(f"{Ln['hello']} {name}.")
else:
    print(f"{Ln['hello']}, {Ln['world']}.")
