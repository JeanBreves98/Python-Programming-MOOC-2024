import math

def get_station_data(filename: str):
    stations = {}
    with open(filename) as stations_file:
        for line in stations_file:  # Stores stations informations in variables
            parts = line.strip().split(";")
            if parts[0].lower() == "longitude":  # Skips header
                continue
            longitude = float(parts[0])
            latitude = float(parts[1])
            FID = int(parts[2])
            name = parts[3]
            total_slot = int(parts[4])
            operative = parts[5]
            id = str(parts[6])
            stations[name] = (longitude, latitude)  # Creates a dictionary where the key is the station name and the values are a tuple of latitude and longitude

    return stations


def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26    # Converts longitude into KMs
    y_km = (latitude1 - latitude2) * 111.2  # Converst latitude into KMs
    distance_km = math.sqrt(x_km**2 + y_km**2)  # Calculates distance using the Pythagorean theorem

    return distance_km


def greatest_distance(stations: dict):
    max_distance = 0
    station_pair = ("", "", 0)  # Tuple to store the result: (station1, station2, distance)

    station_names = list(stations.keys())   # Creates a list of station names

    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):  # Compare each pair only once because the previous ones have already been compared
            station1 = station_names[i]
            station2 = station_names[j]
            d = distance(stations, station1, station2)

            if d > max_distance:
                max_distance = d
                station_pair = (station1, station2, d)   # Stores the correct stations and distance into a tuple
    
    return station_pair


if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    print(stations)
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)