def seconds_calculator(days, hours, minutes, seconds):
    """calculates the total number of seconds from daya, hours, minutes and seconds

       Args:
           days: the number of days
           hours: the number of hours
           minutes: the number of minutes
           seconds: the number of seconds

       Returns:
           returns the total number of seconds"""

    hours += days * 24
    minutes +=  hours * 60
    seconds += minutes * 60
    print(seconds)


seconds_calculator(1,1,1,1)