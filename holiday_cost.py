#This program calculates a user's total holiday cost

# This function calculates the hotel cost based on the number of nights
def hotel_cost(num_nights):
    #you can adjust the price per night based on your preference
    price_per_night=50
    accomodation_cost=num_nights*price_per_night
    return accomodation_cost

#Get user input
nights=int(input("How many nights will you stay at the hotel?:"))
#the result that the 'hotel_cost' function returns 
result_hotel_cost=hotel_cost(nights)
#print out hotel cost
print(f"Your hotel cost will be {result_hotel_cost}$.")

#This function called 'plane_cost'has one parameter, city_flight and calculate plane cost
def plane_cost(city_flight):
    #assign different prices based on the chosen city
    while True:
        
        if city_flight=="London":
            return 120
        elif city_flight=="Berlin":
            return 100
        elif city_flight=="Rome":
            return 110
        else:
            #invalid destination so get valid user input
            city_flight=input("Please input only Berlin, London or Rome:")
            city_flight=city_flight.capitalize()
    return ticket_price

#get user input
city=input("Where are you going for holiday? (Berlin, London, Rome):")
city=city.capitalize()

result_plane_cost=plane_cost(city)
#print out plane cost
print(f"Your plane cost will be {result_plane_cost}$.")

#This function called 'car_rental'has one parameter, rental_days and calculate rental cost
def car_rental(rental_days):
     #you can adjust the price per day based on your preference
    day_price=40
    rental_cost=rental_days*40
    return rental_cost

#get user input    
number_days=int(input("How many days will you hire a car?:"))
result_rental_cost=car_rental(number_days)  
#print out rental cost
print(f"Your rental cost will be {result_rental_cost}$.")

#This function called 'holiday_cost' has three parameters, hotel_cost, plane_cost and car rental.
def holiday_cost(hotel_cost,plane_cost,car_rental):
    #calculate total holiday cost
    total_holiday_cost=result_hotel_cost+result_plane_cost+result_rental_cost
    return total_holiday_cost
total_cost=holiday_cost(result_plane_cost,result_hotel_cost,result_rental_cost)
#print out holiday cost
print(f"Your total holiday cost will be {total_cost}$.")
     


    

    
        