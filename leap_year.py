def checkLeapYear(year):
    
    if(year%400==0):
        return True

    if(year%100==0):
        return False

    if(year%4==0):
        return True

    return False

def main():
    year = int(input("Enter an year: "))
    leapYear = checkLeapYear(year)

    if leapYear == True:
        print(year," is leap year.")
    else:
        print(year," is not a leap year.")

if __name__ == '__main__':

    main()
