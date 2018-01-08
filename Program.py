# Autorzy
# Jakub Kowalewski 155101
# Monika Ingielewicz 150323
# Opis działania poszczególnych funkcji został przedstawiony w pliku funkcje.py


from funkcje import *

# Przyporządkowanie obrazow kategorii: 0 - Nano, 1 - Paint
kategoria = (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)

mtx = generuj_macierze_intensywnosci("obrazy")

# dane, czyli jasność, wariancja i entropia
dane = generuj_dane(mtx)

# otrzymane dane, umieszczamy w obiekcie DataFrame korzystając biblioteki pandas
df = generuj_df(kategoria, dane)

# sprawdzenie działania klasyfikatora na zestawie obrazów testowych
print("Program zwróci kategorię obrazu testowego poprzez podanie liczby, im liczba jest bliższa 0, tym bardziej obraz"
      " kwalifikuje się do kategorii NANO, a im bliżej 1, tym pewniejsze jest, że obraz został wykonany w paincie")
uczenie_maszynowe(df, 'Ant_SEM.png')
uczenie_maszynowe(df, 'Butterfly_tongue.png')
uczenie_maszynowe(df, 'test_paint_1.png')
uczenie_maszynowe(df, 'test_paint_2.png')
