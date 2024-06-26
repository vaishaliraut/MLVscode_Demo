# Take Principal (P), Period (N) Years , Rate of interest (R) % p.a 
P = float(input('Please Enter principal in INR:'))
N = float(input('Please Enter Period in Years:'))
R = float(input('Please Enter Rate of Interest in %.p.a :'))
# Calcuate SI
I = (P*N*R)/100
#calculate Amount
A = P+I
# Print Above Results
print(f'Simple interest for given values is {I:.2f} INR')
print(f'Amount is {A:.2f} INR')