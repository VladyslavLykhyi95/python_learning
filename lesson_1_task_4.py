some_dict = {"title": "plov", "price": 1000, "ingridients": ["25 kartoshek", "vedro vodu", "ohapka drov"]}

some_dict["decription"] = "recipe"
print(some_dict)

some_dict["price"] = some_dict["price"] + 100
print(some_dict)

# some_dict["ingridients"] = some_dict["ingridients"].append("plov gotov")
# print(some_dict) #return None for ingridients

print(len(some_dict["ingridients"]))

some_dict.pop("decription")
print(some_dict)

