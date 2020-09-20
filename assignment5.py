def computepay(h,r):
    if h<=40:
    	return h*r
    else:
        return (40*r)+(1.5*r*(h-40))

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)