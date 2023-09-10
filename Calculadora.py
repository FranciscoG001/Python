def InsertValue():
    print("Type your value:")
    value = input()
    return value

def Operator():
    print("Type the operator(+,-,x,/):")
    operator = input()
    return operator

def OperationType(value1,op,value2):
    if op == "+":
        result = float(value1) + float(value2)
    elif op == "-":
        result = float(value1) - float(value2)
    elif op == "/":
        if value2 == 0:
            result = "Impossible to divide by zero!"
        elif value2 != 0:
            result = float(value1) / float(value2)
    else:
        result = float(value1) * float(value2)
    return result

def Operation(value1,op,value2):
    resultString = value1 + " " + op + " " + value2
    result = OperationType(value1,op,value2)
    print(f"The result of the operation {resultString} is: {result}")

def Main():
    firstValue = InsertValue()
    operator = Operator()
    secondValue = InsertValue()
    Operation(firstValue,operator,secondValue)

Main()

