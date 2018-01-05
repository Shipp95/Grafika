import math
import numpy as np
import os

import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image


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


def suma(photo):
    "funkcja sumujace elementy macierzy (obrazu)"

    width_x = photo.shape[0]
    height_y = photo.shape[1]
    s = 0
    for x in range(width_x):
        for y in range(height_y):
            s = s + photo[x, y]
    return s;


def brigthness(photo: object) -> object:
    "funkcja licząca jasność dla obrazu"
    width_x = photo.shape[0]
    height_y = photo.shape[1]
    NM = 1 / (width_x * height_y)
    b = NM * suma(photo)
    return b;


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


def entropy(photo):
    wynik = 0
    n, bins, patches = plt.hist(photo.ravel(), bins=256, normed=1, range=(0.0, 255.0), fc='k', ec='k')
    for value in n:
        if value != 0.0:
            wynik -= (value * math.log2(value))
    return wynik


def generuj_dane(lista):
    dane = list()
    for index, value in enumerate(lista):
        jas = brigthness(value)
        war = variance(value)
        ent = entropy(value)
        tup = (index, jas, war, ent)
        dane.append(tup)
    return dane


def generuj_df(kat, lista):
    df = pd.DataFrame({'1. Obraz': [x[0] + 1 for x in lista],
                       '2. Kategoria': pd.Categorical(kat),
                       '3. Jasnosc': [x[1] for x in lista],
                       '4. Wariancja': [x[2] for x in lista],
                       '5. Entropia': [x[3] for x in lista]})
    return df
