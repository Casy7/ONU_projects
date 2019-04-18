import json
with open("purchases.json", "r") as file:
    data = json.load(file)
buyers = {}
for purchase in data:
    if purchase["buyer"] not in buyers:
        buyers[purchase["buyer"]] = purchase["price"]
    else:
        buyers[purchase["buyer"]] += purchase["price"]

summ = buyers.values()
max_sum = max(summ)
min_sum = min(summ)
sums = {}

for buyer in buyers:
    sums[buyers[buyer]] = buyer
most_buyer = sums.get(max_sum)
least_buyer = sums.get(min_sum)

res_to_out = [
    {
        "Title": "Most Buyer",
        "Name": most_buyer,
        "Sum": max_sum
    },
    {
        "Title": "Least Buyer",
        "Name": least_buyer,
        "Sum": min_sum
    }
]

# res_to_out = json.dumps(res_to_out, indent = 4)
with open("result.json", "w") as file:
    json.dump(res_to_out, file)
