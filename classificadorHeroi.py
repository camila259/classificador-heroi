nome = "Arthur"
xp = 7500

print(nome)
print(xp)

if xp < 1000:
    nivel = "ferro"

elif xp <= 2000:
    nivel = "bronze"

elif xp <= 5000:
    nivel = "prata"

elif xp <= 6000:
    nivel = "ouro"

elif xp <= 7000:
    nivel = "platina"

elif xp <= 8000:
    nivel = "ascendente"

elif xp <= 9000:
    nivel = "imortal"

elif xp <= 10000:
    nivel = "radiante"

print (f"O heroi de nome {nome} esta no nivel de {nivel}")