#----------------- Exercise 1 -----------------

# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Note: we are using list becuse we have to work on temperature values only

def extract_data(file_name):
    data_set = []
    with open(file_name, "r") as file:
        for line in file:
            tokens = line.split(",")
            try:
                temperature = int(tokens[1])
                data_set.append(temperature)
            except ValueError:
                pass
    return data_set
    


def avg_temperature(days):
        
    data = extract_data(file_name = "nyc_weather.csv")
            
    if days > len(data) or days < 0:
        return "Invalid number of days `{}`".format(days)
    return 'Average temperature of {} days is : {}'.format(days, round(sum(data[0 : days])/days, 2))

def max_temperature():
    data = extract_data(file_name = "nyc_weather.csv")
    return 'Max temperature : {}'.format( max(data) )



if __name__ == "__main__":    
    print(avg_temperature(days = -10))
    print(max_temperature())
