name = input("What is your name? ")
age = input("What is "+name+" 's age? ")

def age_in_one_year(name, age):
    age_next_year = int(age) + 1
    print("In one year, " + name + " will be " + str(age_next_year) + " years old.")

