def bankoper(initialbal, deposite, withdraw):
    totalbal = initialbal + deposite
    updatedbal = totalbal - withdraw

    return totalbal, updatedbal

if __name__ =="__main__":
    initialbal = int(input("enter amount as initial balance"))
    deposite = int(input("enter amount to deposite"))
    withdraw = int(input("enter withdrawal amount"))

    totalbal, updatedbal = bankoper(initialbal, deposite, withdraw)

    print("total balance:", totalbal)
    print("updated balance:", updatedbal)