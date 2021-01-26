def variable_type(x):
    variable_type = type(x)
    print (f"Essa variável é do tipo {variable_type}")

def variable_len(x):
    try:
        variable_len = len(x)
        print(f"O tamanho dessa variável é {variable_len}")
    except TypeError as e:
        print(e)