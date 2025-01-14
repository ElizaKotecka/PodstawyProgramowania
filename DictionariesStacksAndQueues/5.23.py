import json

def display_exchange_rates(file):

    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    print("Date            Buying Rate     Selling Rate")
    print("============================================")
    
    for rate in data["rates"]:
        date = rate["effectiveDate"]
        buy_rate = rate["bid"]
        sell_rate = rate["ask"]
        print(f"{date:<16}{buy_rate:<16.4f}{sell_rate:.4f}")

if __name__ == '__main__':
    #https://api.nbp.pl/api/exchangerates/rates/C/EUR/last/10/?format=json
    display_exchange_rates("euro.json")


