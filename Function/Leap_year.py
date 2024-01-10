""" Python program to calculate the Leap Year and also to check the number of days in the month """

# Function to calculate the leap year;
def is_leap(year):
    if year % 4 == 0:              #(if the year is divided by century year i.e, 400 and 100)
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False        #(leap year is divided by 4 but it should not be century year which is divided by 100, if the year is divided by 100 then it is century year so it should be divided by 400 also.)
                


# Function to calculate the number of days in month;
def days_in_month(year,month):
    """This function returns the number of days in the month of the year by also taking consideration of leap year"""
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month-1]      # index in the list starts with 0


# Provide the inputs;
year = int(input("Enter the year: "))
month = int(input("\nEnter the month: "))   # Enter month in numerical
days = days_in_month(year,month)
print(days)

