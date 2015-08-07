def task():
     dictionary={}
     
     for a in range(0,3):
             sub=raw_input("enter subject name")
             mark=int(raw_input("enter marks for"))
             dictionary[sub]=mark
     print dictionary        
task()
