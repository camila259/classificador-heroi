def calcular_saldo(vitorias, derrotas):
    return vitorias - derrotas
vitorias = 80
derrotas = 20

saldo = calcular_saldo(vitorias, derrotas)
if vitorias <= 10:
    nivel = "ferro"

elif vitorias <= 20:
    nivel = "bronze"

elif vitorias <= 50:
    nivel = "prata"

elif vitorias <= 80:
    nivel = "ouro"

elif vitorias <= 100:
    nivel = "diamante"

elif vitorias >= 101:
    nivel = "lendario"

else:
    nivel = "imortal"

print (f"O Heroi tem de saldo {saldo} e esta no nivel de {nivel}")
