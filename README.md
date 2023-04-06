# Python

def quebra_de_terceira_posiçao(row):
    x = row.split('/')

    if len(x) < 1:
        pass

    elif len(x) > 2:
        return x[2].split('www.')[1]
    else:
        return x[2]
