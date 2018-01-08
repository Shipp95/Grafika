import math
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from sklearn.linear_model import LinearRegression


# funkcja przechodzi do folderu podanego jako parametr, następnie w pętli, pliki z rozszerzeniem .png zostają wczytane do
# macierzy w trybie "L", to znaczy 8-bitowej skali szarości(wartość piksela = 0-255). Funkcja zwraca listę takich macierzy
# intensywności. Na koniec funkcja wraca do folderu roboczego, print() daje użytkownikowi znać do którego folderu przeszedł

def generuj_macierze_intensywnosci(param):
    i = 0
    mtx = list()
    curdir = os.getcwd()
    os.chdir(curdir + "/" + param)
    print(os.getcwd())
    for file in os.listdir('.'):
        if file.endswith(".png"):
            i += 1
            img = Image.open(file).convert("L")
            arr = np.asarray(img)
            mtx.append(arr)
    os.chdir(curdir)
    print(os.getcwd())
    return mtx


# funkcja pomocnicza, która tworzy pętlę pobierając wymiary obrazu i zliczając wartości każdego piksela. Funkcja zwraca
# tę sumę

def suma(photo):
    width_x = photo.shape[0]
    height_y = photo.shape[1]
    s = 0
    for x in range(width_x):
        for y in range(height_y):
            s = s + photo[x, y]
    return s;


# funkcja licząca jasność obrazu

def brigthness(photo):
    width_x = photo.shape[0]
    height_y = photo.shape[1]
    NM = 1 / (width_x * height_y)
    b = NM * suma(photo)
    return b;


# funkcja licząca wariancję

def variance(photo):
    "funkcja licząca wariancję obrazu"
    width_x = photo.shape[0]
    height_y = photo.shape[1]
    NM = 1 / (width_x * height_y)
    b = brigthness(photo)
    v = 0
    s = 0
    for x in range(width_x):
        for y in range(height_y):
            s = s + (photo[x, y] - b) ** 2
    v = NM * s
    return v;


# funkcja licząca entropię. Wykorzystuje utworzony na podstawie obrazu histogram, i pobiera ilość pikseli o danej
# intensywności do pętli.

def entropy(photo):
    wynik = 0
    n, bins, patches = plt.hist(photo.ravel(), bins=256, normed=1, range=(0.0, 255.0), fc='k', ec='k')
    for value in n:
        if value != 0.0:
            wynik -= (value * math.log2(value))
    return wynik


# funkcja, która pobiera listę macierzy intensywności i wylicza dla każdego elementu jasność, wariancję i entropię

def generuj_dane(lista):
    dane = list()
    for index, value in enumerate(lista):
        jas = brigthness(value)
        war = variance(value)
        ent = entropy(value)
        tup = (index, jas, war, ent)
        dane.append(tup)
    return dane


# funkcja, pobiera dwa argumenty, kat, oraz lista. Parametr kat, przyporządkowuje każdemu obrazowi kategorię 0 lub 1
# (NANO lub PAINT). Parametr lista, jest listą wygenerowaną przez poprzednią funkcję.

def generuj_df(kat, lista):
    df = pd.DataFrame({'Obraz': [x[0] + 1 for x in lista],
                       'Kategoria': pd.Categorical(kat),
                       'Jasnosc': [x[1] for x in lista],
                       'Wariancja': [x[2] for x in lista],
                       'Entropia': [x[3] for x in lista]})
    return df


# Funkcja uczenie_maszynowe, przyjmuje 2 argumenty: df oraz obraz. df jest obiektem DataFrame utworzonym za pomocą
# biblioteki pandas, i na podstawie tego obiektu tworzymy model regresji liniowej. Drugi argument 'obraz' jest to obraz,
# któremu chcemy przyporządkować kategorię na bazie naszego modelu. Otwieramy go w trybie "L", czyli 8-bitowej skali szarości
# a następnie tworzymy obiekt DataFrame, z parametrami takimi jak jasność, wariancja oraz entropia. Funkcja następnie porównuje
# taki obiekt do modelu regresji liniowej i informuje nas do której kategorii należy, oraz jakie jest odchylenie od wzorca.
# Wartości bliskie 0, oznaczają, że obraz prawdopodobnie został wykonany za pomocą mikroskopu, a wartości bliskie 1,
# informują nas, że obraz został wykonany w paincie.

def uczenie_maszynowe(df, obraz):
    lr = LinearRegression()
    lr.fit(df[['Jasnosc', 'Wariancja', 'Entropia']], df['Kategoria'])
    test = Image.open(obraz).convert("L")
    matrix = np.asarray(test)
    test = pd.DataFrame([[brigthness(matrix), variance(matrix), entropy(matrix)]], columns=list('ABC'))
    wynik = ((lr.predict(test[['A', 'B', 'C']])))
    if wynik >= 0.5:
        print('Obraz', obraz, 'jest obrazkiem zrobionym w paincie. Odchylenie od wzorca', abs(float(wynik)))
    else:
        print('Obraz', obraz, 'jest zdjęciem zrobionym zrobionym za pomocą mikroskopu. Odchylenie od wzorca',
              abs(float(wynik)))
