import datetime

def dia_semana(data):
    diaSemana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
    return diaSemana[data.weekday()]

if __name__ == '__main__':
    dia_semana()
