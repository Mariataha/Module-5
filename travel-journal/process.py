#Change the script to display sales info for Monday instead of Tuesday.

def sales_reports(log_file, day_of_week):   #defines function "sales_reports". It takes 2 params, log_file & day_of_week
    for line in log_file:               #creates a for loop for each line of the log_file
        line = line.rstrip()       #strips white spaces from right side 
        day = line[0:3]      #sets variable that is the first 3 letters of the line
        if day == day_of_week: #if block is created if day = day_of_week
            print(line)        #prints all the lines beginning w/ day_of_week
            
def melon_orders(log_file, qty):     #defines function "qty_reports" w/ 2 params log_file, qty
    for line in log_file:           #creates a for loop for each line of the log_file
        line = line.rstrip()        #strips white spaces from right side of the line
        data = line.split(' ')       #Splits the line string into a list where each word is a list item
        if int(data[2]) > qty:      #Changes the value of index 2 into int and checks if its > qty
            print(line)             #prints all the lines where qty > requested qty

log_file = open("um-server-01.txt") #Initializes variable that references m-server-01.txt 
sales_reports(log_file, "Mon")         #runs the function  

log_file = open("um-server-01.txt") #m-server-01.txt lets another report run again
melon_orders(log_file, 10)           #runs the  function