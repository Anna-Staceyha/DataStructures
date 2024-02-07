pupils = ["Josh","Maggie","Sarah","Charlie","Lucy","Ashley"]

def searchName():
    name = input("Enter a name: ")
    Flag = False
    for i in range(6):
       if name == pupils[i]:
          Flag = True
          print(i+1)
        
searchName()

def noName():
   for i in range(6):
      if name != pupils[i]:
         Flag = False
         print("Term was not found.")

noName()