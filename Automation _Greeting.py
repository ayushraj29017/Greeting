# Correct me if I'm missing something
# import time
# # Morning: till 12:00,AfterNoon till 18:00,Evening till 20:00,else Night
# name=input("Enter your Name-> ")
# hour=time.strftime('%H')
# minute=time.strftime('%M')
# second=time.strftime('%S')
# print("The current time in your area is->",hour,':', minute,':',second)
# if(int(hour)<12):
#     print("Good Morning!",name)
# elif(int(hour)<18):
#     print("Good Afternoon!",name)
# elif(int(hour)<20):
#     print("Good Evening!",name)
# else:
#     print("Good Night!",name,"\nSir, I think its time for you to sleep")
Anyone you can try;
# import time
# name = input("Enter Your name : ").title()
# currentTime = time.strftime('%H:%M:%S')
# h = int(time.strftime('%H'))
# if(h<12):
#     print("Good Morning,",name)
# elif(h>12 and h<17):
#     print("Good Afternon,",name)
# else:
#     print("Good Night,",name)
 
