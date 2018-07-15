valores = ['Jose', 'Maria', 'Joao', 'Aysla', 'Dani', 'Eu', 'Beto', 'Valdir', 'Ana', 'Adriana', 'Carlos', 'Mariana', 'Andressa', 'Djalma', 'Alice', 'Anita', 'Juliana', 'Gabriel']
countGrupo = 1
grupos = {}
tamanhoGrupo = 5
print(len(valores) % tamanhoGrupo)
tamTotal = len(valores) / tamanhoGrupo
for x in range(0, tamTotal):
    pos = 0
    contador = 0
    grupo = []
    while(contador < tamanhoGrupo):
        try:               
            grupo.append(valores[pos])
            del valores[pos]
        except IndexError:
            break
        contador += 1
        pos = 0 if pos == -1 else -1
    nome = 'Grupo ' + str(countGrupo)
    grupos[nome] = grupo
    countGrupo += 1
    maiorGrupo = len(grupos)
print(grupos)
if(len(valores) > 0):
    if(len(valores) == tamanhoGrupo):
        grupos['Grupo ' + str(countGrupo)] = valores
    else:            
        for valor in valores:
            try:
                grupos['Grupo ' + str(countGrupo)].append(valor)
            except KeyError:
                grupos['Grupo ' + str(maiorGrupo)].append(valor)
                countGrupo -= 1
            countGrupo = countGrupo - 1 if countGrupo > 0 else maiorGrupo
print(grupos)
        