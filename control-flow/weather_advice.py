#asks for weather
weather = input("What's is the whether like today? (sunny/rainy/cloudy): ")
#Cloth recommendation
if weather =="sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif weather == "cloudy":
    print("Make sure to wear a warm coat and scarf.")
else:
    print("don't have recommendations for this weather.")

