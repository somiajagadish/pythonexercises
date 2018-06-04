def trip_cost(city, days):
  return rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city)

def rental_car_cost(days):
  return days*40

def hotel_cost(days):
  return 140*days

def plane_ride_cost(city):
  if city == "L.A":
  	return 300
	
		
def plane_ride_cost(city):
  if city == "Charlotte":
  	return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
	
	
def hotel_cost(nights):
	return 140 * nights
	
def rental_car_cost(days):
  if days >= 7:
    return ((40 * days) - 50)
  elif days >= 3:
  	return ((40*days) - 20)