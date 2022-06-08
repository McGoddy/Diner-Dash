from tkinter import *

root1 = Tk(className='DinerDash')

# Adjust size
root1.geometry("825x615")

# Add image file
bg = PhotoImage(file = "Images/B1.png")

# Create Canvas
canvas1 = Canvas( root1, width = 825,
				height = 615)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")

#Create Previous function
def previous(): 
    root1.destroy()
    import App
    App.mainloop()

def button():
    button_NewGame = Button(root1, text = "New Game", bg='#ffffff',
                  font=("vintagio",12, "bold"), activebackground='#FFFC33', bd= 0)
    button_NewGame.config(width =22, height =3)
    
    
    button_N_canvas = canvas1.create_window( 309, 480, anchor = "nw",
                                           window = button_NewGame)
    
    button_back = Button(root1, text = "Back to the Menu", bg= '#ffffff',
                         font=("vintagio", 10, "bold"), activebackground = '#FFFC33', bd= 0, command= previous)
    button_back.config(width= 17, height= 2)
    
    button_b_canvas = canvas1.create_window( 680, 5, anchor ="nw",
                                            window = button_back)



button()

#execute the program
root1.mainloop()