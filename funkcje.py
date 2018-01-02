import os, numpy
from PIL import Image

def generuj_macierze_intensywnosci(param):
    i = 0
    mtx = list()
    curdir=os.getcwd()
    os.chdir(curdir + "/" + param)
    print(os.getcwd())
    for file in os.listdir('.'):
        if file.endswith(".png"):
            i += 1
            img = Image.open(file)
            img = img.convert("L")
            px = img.load()
            mtx.append(px)
            result = open("{0}.txt".format(i),'w')
            width_x=img.size[0]
            height_y=img.size[1]
            for y in range(height_y):
                result.write("\n")
                for x in range(width_x):
                    result.write(str(px[x,y])+" ")
            result.close()
    os.chdir(curdir)
    print(os.getcwd())