#Make 3 commits with descriptive messages
import random

#Places to visit
destinations =  ['Orlando', 'San Francisco', 'Las Vegas', 'Seattle', 'Minneapolis', 'New York City'] 

#Places to eat
restaurants = ['Carrabas', 'On The Border', 'Texas Roadhouse', 'Joes Crab Shack', 'PF Changs'] 

#Methods of transportation
trans_methods = ['Boat', 'Train', 'Car', 'Plane'] 

#Forms of entertainment
ent_forms = ['Dance Club', 'Comedy Bar', 'Playhouse Theater', 'Cinema', 'Escape Room'] 

#Randomly select item function
def select_item(list):
    random_item = random.choice(list)
    return random_item

place_selected = select_item(destinations)

def validate_answer(user_input):
    while user_input != "yes" and user_input != "no":
        print("You must enter yes or no")
        user_input = input()
    return user_input

#Opening to select destination
print ("Welcome to the Day Trip Generator. We hope to make your travel planning as easy as possible. Let's start with a location. How about " + place_selected + "? Does that sound like a good idea? type yes or no"  )
place_answer = input()

place_answer = validate_answer(place_answer)

while place_answer == "no":
    place_selected = select_item(destinations)
    print("We want to make sure you are satisfied. Let's try another place.")
    print("How about " + place_selected + " ?")
    place_answer = input()
    place_answer = validate_answer(place_answer)
    

#Randomly select restaurant
restaurant_selected = select_item (restaurants)

#Validate selected restaurant
if place_answer == "yes":
    print("Now that you have a destination, you can pick a restaurant. How does " + restaurant_selected + " sound?")
    rest_answer = input("Please type yes or no." )
    rest_answer = validate_answer(rest_answer)

    while rest_answer == "no":
        restaurant_selected = select_item(restaurants)
        print("Not what you're in the mood for. Let's try something else.")
        print("How about " + restaurant_selected + " ?")
        rest_answer = input()
        rest_answer = validate_answer(rest_answer)



#Randomly select transportation
transportation_selected = select_item(trans_methods)

#Validate selected transportation
if rest_answer == "yes":
    print("How do you prefer to get to your destination? Would a " + transportation_selected + " work?")
    trans_answer = input("Please type yes or no." )
    trans_answer = validate_answer(trans_answer)

    while trans_answer == "no":
        transportation_selected = select_item(trans_methods)
        print("Not what you had in mind?")
        print("How about a " + transportation_selected + " ?")
        trans_answer = input()
        trans_answer = validate_answer(trans_answer)



#Randomly select entertainment
entertainment_selected = select_item(ent_forms)

#Validate selected entertainment
if trans_answer == "yes":
    print("What type of entertainment are you looking for? Would a " + entertainment_selected + " be on your agenda?")
    ent_answer = input("Please type yes or no." )
    ent_answer = validate_answer(ent_answer)

    while ent_answer == "no":
        entertainment_selected = select_item(ent_forms)
        print("Not what you had in mind?")
        print("How about a " + entertainment_selected + " ?")
        ent_answer = input()
        ent_answer = validate_answer(ent_answer)

#Display completed trip
print("We are excited to book the following trip for you! Please confirm the following answers are correct")
print("Your destination is " + place_selected + ".")
print("Your restaurant selected is " + restaurant_selected + ".")
print("Your transporation selected is " + transportation_selected + ".")
print("Your entertainment selected will be a " + entertainment_selected + ".")

#Confirm day trip
print("Does your information look correct? Please type yes or no")
confirm_trip = input()
while confirm_trip != "yes" and confirm_trip != "no":
        print("You must enter yes or no")
        confirm_trip = input()
while confirm_trip == "no":
    print("We are sorry to hear that. Please start the process over.")
    confirm_trip = input("Please type yes or no." )
    while confirm_trip != "yes" and confirm_trip != "no":
        print("You must enter yes or no")
        confirm_trip = input()

#Preview that the day trip is complete
print(f'You will be visiting luxurious {place_selected} and enjoying fine dining at {restaurant_selected}. You will be travelling by {transportation_selected} and enjoying some fantastic entertainment at the local {entertainment_selected}! Enjoy!!')








#functions single responsibility





# print(trans_methods)

# print(ent_forms)
