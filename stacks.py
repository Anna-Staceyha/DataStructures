cars = []

def push(car):
    cars.append(car)

def pop():
    cars.pop()

print(cars)
push("mondeo")
print(cars)
pop()
print(cars)

def isFull():
   if len(cars) == 6:
       return True
    else:
       return False

def isEmpty():
    if len(cars) == 0:
        return True
    else: 
        return False