user_choice=""
started=False
while True:
    #user_choice!= 'quit':
    user_choice=input(">").lower()
    if user_choice=="start":
        if started:
            print("Car is already started!")
        else:
            started=True
            print("Car started....")
    elif user_choice=="stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started=False
            print("Car stopped.")
    elif user_choice=="help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif user_choice=="quit":
        break
    else:
        print("Sorry I don't understand that")

