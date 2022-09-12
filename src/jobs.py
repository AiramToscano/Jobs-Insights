import csv
from functools import lru_cache


@lru_cache
def read(path):
    lista = []
    with open(path) as file:
        read = csv.DictReader(file)
        for row in read:
            lista.append(row)

    return lista
