swimming_time=float(input("Enter swimming time (minutes):"))
cycling_time=float(input("Enter cycling time (minutes):"))
running_time=float(input("Enter running time (minutes):"))
total_time= swimming_time+ cycling_time+ running_time

qualifying_time=100

if total_time<= qualifying_time:
    print("Provincial Colours")
elif qualifying_time< total_time and total_time<= qualifying_time +5:
    print("Provincial Half Colours")
elif qualifying_time+6<=total_time and total_time<=qualifying_time+ 10:
    print("Provincial Scroll")
else:
    print("No award")