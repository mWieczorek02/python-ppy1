import json

if __name__ == "__main__":
    stocks = {"PLW": 360.0, "TEN": 320.0, "CDR": 329.0}
    json_obj = json.dumps(stocks, indent=4, sort_keys=True)

    print(json_obj)
