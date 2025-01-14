from Magazine import utils


def cena_z_podatkiem(cena, stawka_podatku):

    return cena + utils.oblicz_podatek(cena, stawka_podatku)
