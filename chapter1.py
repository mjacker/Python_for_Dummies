import menu as mn
def _1():
    mn.square("Integers:")
    print("""
    Any valid number that does not contain a decimal point.
    For example:""")
    example = """
a = 123
b = 321
print(a + b)"""
    print(example)
    mn.square("output")
    exec(example)

    ### ════ ###
    mn.line()
    input("Press any key to continue...")
    ### ════ ###
    mn.square("Floats: ")
    print("""
    Any valid number that does contain a decimal point.
    
    For example:""")
    example = """
a = 1.2
b = 2.3
print(a + b)"""
    print(example)
    mn.square("output")
    exec(example)
