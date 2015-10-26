# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def leap_year(year):
    if year % 4 == 0:
        return 1
    else:
        return 0
    
def man(month):
    list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mon = 0
    while month < 12:
        mon = mon + list1[month]
        if month == 12:
            return 0
            break
        else:
            month = month + 1
    return mon
    
def days_left(year, month, day):
    list2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month <= 2:
        x = (list2[month-1] - day) + man(month) + leap_year(year)
        return x 
    else:
        x = x = (list2[month-1] - day) + man(month) 
        return x
    

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    yeardiff = year2 - year1 
    days_left_birth = days_left(year1, month1, day1)
    days_left_curr = days_left(year2, month2, day2)
    if yeardiff == 0:
        days_all = (yeardiff / 4) + (days_left_birth - days_left_curr)
        return days_all
    elif yeardiff == 1:
        days_all = (yeardiff / 4) + days_left_birth + (365 - days_left_curr) + leap_year(year2)
        return days_all
    else:
        days_all = (yeardiff + 1) * 365 + (yeardiff / 4) + days_left_birth - (365 - days_left_curr)
        return days_all
    

    
#print daysBetweenDates(2012,1,1,2012,2,28)
#print daysBetweenDates(2012,1,1,2012,3,1)
#print daysBetweenDates(2011,6,30,2012,6,30)
#print daysBetweenDates(2011,1,1,2012,8,8)
#print daysBetweenDates(1900,1,1,1999,12,31)


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
