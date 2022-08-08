from z3 import Int, Solver, Distinct
def sudoku_geral(estado):
    s = Solver()
    vars = [[Int(f'x{i}{j}') for j in range(len(estado))]
                for i in range(len(estado))]
    for i in range(len(estado)):
        s.add(Distinct(*vars[i]))
        s.add(Distinct(*[vars[j][i] for j in range(len(estado))]))
    for i in range(0, len(estado), 3):
        for j in range(0, len(estado), 3):
            s.add(Distinct(*sum([[vars[ii][jj] for jj in range(j, j+3)]
                                    for ii in range(i, i+3)], [])))

    for i in range(len(estado)):
        for j in range(len(estado)):
            if 1 <= estado[i][j] <= len(estado):
                s.add(vars[i][j] == estado[i][j])
            else:
                s.add(vars[i][j] >= 1)
                s.add(vars[i][j] <= len(estado))
    s.check()
    m = s.model()
    return [[m[vars[i][j]] for j in range(len(estado))]
                for i in range(len(estado))]



if __name__ == '__main__':
    sudoku_geral()
