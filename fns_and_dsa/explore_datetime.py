from datetime import datetime, timedelta, date

current_date = ""
future_date = ""

def display_current_datetime():
	dt = datetime.now()
	return dt

current_date = display_current_datetime()

print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
	today = date.today()
	return today + timedelta(days=days)

days = float(input("Enter the number of days to add to the current date: "))

future_date = calculate_future_date(days)

print("Future date:", future_date)
