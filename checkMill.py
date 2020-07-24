
def ranget(a, b, x, y):
    if y + 4 > a:
        return False
    elif y - 3 < 0:
        return False
    else:
        return True
                #------------------------FOR ROWS--------------------------------------------#
def checMill_rows(matriz):
    for x in range(7):
        for y in range(7):
            if matriz[x][y] == ['0'] and ranget(7, 7, x, y):
                if matriz[x][y] and matriz[x][y+3] == ['0']:
                    if matriz[x][y-3] == ['0']:
                        return True

                if matriz[x][y] and matriz[x][y+2] == ['0']:
                    if matriz[x][y-2] == ['0']:
                        return True

                if matriz[x][y] and matriz[x][y+1] == ['0']:
                    if matriz[x][y-1] == ['0']:
                        return True
                
            if matriz[3][0] == ['0'] and matriz[3][0+1] == ['0']:
                if matriz[3][1+1] == ['0']:
                    return True

            if matriz[3][4] == ['0'] and matriz[3][4+1] == ['0']:
                if matriz[3][5 + 1] == ['0']:
                    return True

print(checMill_rows(matriz))


            #----------------------------FOR COLUMNS--------------------------------------#
def checMill_colums(matriz):
    for x in range(7):
        for y in range(7):
            if y != 3:
                if x + 3 < len(matriz):
                    if matriz[x][y] == ['0'] and matriz[x+3][y] == ['0']:
                        if matriz[x-3][y] == ['0']:
                            return True

                    if matriz[x][y] == ['0'] and matriz[x+2][y] == ['0']:
                        if matriz[x-2][y] == ['0']:
                            return True

                    if matriz[x][y] == ['0'] and matriz[x+1][y] == ['0']:
                        if matriz[x-1][y] == ['0']:
                            return True

            if matriz[0][3] == ['0'] and matriz[1][3] == ['0']:
                if matriz[2][3] == ['0']:
                    return True

            if matriz[4][3] == ['0'] and matriz[5][3] == ['0']:
                if matriz[6][4-1] == ['0']:
                    return True
                    


print(checMill_colums(matriz))










