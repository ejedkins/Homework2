from datetime import date
#create a list called months that connects the months of the year with a number
date = date.today()
months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
          "September": 9, "October": 10, "November": 11, "December": 12}


#open up inputDates file and read it and the parsedDates file and write it.
file1 = open('inputDates.txt', 'r')

file2 = open('parsedDates.txt', 'w')

#For every date in the inputDates file, remove the extra spaces using strip.
for date in file1:
    date = date.strip()
#If the the date is equal to -1 then exit the for loop
    if date == '-1':
        break
#Make r1 equal to the date.find(' ') to start off the date with the correct formatting
    r1 = date.find(' ')
#if r1 is equal to -1 or date[:r1] is not in the list called months, then the loop continues
    if r1 == -1 or date[:r1] not in months:
        continue
#Month is now equal to date[:r1]
    month = date[:r1]
    # Make r3 equal to the date.find(',') make sure the middle of the date has the correct spacing
    r2 = date.find(',')
    #r2 will represent the day of the date so r2 must be equal to -1 or between 1 & 31. The loop will then continue
    if r2 == -1 or int(date[r1 + 1:r2]) < 1 or int(date[r1 + 1:r2]) > 31:
        continue
    # day is now equal to the date[r1 + 1:r2]
    day = date[r1 + 1:r2]
    #Make r3 equal to the date.find(', ') make sure the end of the date has the correct spacing
    r3 = date.find(', ')
    #If r3 is equal to -1, then the loop can continue
    if r3 == -1:
        continue
    #The year will be representsed by r3
    year = date[r3+2:r3 + 7]
    #Formatting for the the parsed ouput txt
    parsed = '{}/{}/{}'.format(months[month], day, year)

    print(parsed)
    #Writing the text for the paresedDates.txt file
    file2.write(parsed)
    file2.write('\n')
#Close both the inputDates.txt file and the parsedDates.txt file
file1.close()
file2.close()
