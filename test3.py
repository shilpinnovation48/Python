temp=int(raw_input('Enter a Temperature value'))
while True:
        if temp > 31 and temp < 35:
            print ("sunny day:",temp)
            break
        elif temp > 31 and temp < 40:
            print ("Warm day:",temp)
            break
        elif temp > 40 and temp < 50:
            print ("High Temperature:",temp)
            break
        else:
            print("Invalid")
            break

