from Magazine import Product

if __name__ == "__main__":
    cena = 100.0
    stawka_podatku = 0.23

    cena_brutto = Product.cena_z_podatkiem(cena, stawka_podatku)

    print(f"Cena brutto produktu: {cena_brutto} PLN")
