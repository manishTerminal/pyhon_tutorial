print("Simple Interest")
def simpleInterest(p, r, t):
    si = (p*r*t)/100.0
    return si

p = int(input("Enter principle amount : "))
r = int(input("Enter rate of interest : "))
t = int(input("Enter the time : "))
si = simpleInterest(p, r, t)

print(si)