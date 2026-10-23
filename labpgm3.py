import sys
def simpleInt(pr , intr, time):
    return (pr*intr*time)/100

if __name__ =="__main__":
    p = int(input("Enter value p"))
    i = int(input("Enter interest"))
    t = int(input("Enter the time"))

    result = simpleInt(p, i, t)
    print(f"Simple Interest: {result} ")
