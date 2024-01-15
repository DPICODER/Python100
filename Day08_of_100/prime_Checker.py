def prime_chercker(number):
    IsPrime = True
    i = 1
    for i in range(2,number):
        print(i) 
        if number % i == 0:
            IsPrime = False
    
    if IsPrime:
        print(f"The Given Number : {number} Is A Prime number")
    else:
        print(f"The Given Number : {number} Is NOT A Prime number")


number = int(input("Enter a Number to check if its a prime or Not : "))

prime_chercker(number)
