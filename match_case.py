value_x = 5
match value_x:
    case 0:
        print("value_x is zero")
    case 4 if value_x % 2 == 0:
        print(f"value_x % 2 == 0 and case is {value_x}")
    case _ if value_x < 0:
        print("Value is negative")
    case _ if value_x > 10:
        print(f"Value is: {value_x}")
    case _ :
        print(value_x)


