#TASK 1
#2)which one is greater and which one is less?
#ex:
#input1:12
#input2:14

#output:input1 is less than input2 and input2 is greater than input1

#ex:
#input1:16
#input2:14

#output:input2 is less than input1 and input1 is greater than input2

input1=int(input("Enter the number:"))
input2=int(input("Enter the number:"))
if input1<input2 :
    print("Input1 is lesser than input2 and input2 is greater than input1")
else :
    print("Input2 is greater than input1 and input1 is lesser than input2")