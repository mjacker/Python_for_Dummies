def menugen(*args):
    output = 'Menu:\n\n'
    for index, arg in enumerate(args):
        output += f'{index + 1}.{arg}\n'
    return output

print(menugen('Frances', 'Italiano'))

def ingles():
    print('Ingles ejecutado')

def chino():
    print('Chino ejecutado')

def espanol():
    print('Español ejecutado')

def alienigena():
    print('Alienigena ejecutado')

# -----

print("""Menu:

1. Ingles
2. Chino
3. Español
4. Alienigena
""")

# -----

dialog = int(input('Seleccione una opción >> '))

menu = {True: lambda: None,
        dialog == 1: ingles,
        dialog == 2: chino,
        dialog == 3: espanol,
        dialog == 4: alienigena}

print(menu[True]())