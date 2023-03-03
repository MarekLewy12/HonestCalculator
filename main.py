msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0.0

def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer() == True:
        output = True
    else:
        output = False
    return  output


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


print(msg_0)


while True:
    try:

        calc = input()

        x, oper, y = calc.split()

        oper_list = ["+", "-", "*", "/"]

        if y == "M":
            y = memory
        if x == "M":
            x = memory

        x = float(x)
        y = float(y)

        if oper not in oper_list:
            print(msg_2)
            print(msg_0)
            continue

        check(x, y, oper)

        if oper == oper_list[0]:
            result = x + y
        elif oper == oper_list[1]:
            result = x - y
        elif oper == oper_list[2]:
            result = x * y
        elif oper == oper_list[3] and y == 0:
            print(msg_3)
            print(msg_0)
            continue
        else:
            result = x / y

    except ValueError:
        print(msg_1)
        print(msg_0)
        continue

    else:
        msg_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, msg_10, msg_11, msg_12]
        print(result)
        print(msg_4)
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    if msg_index <= 12:
                        print(msg_[msg_index])
                        answer = input()
                        if answer == 'y':
                            msg_index = msg_index + 1
                            continue
                        if answer == 'n':
                            break
                        else:
                            print("Wrong input, ending")
                            break
                    else:
                        memory = result
                        break
            else:
                memory = result

    print(msg_5)
    answer = input()
    if answer == 'y':
        print(msg_0)
        continue
    if answer == 'n':
        break
    else:
        break





























