from data import data

splited_data = data.split("\n")
reportes_seguro = 0

for reporte in splited_data:
    if reporte.strip():
        reporte_dividido = list(map(int, reporte.split()))
        es_valido = True
        desc = False
        indice = 0
        if reporte_dividido[0] > reporte_dividido[1]:
            desc = True
        while es_valido and indice < len(reporte_dividido) - 1:
            diferencia = abs(reporte_dividido[indice] - reporte_dividido[indice + 1])
            if diferencia < 1 or diferencia > 3:
                es_valido = False
            if desc and reporte_dividido[indice] < reporte_dividido[indice + 1]:
                es_valido = False
            if not desc and reporte_dividido[indice] > reporte_dividido[indice + 1]:
                es_valido = False
            indice += 1
        if es_valido:
            reportes_seguro += 1

print(f"Número de reportes seguros: {reportes_seguro}")



def es_seguro(reporte):
    es_valido = True
    desc = False
    indice = 0
    if reporte[0] > reporte[1]:
        desc = True
    while es_valido and indice < len(reporte) - 1:
        diferencia = abs(reporte[indice] - reporte[indice + 1])
        if diferencia < 1 or diferencia > 3:
            es_valido = False
        if desc and reporte[indice] < reporte[indice + 1]:
            es_valido = False
        if not desc and reporte[indice] > reporte[indice + 1]:
            es_valido = False
        indice += 1
    return es_valido

def es_seguro_con_dampener(reporte):
    if es_seguro(reporte):
        return True
    for i in range(len(reporte)):
        nuevo_reporte = reporte[:i] + reporte[i+1:]
        if es_seguro(nuevo_reporte):
            return True
    return False

splited_data = data.split("\n")
reportes_seguro = 0

for reporte in splited_data:
    if reporte.strip():
        reporte_dividido = list(map(int, reporte.split()))
        if es_seguro_con_dampener(reporte_dividido):
            reportes_seguro += 1

print(f"Número de reportes seguros: {reportes_seguro}")


