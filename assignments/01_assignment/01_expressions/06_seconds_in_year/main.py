
days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
seconds_per_minute = 60

def main():
    
    seconds_per_year = days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute
    print("There are "+ str(seconds_per_year) + " seconds in a year!" )

if __name__ == "__main__":
    main()
