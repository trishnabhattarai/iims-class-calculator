#day 1 we have created a calculator for python Arithmetic Operators
while True: # while true will always run the code
#for packing
  user_input_1= float(input( "enter first number:"))
  user_input_2= float(input( "enter second number:"))
  user_input_operation= (input( "operation:"))
  if user_input_operation== "+" :
   print(f"Arithmetic Operators addition={user_input_1+ user_input_2}")
  elif user_input_operation== "-":
   print( f"Arithmetic Operators difference={user_input_1- user_input_2}")
  elif user_input_operation== "/":
   print( f"Arithmetic Operators divison={user_input_1/ user_input_2}")
  elif user_input_operation== "*":
   print( f"Arithmetic Operators Multiplication={user_input_1* user_input_2}")
  elif user_input_operation== "%":
   print( f"Arithmetic Operators Modulus={user_input_1% user_input_2}")
  elif user_input_operation== "**":
   print( f"Arithmetic Operators Exponentiation={user_input_1** user_input_2}")
  elif user_input_operation== "//":
   print( f"Arithmetic Operators Floor division={user_input_1// user_input_2}")

  else:
   print("sry")

  user_continue = input("do u wana to continue?(y/n)")

  if user_continue=="n":
    break

