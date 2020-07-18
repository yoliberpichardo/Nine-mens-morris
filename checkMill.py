matriz = [[ [' '],'-----','-----',[' '],'-----','-----',[' '] ],#0m

        ['  |  ', [' '],'-----', [' '],'-----',[' '],'  | '],#1m

        ['  |    ','|  ',[' '],[' '],[' '],'  |  ','  |   '],#f--4

        [[' '],[' '],[' '], '     ',[' '],[' '],[' ']],#f--4

        ['  |    ','|  ',[' '],[' '],[' '],'  |   ',' |   '],#f--4

        ['  |  ', [' '],'-----', [' '],'-----',[' '],'  | '],#5m

        [[' '], '-----', '-----', [' '], '-----', '-----', [' ']]]#6m


def ranget(x, y, a, b):
    if b + 2 > y:
        return False
    else:
        return True

def Mill_matriz(matriz):
    for x in range(7):
        for y in range(7):
            if matriz[x][y] and ranget(7, 7, x, y):
                if matriz[x][y] == ['0'] and matriz[x][y+1] == ['0']:#f--4
                    if matriz[x][y-1] == ['0']:
                        return True

    if matriz[0][0] == ['0'] and matriz[0][0+3] == ['0']:#fila 0m
        if matriz[0][3+3] == ['0']:
            return True

    if matriz[1][1] == ['0'] and matriz[1][1+2] == ['0']:#fila 1m
        if matriz[1][3+2] == ['0']:
            return True
    
    if matriz[5][1] == ['0'] and matriz[5][1+2] == ['0']:#5m
        if matriz[5][3+2] == ['0']:
            return True

    if matriz[6][0] == ['0'] and matriz[6][0+3] == ['0']:#6m
        if matriz[6][3+3] == ['0']:
            print('logrado', end=' ')

    else:
        return False

print(Mill_matriz(matriz))










