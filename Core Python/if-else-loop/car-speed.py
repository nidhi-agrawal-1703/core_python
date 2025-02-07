basic_speed=float(input("Enter car speed"))

if (basic_speed>0):
    for i in range(1,120):
        if(basic_speed>100):
            print("Car overheated and stopped at speed ",basic_speed)
            break
        else:
            print("Car is driving at the speed ",basic_speed)
            basic_speed+=20
else:
    print("Invalid input,please enter non-negative number as car speed")