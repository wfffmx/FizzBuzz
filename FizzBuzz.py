#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz”.

#for loop
for num in range(1,101):
    
    string = ""

    #check for multiple of 3
    if num % 3 == 0:
        string = string + "Fizz"
    
    #check for multiple of 5
    if num % 5 == 0:
        string = string + "Buzz"
    
    #check for multiples of both 3 and 5
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    
    print(string)