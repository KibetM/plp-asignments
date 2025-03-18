num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
operand=input("Enter an operation :(+,-,/,*) : ")

operations={
    "+":num1+num2,
    "-":num1-num2,
    "*":num1*num2,
    "/":num1/num2

}
print(f"{num1} {operand} {num2} = {operations[operand]}")