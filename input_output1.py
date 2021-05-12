# I/O with simple input validation
while True:
    user_name = input("Please, enter your name below: \n")
    if user_name.isalpha() != True:
        print("Incorrect input. Try once more.")
        continue
    else:
        print("Hello, ", user_name, "!")
        break
        
while True:    
    user_surname = input("Please, enter your surname below: \n")
    if user_surname.isalpha() != True:
        print(user_name, ", your input is incorrect. Try once more.")
        continue
    else:
        print("Nice to meet you, ", user_name, user_surname, "!")
        break
        
while True:    
    age = input("How old are you? \n")
    try:
        age = int(age)
    except:
        print(user_name, user_surname, ", the age must contain the digits only.")
        continue
    print(user_name, user_surname, ", you are ", age, " years old. Thus, in 3 years you will be ", age + 3, "years old.")
    break
        
while True:
    user_location = input("Where do you live? \n")
    if user_location.isalpha() != True:
        print("Incorrect input. Try once more.")
        continue
    else:
        print(user_name, user_surname, ", you live in ", user_location)
        break
    
print("-"*70)
print("SUMMARY: Your name is ", user_name, user_surname, ". You are ", age, " years old and you live in ", user_location,".")
print("-"*70)
