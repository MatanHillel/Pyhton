import webbrowser
import math
# Function to calculate distance between two geographic coordinates
def haversine(lat1, lon1, lat2, lon2):
        # Radius of the Earth in km
        R = 6371.0
        # Convert degrees to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        # Compute differences
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        # Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    # Define the list of people with their latitude and longitude
people = [
    {'name': 'RazY', 'latitude': 32.069359, 'longitude': 34.812181}, # Givatayim
    {'name': 'Ohadi', 'latitude': 32.041754, 'longitude': 34.810054}, # Tel Aviv
    {'name': 'Shag', 'latitude': 31.897277, 'longitude': 34.812902},  # Rehovot
    {'name': 'Itay', 'latitude': 32.176593, 'longitude': 34.854402},  # Herzelia
    {'name': 'BarK', 'latitude': 32.023995, 'longitude': 34.746677},  # Bat Yam
    {'name': 'IdanK', 'latitude': 32.023995, 'longitude': 34.746677}, # Bat Yam
    {'name': 'Matan', 'latitude':  31.995068, 'longitude': 34.949674},# Shoham
    {'name': 'Shai', 'latitude': 31.961054, 'longitude': 34.789930},  # Rishon
    {'name': 'Dor', 'latitude': 31.984225776418214, 'longitude': 34.7754845948208},  # Shoham
    {'name': 'Lisa', 'latitude': 31.984225776418214, 'longitude': 34.7754845948208},  # Shoham
]
while(1):
    chosen_people = []
    for person in people:
        answer = input(f"Considering {person['name']} in the calculation? (y/n): ").strip().lower()
        while(answer != "y" and answer != "n" ):
            answer = input("You piece of shit only type y or n: ").strip().lower()
        if answer == 'y':
            chosen_people.append(person)
    # Initialize variables to calculate the sum of latitudes and longitudes
    sum_latitude = 0
    sum_longitude = 0

    # Loop through the list of people and sum up their latitude and longitude
    for person in chosen_people:
        sum_latitude += person['latitude']
        sum_longitude += person['longitude']
    if len(chosen_people) == 0:
        answer = input("People are lazy, there is no one, try again? (y/n): ")
        while (answer != "y" and answer != "n"):
            answer = input("You piece of shit only type y or n: ").strip().lower()
        if(answer == "y"):
            continue
        break
    # Calculate the average latitude and longitude to find the meeting point
    meeting_latitude = sum_latitude / len(chosen_people)
    meeting_longitude = sum_longitude / len(chosen_people)

    #print(f"The optimal meeting point is at latitude: {meeting_latitude}, longitude: {meeting_longitude}")
    answer = input("Home meeting? (y/n): ")
    while(answer != "y" and answer != "n" ):
            answer = input("You piece of shit only type y or n: ").strip().lower()
    if answer == "n":
        # Construct the Google Maps URL with the calculated coordinates
        maps_url = f"https://www.google.com/maps?q={meeting_latitude},{meeting_longitude}"
        # Open the constructed URL in the default web browser
    else:
        closest_person = min(chosen_people, key=lambda person: haversine(meeting_latitude, meeting_longitude, person['latitude'],person['longitude']))
        maps_url = f"https://www.google.com/maps?q={closest_person['latitude']},{closest_person['longitude']}"
    webbrowser.open(maps_url)
    print("\n\n New session!!!\n")