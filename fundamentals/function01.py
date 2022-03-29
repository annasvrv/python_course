def computepay(h,r):
    if h<=40:
        p=h*r
        return p
    elif h>40:
        p=40*r+((h-40)*(r*1.5))
        return p

try:
    Hours = input("Enter Hours:")
    h=float(Hours)
    Rate = input("Enter Rate:")
    r=float(Rate)
except:
    print ("Error, not a number.")    

p = computepay(h,r)
print ("Pay:", p)