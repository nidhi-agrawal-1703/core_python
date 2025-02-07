import datetime

current=datetime.datetime.now()
current_year=current.year

dob=datetime.datetime(1989,3,17)
dob_year=dob.year

age=dob_year-current_year
print("Your age is",age)