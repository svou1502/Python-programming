print("This is a Time Calculator")
print("1- Add two time formats together")
print("2- Find the difference between two different time formats")
print("3- Convert to Hours")
print("4- Convert to Minutes")
print("5- Convert Minutes to Time")
print("6- Convert Hours to Time")
print("7- Convert Days to Time")
print("8- Exit")

option = input("Enter an option: ")
        
if option == '1':
    time1 = input("Enter the first time (DD:HH:MM): ")
    time2 = input("Enter the second time (DD:HH:MM): ")

Total_time = time1 + time2
print("Result is", Total_time)