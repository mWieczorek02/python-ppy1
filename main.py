# Mikołaj Wieczorek s24697

def calulator_main():
    while True:
        operation = input("input operation ")

        currentOp = ""

        inputs = operation.split(" ")
        output = int(inputs[0])

        for data in inputs:
            if data in ["+", "-", "/", "%", "*"]:
                currentOp = data
            else:
                match currentOp:
                    case "+":
                        output += int(data)
                    case "-":
                        output -= int(data)
                    case "/":
                        output = output / int(data)
                    case "%":
                        output = output & int(data)
        print(output)


if __name__ == '__main__':
    calulator_main()
