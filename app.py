from flask import Flask
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def home():
  main = {}
  main["images"] = []
  main["names"] = []
  main["discounts"] = []
  main["prices"] = []
  main["prices1"] = []
  main["categories"] = []
  main["stocks"] = []
  f = open("db.json")
  data = json.load(f)
  for property in data["Products"]:
    main["images"].append(property["image_url"])
    main["names"].append(property["name"])
    main["discounts"].append(property["discount"])
    main["prices"].append(property["price"])
    main["prices1"].append(property["price1"])
    main["categories"].append(property["category"])
    main["stocks"].append(property["Stock"])
  return main

if __name__ == "__main__":
    app.run(debug=True)
