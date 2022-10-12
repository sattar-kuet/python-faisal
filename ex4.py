import math

a = input("Edge Length: ")
a = float(a)
s = round(a**2*math.sqrt(3), 4)
v = round(a**3*math.sqrt(2)/12, 4)
h = round(a*math.sqrt(6)/3,4)

print(f"Surface: {s}")
print(f"Volume: {v}")
print(f"Height: {h}")