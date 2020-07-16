# -------------------- Exercise 2------------------------

# What was the temperature on Jan 9?
# What was the temperature on Jan 4?

# Note: Here we must have to use hash-map because we want to get temperature value of a particular date 

def extract_data(file_name):
    data_set = []
    with open(file_name, "r") as file:
        for line in file:
            tokens = line.split(",")
            try:
                data_set[tokens[0]] = int(tokens[1])
            except ValueError:
                pass
    return data_set


def temp_of_day(day):
    data = extract_data(file_name="nyc_weather.csv")
    # Check if date is correct
    if not day in data.keys():
        return "`{}` does not exists in data set".format(day)
    return "Teperature on {} was : {}".format(day, data[day])

if __name__ == "__main__":
    temp_of_day('Jan 94')
