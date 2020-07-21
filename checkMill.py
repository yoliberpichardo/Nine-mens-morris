matriz = [[ [' '],'-----','-----',[' '],'-----','-----',[' '] ],#0m

        ['  |  ', [' '],'-----', [' '],'-----',[' '],'  | '],#1m

        ['  |    ','|  ',[' '],[' '],[' '],'  |  ','  |   '],#f--4

        [[' '],[' '],[' '], '     ',[' '],[' '],[' ']],#f--4

        ['  |    ','|  ',[' '],[' '],[' '],'  |   ',' |   '],#f--4

        ['  |  ', [' '],'-----', [' '],'-----',[' '],'  | '],#5m

        [[' '], '-----', '-----', [' '], '-----', '-----', [' ']]]#6m


def ranget(a, b, x, y):
    if y + 4 > a:
        return False
    elif  y + 3 > a:
        return False
    elif y - 3 < 0:
        return False
    else:
        return True



def Matriz(matriz):
    for x in range(7):
        for y in range(7):
            if matriz[x][y] == ['0'] and ranget(7, 7, x, y):
                if matriz[x][y] == ['0'] and matriz[x][y+3] == ['0']:#0m, 6m
                    if matriz[x][y-3] == ['0']:
                        print('logrado', end=' ')

                if matriz[x][y] == ['0'] and matriz[x][y+2] == ['0']:#1m, 5m
                    if matriz[x][y-2] == ['0']:
                        print('logrado', end=' ')

                if matriz[x][y] == ['0'] and matriz[x][y+1] == ['0']:#f -- 4
                    if matriz[x][y-1] == ['0']:
                        print('logrado', end=' ')


            else:
                print('no', end = ' ')




  

Matriz(matriz)










