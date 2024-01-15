# leap year function

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if  year % 400 == 0:
               print("Leap Year")
            else:
                print("Not a Leap year .")
        else:
            print("leap year")
    else:
        print("Not a Leap year .")


# is_leap(2028)
        
def days_in_month(year , month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month-1]
  

year = int(input("Enter Year :"))
month = int(input("Enter Month :"))

if month < 0 or month > 12:
    print("The limited range is 1 - 12 ")
else:   
    days = days_in_month(year,month)
    print(days)