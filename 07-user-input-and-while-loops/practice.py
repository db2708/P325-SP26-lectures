from math import sqrt

a_str = input("Enter your a value:")
b_str = input("Enter your b value:")
c_str = input("Enter your c value:")

a = float(a_str)
b = float(b_str)
c = float(c_str)

sq_rt = sqrt(b**2 - 4*a*c)

root_1 = (-b + sq_rt) / (2*a)
root_2 = (-b - sq_rt) / (2*a)

if input == 'q': 
    quit()
else:
    print(root_1, root_2)
    
