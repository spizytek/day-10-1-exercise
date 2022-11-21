def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
        return 1
      else:
        print("Not leap year.")
        return 0
    else:
      print("Leap year.")
      return 1
  else:
    print("Not leap year.")
    return 0

def days_in_month(yr, mnth):
  """ This is a doc string for a function takes year and month as argument"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  ret  = is_leap(yr)
  dys  = month_days[(mnth-1)]
  if((ret == 1) and mnth == 2):
      return dys+1
  else:
    return dys
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












