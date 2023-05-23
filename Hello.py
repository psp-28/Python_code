print('Hello World')

name = input("Please enter your name:")
print("Hello", name, ", Welcome to rate calculation tool")
print("\n\t\t We will calculate the rate per hour")

hrs= input("Please enter number of hours:")
rate= input("Please enter rate:")

cal= float(hrs)*float(rate)
print("Hello", name, ", here we have calculated rate per hour")

print("Pay: \a", cal)