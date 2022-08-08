import datetime

def existe(dia, mes, ano):
    diaSemana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
    try:
        data = datetime.datetime(ano, mes, dia)
        return diaSemana[data.weekday()] in diaSemana
    except Exception:
        return False

if __name__ == '__main__':
    existe()
