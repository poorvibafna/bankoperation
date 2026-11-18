import sys
def bankoper(initialbal, deposite, withdraw):
    totalbal = initialbal + deposite
    updatedbal = totalbal - withdraw

    return totalbal, updatedbal

if __name__ =="__main__":
    initialbal = int(sys.argv[1])
    deposite = int(sys.argv[2])
    withdraw = int(sys.argv[3])

    totalbal, updatedbal = bankoper(initialbal, deposite, withdraw)

    print("total balance:", totalbal)
    print("updated balance:", updatedbal)