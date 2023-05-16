import math_funcs


def calulator_main():
    while True:
        operation = input("input operation ")

        currentOp = ""

        inputs = operation.split(" ")
        output = int(inputs[0])

        for data in inputs:
            if data in ["+", "-", "/", "*"]:
                currentOp = data
            else:
                match currentOp:
                    case "+":
                        output = math_funcs.add(output, int(data))
                    case "-":
                        output = math_funcs.substract(output, int(data))
                    case "/":
                        output = math_funcs.divide(output, int(data))
                    case "*":
                        output = math_funcs.multiply(output, int(data))

        print(output)


if __name__ == '__main__':
    calulator_main()
