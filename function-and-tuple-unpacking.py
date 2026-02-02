my_list = [('apple', 200), ('banana', 400), ('grape', 500)]

for item, price in my_list:
    print (price + (.1*price))


#Let's create a function for the loop
work_hour = [('abby', 100), ('billy', 200), ('cassy', 800)]

def employee_check(work_hour):
    #place holder for employee and hours the worked
     employee_of_the_month = ''
     current_max = 0

     for employee, hours in work_hour:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass
     
     #return
     return (employee_of_the_month, current_max)

name, hours = employee_check(work_hour)
print (name)

