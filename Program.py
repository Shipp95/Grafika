# Autorzy
# Jakub Kowalewski 155101
# Monika Ingielewicz 150323


from funkcje import *



kategoria = ('NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO',
             'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT')

mtx = generuj_macierze_intensywnosci("obrazy")

dane = generuj_dane(mtx)

df = generuj_df(kategoria, dane)

print(df.to_string(index=False))
