# Dictionary of Countries and their Food Cuisines
Food = {
    "Italy": "Pasta, Pizza, Gelato",
    "Japan": "Sushi, Ramen, Tempura",
    "Mexico": "Tacos, Enchiladas, Guacamole",
    "India": "Curry, Biryani, Samosa",
}
x = Food["India"]
print("Food Cuisine of India:", x)
# Get Keys
keys = Food.keys()
Food["France"] = "Baguette, Croissant, Ratatouille"
print("Countries:", list(keys))
# Get Values
values = Food.values()
Food["Italy"] = "Pasta, Pizza, Gelato, Risotto"
print("Food Cuisines:", list(values))
# Get Items
items = Food.items()
Food["France"] = "Baguette, Croissant, Ratatouille, Pain au Chocolat"
print("Country-Cuisine Pairs:", list(items))
# Check if a Key Exists
if "Italy" in Food:
    print("Italy is present in the  dictionary.")
else: 
    print("Italy is not present in the dictionary.")
if "Spain" in Food:
    print("Spain is present in the dictionary.")
else: 
    print("Spain is not present in the dictionary.")

# Updating Dictonary
Food.update({"Spain": "Paella, Tapas, Churros"})
print("Updated Dictionary:", Food)

# Removing Items
Food.pop("Mexico")
print("After Removing Mexico:", Food)

Food.popitem()
print("After Removing Last Item:", Food)# Looping
for country, cuisine in Food.items():
    print(f"{country}: {cuisine}")
for country in Food.keys():
    print(country)
for cuisine in Food.values():
    print(cuisine)
# Copying a Dictionary
Food_copy = Food.copy()
print("Copied Dictionary:", Food_copy)
# Nesting Dictionaries (Example: America)
America = {
    "New York": "Bagel, Pizza",
    "Los Angeles": "In-N-Out Burger, Tacos",
    "Chicago": "Deep Dish Pizza, Hot Dogs"
}
Food["America"] = America
print("Dictionary with Nested Dictionaries:", Food)
#Clearing a Dictionary
Food.clear()
print("After Clearing the Dictionary:", Food)