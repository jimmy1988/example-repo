# Old JavaScript/PHP habit of mine, all functions at the top of the file, to keep the main program separate from functions

def hotel_cost(nights) -> float:
    """
    Calculate the hotel cost
    Args:
        nights (int): The number of nights a user will stay in a hotel:

    Returns:
    float: The hotel cost
    """

    nights = int(nights) # make sure the number of nights is an integer
    return float(nights *  120.00) # return the number of nights multiplied by the price, converted to a float


def plane_cost(city) -> float:

    """"
    Calculate the plane cost
    Args:
        city (str): The name of the city you are working with

    Returns:
        float: The plane cost
    """

    city = str(city).title() # make sure city is string and convert to title case

    # check the city to work out the price
    if city == "New York":
        price = 120.00

    elif city == "San Francisco":
        price = 95.00

    elif city == "San Jose":
        price = 200.00

    elif city == "Tokyo":
        price = 1000.00

    elif city == "Chicago":
        price = 300.00

    elif city == "London":
        price = 500.00

    else:
        price = 0

    # return the price and convert to float
    return float(price)


def car_rental(days) -> float:

    """
    Calculate the car rental cost
    Args:
        days (int): The number of days a user will stay in a car

    Returns:
        float: The car rental cost

    """

    days = int(days) # convert the rental days to int
    return float(days * 55.00) # out put the rental days multiplied by the price


def holiday_cost(city, car_rental_days, nights) -> dict[str, str | int | float]:

    """
    Calculate the holiday cost
    Args:
        city (str): The name of the city you are working with
        car_rental_days (int): The number of days a user will have a car
        nights (int): The number of nights a user will stay in a hotel

    Returns:
        dict: The holiday cost list
    """

    city = str(city).strip().title()

    hotel = hotel_cost(nights)
    plane = plane_cost(city)
    car = car_rental(car_rental_days)

    return dict(
        city=city,
        rental_days=rental_days,
        nights=nights,
        hotel_cost=hotel,
        plane_cost=plane,
        car_rental=car,
        holiday_total=sum([hotel, plane, car]),
    )



# Ask the user for the details
city_flight = input("What city will you be flying to? ") # City flying to
num_nights = int(input("How many nights will you be staying at the hotel? ")) # Nights in the hotel
rental_days = int(input("How many days will you be renting a car? ")) # days renting a car

# Get all the costs, including the total cost
cost = holiday_cost(city_flight, rental_days, num_nights)

# output all the costs
print(f"The city you will be flying to is {cost['city']}")
print(f"The hotel cost is £{round(float(cost['hotel_cost']), 2):.2f} ({cost['nights']} nights x £120.00)")
print(f"The plane cost is: £{round(float(cost['plane_cost']), 2):.2f}")
print(f"The car rental days is: £{round(float(cost['car_rental']), 2):.2f} ({cost['rental_days']} x £55.00)")
print(f"The total cost of the holiday is: £{round(float(cost['holiday_total']), 2):.2f}")

