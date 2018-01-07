# Autorzy
# Jakub Kowalewski 155101
# Monika Ingielewicz 150323


from funkcje import *


kategoria = (0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0)
#kategoria = ('NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO', 'NANO',
#            'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT', 'PAINT')

mtx = generuj_macierze_intensywnosci("obrazy")

dane = generuj_dane(mtx)

df = generuj_df(kategoria, dane)


# print(df.to_string(index=False))
# df.to_csv(path_or_buf='wyniki.txt', sep='\t', index=False)
uczenie_maszynowe(df, 'Ant_SEM.png')
uczenie_maszynowe(df, 'Butterfly_tongue.png')
uczenie_maszynowe(df, 'test_paint_1.png')
uczenie_maszynowe(df, 'test_paint_2.png')