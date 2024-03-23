first_day = int(input())
second_day = int(input())
third_day = int(input())

if first_day == second_day and first_day == third_day and \
    second_day == third_day:
    print("3")
elif first_day == second_day:
    print("2")
elif first_day == third_day:
    print("2")
elif third_day == second_day:
    print("2")
else:
    print("1")
