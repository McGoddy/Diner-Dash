# Import module
import threading
from tkinter import *
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
import pygame
from pygame.locals import *
from pygame import mixer
 







# Create object
root = Tk(className='DinerDash')

# Adjust size
root.geometry("825x615")

# Add image file
bg = PhotoImage(file = "Images/A1.png")

# Create Canvas
canvas1 = Canvas( root, width = 825,
				height = 615)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")

#Define a nextpage function
def nextpage():
    root.destroy()
    import Waiting1
    

#close window
# Define a function to close the window
def close():
   #win.destroy()
   root.quit()

def button(): 
 button1 = Button( root, text = "FLO'S CAREER",bg='#ffffff', font=("vintagio",12, "bold"),
                  activebackground='#FFFC33', bd= 0, command = nextpage)
 button1.config(width =22, height =3)

 button2 = Button( root, text = "ENDLESS SHIFT",bg='#ffffff',
                  font=("vintagio",12, "bold"), activebackground='#FFFC33', bd= 0)
 button2.config(width =22, height =3)

 button3 = Button( root, text = "HIGH SCORES",bg='#ffffff',
                  font=("vintagio",12, "bold"), activebackground='#FFFC33', bd= 0)
 button3.config(width =22, height =3)

 button_help = Button(root, text = "HELP",bg='#ffffff',
                      font=("vintagio",12, "bold"), activebackground='#FFFC33', bd= 0)
 button_help.config(width =11, height =2)

 button_option = Button( root, text = "OPTION",bg='#ffffff',
                        font=("vintagio",12, "bold"), activebackground='#FFFC33', bd= 0)
 button_option.config(width =11, height =2)

 button_exit = Button( root, text = "QUIT",bg='#ffffff', activebackground='#FFFC33', bd= 0,
                      font=("vintagio",12, "bold"), command=close)
 button_exit.config(width =11, height =2)

# Display Buttons
 button1_canvas = canvas1.create_window( 105, 210,
									anchor = "nw",
									window = button1)

 button2_canvas = canvas1.create_window( 105, 275,
									anchor = "nw",
									window = button2)

 button3_canvas = canvas1.create_window( 105, 340, anchor = "nw",
									window = button3)

 button_help_canvas = canvas1.create_window( 105, 410, anchor = "nw",
                                           window = button_help)

 button_option_canvas = canvas1.create_window( 229, 410, anchor = "nw",
                                           window = button_option)

 button_exit_canvas = canvas1.create_window( 105, 460, anchor = "nw",
                                           window = button_exit)
#Add the background sound
mixer.init()
mixer.music.load('sound/S4.wav')
mixer.music.play()

button()



# Execute tkinter
root.mainloop()

