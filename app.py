from flask import Flask
import re
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
  images = []
  names = []
  discounts = []
  prices = []
  prices1 = []
  categories = []
  stocks = []
  main = []
  f = open("db.json")
  data = json.load(f)
  for property in data["Products"]:
    images.append(property["image_url"])
    names.append(property["name"])
    discounts.append(property["discount"])
    prices.append(property["price"])
    prices1.append(property["price1"])
    categories.append(property["category"])
    stocks.append(property["Stock"])
    main.append(images)
    main.append(names)
    main.append(discounts)
    main.append(prices)
    main.append(prices1)
    main.append(categories)
    main.append(stocks)
  return main

if __name__ == "__main__":
    app.run(debug=True)
