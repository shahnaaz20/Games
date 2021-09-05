# # Import Required Library
# from tkinter import *
# import random

# # Create Object
# root = Tk()

# # Set geometry
# root.geometry("300x300")

# # Set title
# root.title("Rock Paper Scissor Game")

# # Computer Value
# computer_value = {
# 	"0":"Rock",
# 	"1":"Paper",
# 	"2":"Scissor"
# }

# # Reset The Game
# def reset_game():
# 	b1["state"] = "active"
# 	b2["state"] = "active"
# 	b3["state"] = "active"
# 	l1.config(text = "Player			 ")
# 	l3.config(text = "Computer")
# 	l4.config(text = "")

# # Disable the Button
# def button_disable():
# 	b1["state"] = "disable"
# 	b2["state"] = "disable"
# 	b3["state"] = "disable"

# # If player selected rock
# def isrock():
# 	c_v = computer_value[str(random.randint(0,2))]
# 	if c_v == "Rock":
# 		match_result = "Match Draw"
# 	elif c_v=="Scissor":
# 		match_result = "Player Win"
# 	else:
# 		match_result = "Computer Win"
# 	l4.config(text = match_result)
# 	l1.config(text = "Rock		 ")
# 	l3.config(text = c_v)
# 	button_disable()

# # If player selected paper
# def ispaper():
# 	c_v = computer_value[str(random.randint(0, 2))]
# 	if c_v == "Paper":
# 		match_result = "Match Draw"
# 	elif c_v=="Scissor":
# 		match_result = "Computer Win"
# 	else:
# 		match_result = "Player Win"
# 	l4.config(text = match_result)
# 	l1.config(text = "Paper		 ")
# 	l3.config(text = c_v)
# 	button_disable()

# # If player selected scissor
# def isscissor():
# 	c_v = computer_value[str(random.randint(0,2))]
# 	if c_v == "Rock":
# 		match_result = "Computer Win"
# 	elif c_v == "Scissor":
# 		match_result = "Match Draw"
# 	else:
# 		match_result = "Player Win"
# 	l4.config(text = match_result)
# 	l1.config(text = "Scissor		 ")
# 	l3.config(text = c_v)
# 	button_disable()

# # Add Labels, Frames and Button
# Label(root,
# 	text = "Rock Paper Scissor",
# 	font = "normal 20 bold",
# 	fg = "blue").pack(pady = 20)

# frame = Frame(root)
# frame.pack()

# l1 = Label(frame,
# 		text = "Player			 ",
# 		font = 10)

# l2 = Label(frame,
# 		text = "VS			 ",
# 		font = "normal 10 bold")

# l3 = Label(frame, text = "Computer", font = 10)

# l1.pack(side = LEFT)
# l2.pack(side = LEFT)
# l3.pack()

# l4 = Label(root,
# 		text = "",
# 		font = "normal 20 bold",
# 		bg = "white",
# 		width = 15 ,
# 		borderwidth = 2,
# 		relief = "solid")
# l4.pack(pady = 20)

# frame1 = Frame(root)
# frame1.pack()

# b1 = Button(frame1, text = "Rock",
# 			font = 10, width = 7,
# 			command = isrock)

# b2 = Button(frame1, text = "Paper ",
# 			font = 10, width = 7,
# 			command = ispaper)

# b3 = Button(frame1, text = "Scissor",
# 			font = 10, width = 7,
# 			command = isscissor)

# b1.pack(side = LEFT, padx = 10)
# b2.pack(side = LEFT,padx = 10)
# b3.pack(padx = 10)

# Button(root, text = "Reset Game",
# 	font = 10, fg = "red",
# 	bg = "black", command = reset_game).pack(pady = 20)

# # Excecute Tkinter
# root.mainloop()


# from tkinter import *

# def callback():
#     print ('You clicked the button!')

# top = Tk()
# L1 = Label(top, text="User Name")
# L1.grid(row=0, column=0)
# E1 = Entry(top, bd = 5)
# E1.grid(row=0, column=1)

# MyButton1 = Button(top, text="Submit", width=10, command=callback)
# MyButton1.grid(row=1, column=1)

# top.mainloop()



from tkinter import* 
from random import randint  
from tkinter import ttk

root=Tk()
root.title("my window name")
label=Label(root,font=("Arial",21),text="game of rock,paper,scissoir",bg="black",fg="white")
label.pack()
root.geometry("800x900+300+200")
root.resizable(0,0)
# root.mainloop()

rock=PhotoImage(file="/home/anushka/Downloads/ocks.pngr")
paper=PhotoImage(file="/home/anushka/Downloads/papers.png")
scissoir=PhotoImage(file="/home/anushka/Downloads/scissorss.png")
var = StringVar()
image_list=[rock,paper,scissoir]
pick_number=randint(0,2)

image_label=Label(root,image=image_list[pick_number])
image_label.pack(pady=20)

#create spin function
    
def spin():
    pick_number=randint(0,2)
    image_label.config(image=image_list[pick_number])
    def win():
        print("you win!")

    def lose():
        print("you loss!")
    while True:
        player_choice=input("what do you pick?(rock,paper,scissors)")
        player_choice.strip()
        random_moves=randint(0,2)
        moves=["rock","paper","scissors"]
        computer_choice=moves[random_moves]
        print(computer_choice)
        # if computer_choice == 1:
        #     computer_choice = 'rock'
        # elif computer_choice ==2:
        #     computer_choice = 'paper'
        # else:
        #     computer_choice= 'scissors'

        if player_choice==computer_choice:
            print("choice your option")
        elif player_choice=="rock" or computer_choice=="scissors":
            win()
        elif player_choice=="paper" or computer_choice=="scissors":
            lose()
        elif player_choice=="scissors" or computer_choice=="paper":
            win()
        elif player_choice=="scissors" or computer_choice=="rock":
            lose()
        elif player_choice=="paper" or computer_choice=="rock":
            win()
        again=input("do you want play again? (y or no").strip()
        if again=="n":
            break

        if player_choice==0:
            if pick_number==0:
                win_lose_label.config(text="Its A Tie! spin again...")
            elif pick_number==1:
                win_lose_label.config(text="paper cover rock! you lose....")
            elif pick_number==2:
                win_lose_label.config(text="rock cutes smashes scissors! you win")

        #if user piks paper
        if player_choice==1:
            if pick_number==1:
               win_lose_label.config(text= "Its A Tie! spin again...")
            elif pick_number==0:
                win_lose_label.config(text ="paper cover rock! you win....")
            elif pick_number==2:
                win_lose_label.config(text= "scissors cutes paper! you loss")

        #if user piks scissors
        if player_choice==2:
            if pick_number==2:
                win_lose_label.config(text="Its A Tie! spin again...")
            elif pick_number==0:
                win_lose_label.config(text = "rock smashes scissors! you lose....")
            elif pick_number==1:
               win_lose_label.config(text="scissors cutes paper! scissors! you win")
            
            
#make our choice
player_choice=ttk.Combobox(root,value=("rock","paper","scissoir"))
player_choice.current(0)
player_choice.pack(pady=20)

#create a spin button
spin_button=Button(root,text="spin!",command=spin)
spin_button.pack(pady=10)

exit_button=Button(root,text="exit!",command=exit)
exit_button.pack(pady=100)

#label for showing if you won or not
win_lose_label=Label(root,text=var.get(),font=("Helvetica",18))
win_lose_label.pack(pady=50)


root.mainloop()