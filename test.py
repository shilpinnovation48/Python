for temp in [31,45,32,40,50,55,12,36]:
           if temp > 31 and temp < 35:
                print ("sunny day:",temp)
           elif temp > 31 and temp < 40:
                print ("Warm day:",temp)
           elif temp > 40 and temp < 50:
                print ("High Temperature:",temp)
           else:
                print("Invalid")
