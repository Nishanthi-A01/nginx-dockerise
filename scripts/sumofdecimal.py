

def sumofdecimalvalue(x):
    sum=0
    sum = x+(x^2)+(x^3)+(x^4)
    return(sum)

if __name__ == "__main__":
   x = input("Enter any decimal digit:") 
   sumofdecimalvalue(x)
