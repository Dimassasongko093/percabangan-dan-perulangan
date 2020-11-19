#perulangan 
print("=============================================")
def pangkat(x):
    return(10** x)
    
n = int(input("\n Masukan nilai N : "))
    
for x in range(n + 1):
    if 10**x > n:
        print(pangkat(x))
        break
print("=============================================")