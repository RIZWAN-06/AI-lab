#def say_hello():
 #   print("hello")
#say_hello()



#def add_num(n1, n2):
 #   return n1 + n2
#n1 = int(input("enter num"))
#n2 = int(input("enter num"))
#print(add_num(5))



#logic in function

#def even_check(num):
 #   return num % 2 == 0 
#print(even_check(30))


#check even list

#def check_even_list(num_list):
 #   for number in num_list:
  #      if number % 2 == 0:
   #         return True
    #    else:
     #       pass
#print(check_even_list([1,1,1,2]))





#return even number in list

def check_even_list(num_list):
    #place holder:
    even_num = []
    for number in num_list:
        if number % 2 == 0:
            even_num.append(number)
        else:
            pass
    return even_num

print(check_even_list([1,2,3,4,5,8]))




