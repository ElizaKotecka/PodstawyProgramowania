transactions_in_eur = [15.90,38.47,4.07,132.70,9.15]
transactions_in_pln = list(map(lambda x:x*4.5, transactions_in_eur))

for elem in transactions_in_pln:
    print(round(elem, 2))
