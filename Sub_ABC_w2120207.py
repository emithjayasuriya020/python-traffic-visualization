#Author: M. E. S. Jayasuriya
#Date: 23/11/2024
#Student ID: 20231293

# Task A: Input Validation
def validate_date_input():
    try:
        while True:
            day = int(input("Please enter the day of the survey in the format DD: "))
            if day >= 1 and day <= 31 and day != 0:
                break
            print("Out of range - values must be in the range 1 and 31.")

        while True:
            month = int(input("Please enter the month of the survey in the format MM: "))
            if month >= 1 and month <= 12:
                break
            print("Out of range - values must be in the range 1 to 12.")

        while True:
            year = int(input("Please enter the year of the survey in the format YYYY: "))
            if year >= 2000 and year <= 2024:
                break
            print("Out of range - values must range from 2000 and 2024.")
        global file_date
        global file_date_histo
        file_date_histo = f"{day:02}/{month:02}/{year:04}"
        file_date = f"{day:02}{month:02}{year:04}"

        return f"{day:02}{month:02}{year:04}", file_date_histo

    except ValueError:
        print("Integer required")
    pass

def validate_continue_input():
    while True:
        dataset_validate_input = input("Do you want to select another data file for a different date? Y/N: ")
        dataset_validate_input = dataset_validate_input.lower()
        if dataset_validate_input == "y":
            return True
        if dataset_validate_input == "n":
            print("End of run")
            return False
        else:
            print("Please enter “Y” or “N”.")
    pass

