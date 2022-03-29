largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":  break 
        if len(num) < 1: break
        n = int(num)
    except:
        print ("Invalid input")
        continue    
    
    if largest is None:
        largest = n
    if smallest is None:
        smallest = n
    elif n > largest:
        largest = n
    elif n < smallest:
        smallest = n
                     
print ("Maximum is", largest)
print ("Minimum is", smallest)