# day 3 :task overview
user_task_list=[]  #to store the task list
user_money_list=[]  #to store the money list
while True:
  user_option= input("""
  1. add
  2. modify
  3. view
  4. Update
  """)
  if user_option=="1":
    user_date = input("Date (MM/DD/YYYY): ") #take the input fron the user and store it in user_date variable
    user_task= input("Task")
    user_task_list.append((user_task))
    user_money= int(input("Money"))
    user_money_list.append((user_money))
    print("Added.")
  elif user_option=="2":
    user_update=input("What do you want to Update?(date/task/money)")
    if user_update=="date":
      user_date=(input("Renter the Date:"))
      print("Updated")
    elif user_update=="task":
      user_task= input("Renter the task:")
      print("Updated")
    elif user_update=="money":
      user_money= int(input("Renter the money:"))
      print("Updated")
    else:
      print("Sorry,You can't Update the Data.")
  elif user_option=="3":
    print(f"Date: {user_date} Task: {user_task_list} Money: {user_money_list}") # f is a f string basically the data taken from the user is added to the variable called user_date
  elif user_option=="4":
    user_option1= input("what do you want to update?(task/money)")
    if user_option1=="task":
      user_task= input("enter the new task")
      user_task_list.append((user_task))
      print(user_task_list)
    elif user_option1=="money":
      user_money= input("enter the new money4")
      user_money_list.append((user_money))
      print(user_money_list)
  elif user_option=="5":
    sum = 0
    for money in user_money_list:
      sum+=int(money)
    print("Total = ", sum)