# Task B: Processed Outcomes
import csv
# Referance: docs.python.org/3/library/csv.html
def process_csv_data(file_path):
    try:
        # Referance: https://docs.python.org/3/library/csv.html#csv.DictReader
        with open(file_path,'r') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)

        total_vehicles = 0
        total_trucks = 0
        total_electric_vehicles = 0
        two_wheeled_vehicles = 0
        buses_heading_north = 0
        straight_through_vehicles = 0
        over_speed_limit_vehicles = 0
        total_vehicles_elm_avenue = 0
        total_vehicles_hanley_highway = 0
        total_scooters_elm_avenue = 0
        bicycles_per_hour = {hour: 0 for hour in range(24)}
        hourly_counts = {}
        rainy_hours = set()

        for row in data:
            total_vehicles += 1

            if row["VehicleType"] == "Truck":
                total_trucks += 1

            if row["elctricHybrid"] == "True":
                total_electric_vehicles += 1

            if row["VehicleType"] in ["Motorcycle", "Scooter", "Bicycle"]:
                two_wheeled_vehicles += 1

            if row["JunctionName"] == "Elm Avenue/Rabbit Road" and row["travel_Direction_out"] == "N" and row["VehicleType"] == "Buss":
                buses_heading_north += 1

            if row["travel_Direction_out"] == row["travel_Direction_in"]:
                straight_through_vehicles += 1

            if row['VehicleType'] == 'Bicycle':
                hour = int(row['timeOfDay'].split(':')[0])
                if 0 <= hour < 24:
                    bicycles_per_hour[hour] += 1

            if int(row["JunctionSpeedLimit"]) < int(row["VehicleSpeed"]):
                over_speed_limit_vehicles += 1

            if row["JunctionName"] == "Elm Avenue/Rabbit Road":
                total_vehicles_elm_avenue += 1

            if row["JunctionName"] == "Hanley Highway/Westway":
                total_vehicles_hanley_highway += 1

            if row["JunctionName"] == "Elm Avenue/Rabbit Road" and row["VehicleType"] == "Scooter":
                total_scooters_elm_avenue += 1

            if row["JunctionName"] == "Hanley Highway/Westway":
                hour = row["timeOfDay"].split(":")[0]
                hourly_counts[hour] = hourly_counts.get(hour, 0) + 1

            if row["Weather_Conditions"] == "Overcast":
                hour = row["timeOfDay"].split(":")[0]
                rainy_hours.add(hour)

        trucks_percentage = round((total_trucks / total_vehicles) * 100) if total_vehicles else 0
        scooter_percentage = round((total_scooters_elm_avenue / total_vehicles_elm_avenue) * 100) if total_vehicles_elm_avenue else 0

        total_bicycles = sum(bicycles_per_hour.values())
        total_hours = sum(1 for count in bicycles_per_hour.values() if count > 0)
        avg_bicycles = round(total_bicycles / total_hours) if total_hours > 0 else 0

        max_traffic = max(hourly_counts.values(), default=0)
        peak_hours = [
            f"Between {hour}:00 and {int(hour) + 1}:00"
            for hour, count in hourly_counts.items()
            if count == max_traffic
        ]

        total_rain_hours = len(rainy_hours)

        final = {
            "Total Vehicles" : total_vehicles,
            "Total Number of Trucks" : total_trucks,
            "Total Number of electric vehicles" : total_electric_vehicles,
            "Total Number of two wheeled vehicles" : two_wheeled_vehicles,
            "Busses Heading North(Elm)" : buses_heading_north,
            "Straight-through vehicles" : straight_through_vehicles,
            "Truck Percentage" : trucks_percentage,
            "Average Bicycles per hour" : avg_bicycles,
            "Vehicles over the speed limit" : over_speed_limit_vehicles,
            "Vehicles recorded through only Elm Avenue/Rabbit Road junction" : total_vehicles_elm_avenue,
            "Vehicles recorded through only Hanley Highway/Westway junction" : total_vehicles_hanley_highway,
            "Scooter percentage through Elm Avenue/Rabbit Road" : scooter_percentage,
            "Peak traffic count" : max_traffic,
            "Peak hours" : peak_hours,
            "Total Rain Hours" : total_rain_hours,
        }
        result = (
            (f"data file selected is traffic_data{file_date}.csv"),
            (f"The total number of vehicles recorded for this date is {final['Total Vehicles']}"),
            (f"The total number of trucks recorded for this date is {final['Total Number of Trucks']}"),
            (f"The total number of electric vehicles for this date is {final['Total Number of electric vehicles']}"),
            (f"The total number of two-wheeled vehicles for this date is {final['Total Number of two wheeled vehicles']}"),
            (f"The total number of Buses leaving Elm Avenue/Rabbit Road heading North is {final['Busses Heading North(Elm)']}"),
            (f"The total number of Vehicles through both junctions not turning left or right is {final['Straight-through vehicles']}"),
            (f"The percentage of total vehicles recorded that are trucks for this date is {final['Truck Percentage']}%"),
            (f"The average number of Bikes per hour for this date is {final['Average Bicycles per hour']}"),
            (f"The total number of Vehicles recorded as over the speed limit for this date is {final['Vehicles over the speed limit']}"),
            (f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {final['Vehicles recorded through only Elm Avenue/Rabbit Road junction']}"),
            (f"The total number of vehicles recorded through Hanley Highway/Westway junction is {final['Vehicles recorded through only Hanley Highway/Westway junction']}"),
            (f"{final['Scooter percentage through Elm Avenue/Rabbit Road']}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters."),
            (f"The highest number of vehicles in an hour on Hanley Highway/Westway is {final['Peak traffic count']}"),
            (f"The most vehicles through Hanley Highway/Westway were recorded between {final['Peak hours']}"),
            (f"The number of hours of rain for this date is {final['Total Rain Hours']}"),
            (f""),
            (f"***************************"),
            (f"")
        )
        return result

    except FileNotFoundError:
        print("File not found")
        return{}

def display_outcomes(outcomes):
    for output in outcomes:
        print(f"{output}")
    pass

# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    try:
        with open(file_name, "a+") as file:
            for statement in outcomes:
                file.write(f"{statement}\n")
    #Referance: https://www.askpython.com/python/examples/handling-ioerrors
    except IOError:
        print("Unable to save file")
    pass


"""This used for A B C parts in submission one now we can run code true Histogram Program
def main():
    while True:
        # Task A: Input Validation
        date_str = validate_date_input()
        filename = f"traffic_data{date_str}.csv"

        # Task B: Process CSV Data and Calculate Outcomes
        global outcomes
        outcomes = process_csv_data(filename)

        # Displaying outcomes if file exists and data is processed
        if outcomes:
            display_outcomes(outcomes)
            # Task C: Saving to txt file
            save_results_to_file(outcomes, file_name="results.txt")

        if not validate_continue_input():
            break

main()"""