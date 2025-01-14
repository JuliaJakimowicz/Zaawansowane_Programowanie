from Magazine import utils

def utworz_zamowienie(cena, stawka_podatku):

    cena_calosciowa = cena + utils.oblicz_podatek(cena, stawka_podatku)
    return f"Cena całkowita zamówienia: {cena_calosciowa} PLN"
