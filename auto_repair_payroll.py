#Named constant to represent base hours
# the overtime multiplier
BASE_HOURS = 40     #Base hours per week
OT_MULTIPLIER = 1.5 #Overtime multiplier

# get the number of hours worked per week
hours = float(input ("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly pay rate: "))

#calculate and dispaly the gross pay.
if hours > BASE_HOURS:
    #Calculate the gross pay with overtime.
    #First, get the number of overtime hours worked.
    overtime_hours = hours - BASE_HOURS

    #calculate the amount of overtime pay
    overtime_pay = overtime_hours *  pay_rate * OT_MULTIPLIER

    #Calculate the gross pay
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    #calculate the gross pay without overtime
    gross_pay = hours * pay_rate

#Display the gross pay
print('The gross pay is $'. format(gross_pay,  '..2f'), sep='')