def perfect(number):
    if number <= 0 or (type(number) == float and number.is_integer() == False):
        return False
    number = int(number)
    sum = 1
    for i in range(2, number):
        if number % i == 0:
            sum += i
 
    
    if sum == number:
        return True
    else:
        return False


print(perfect(float(input(""))))