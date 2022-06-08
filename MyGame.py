import random
import arcade
import time
import arcade.gui
from Customers import Customers
from Environment import Environment

#from Environment import Environment








#setting up the title and size
SCREEN_WIDTH = 800
SCREEN_HEIGHT =600
SCREEN_TITLE = "Group 8 environment"
#Constants for sizing
CUSTOMER_SCALE = 0.20
MUSIC_VOLUME = 0.5

#CUSTOMERS PROPERTIES
CUSTOMER_MODEL = ["customers", "customers", "customers"]

#How big are the customers
CUSTOMER_WIDTH = 120 * CUSTOMER_SCALE
CUSTOMER_HEIGHT = 120 * CUSTOMER_SCALE

#How big is the mat we'll place the customers on?
MAT_PERCENT_OVERSIZE = 5.7
MAT_HEIGHT = int(MAT_PERCENT_OVERSIZE * CUSTOMER_HEIGHT)
MAT_WIDTH = int(MAT_PERCENT_OVERSIZE * CUSTOMER_WIDTH)




#How much space do we leave as agap between the mats?
#Done as a percent of the mat size
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

#The y of the bottom row (2 piles)
BOTTOM_Y = MAT_HEIGHT/ 2 + MAT_WIDTH*VERTICAL_MARGIN_PERCENT - 50

#The X of where to start putting things on the left side
START_X = MAT_WIDTH/2 + MAT_WIDTH*HORIZONTAL_MARGIN_PERCENT-5


#The y(position of the table) of the top row
TOP_Y = SCREEN_HEIGHT-MAT_HEIGHT/2 - MAT_HEIGHT*VERTICAL_MARGIN_PERCENT

# The Y of the middle row (7 piles)
MIDDLE_Y = TOP_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# How far apart each pile goes
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT


#tables scale
TABLE_SCALE = 0.3



class MyGame(arcade.Window):
    #Main application class
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        #Sprite list with all the customers, no matter what pile they are in.
        self.Customer_list = None
        
        self.tables_list = []
        self.tables_seated = []
        self.features_list = []
        
        self.total_time = 0.0
        self.seconds = 0.0
        
        self.background = None
        arcade.set_background_color(arcade.color.AMAZON)
        
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None
        
        
        
        #List of customers we are dragging with the mouse
        self.held_Customers = None
        
        #The Original location of the Customers we are dragging with the mouse in case
        #they have to go back
        self.held_Customers_original_position = None
        
        #Sprite list with all the tables that customers lay on
        self.pile_mat_list = None
        
        self.counter = None
        self.board = None
        self.trashCan = None
        
        
    def advance_song(self):
        #Advance the pointer to the next song
        self.current_song_index += 1
        if self.current_song_index >= len(self.music_list):
            self.current_song_index = 0
    
    
    def play_song(self):
        #play the song
        if self.music:
            self.music.stop()
        
        #play the next song
        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(MUSIC_VOLUME)
        #Now, setting up a quick delay. If we don't do this,
        #our elapsed time will be 0
        #and on_update will think the music is over and start the next
        #song befor starting this one
        #time.sleep(0.03)
    
        
    def setup(self):
        
        #setup the game here. Call this function to restart the game
       
        #set up the game here.
        self.background = arcade.load_texture("Images\BA.png")
        #list of music
        self.music_list = ["sound\music2.wav", "sound\S4.wav", "sound\S2.ogg", "sound\S1.wav"]
        #Array index of what to play
        self.current_song_index = 0
        #play the song
        self.play_song()
        #list of tables
        self.tables_list = arcade.SpriteList()
        self.tables_seated = arcade.SpriteList()
        
        #list of features 
        self.features_list = arcade.SpriteList()
        
        
        #Create the counter
        self.counter = arcade.Sprite("Images\counter.png", 1.0)
        self.counter.center_x = 460
        self.counter.center_y =410
        self.features_list.append(self.counter)
        
        #Create the trashCan
        self.trashCan = arcade.Sprite("Images\Trash.png", 0.1)
        self.trashCan.center_x = 700
        self.trashCan.center_y = 410
        self.features_list.append(self.trashCan)
        
        #create the board
        self.board = arcade.Sprite("Images\Board.png", 0.5)
        self.board.center_x =350
        self.board.center_y =450
        self.features_list.append(self.board)
        
        
        #create the tables instance 1
        self.table1 = arcade.Sprite("Images\Table.png", TABLE_SCALE)
        self.table1.center_x = 370 
        self.table1.center_y = 220
        self.tables_list.append(self.table1)
        
        
        #table2
        self.table2 = arcade.Sprite("Images\Table.png", TABLE_SCALE)
        self.table2.center_x = 650
        self.table2.center_y = 220
        self.tables_list.append(self.table2)
       
        
        #create the tables instance3
        self.table3 = arcade.Sprite("Images\Table.png", TABLE_SCALE)
        self.table3.center_x = 370 
        self.table3.center_y = 100
        self.tables_list.append(self.table3)
       
        
        self.table4 = arcade.Sprite("Images\Table.png", TABLE_SCALE)
        self.table4.center_x = 650
        self.table4.center_y = 100
        self.tables_list.append(self.table4)
        
        
        
        
        
        
        
        #List of cards we are dragging with the mouse
        self.held_Customers = []
        
        #The Original location of Customers we are dragging with the mouse in case
        #They have to go back
        self.held_Customers_original_position = []
        
        
        #---Create the tables customers go on.
        
        #sprite list with all the tables lay on
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        self.table_mat_list: arcade.SpriteList= arcade.SpriteList()
        
        #Create the mats for the bottom face down and face up piles
        #pile = arcade.Sprite("images\NApe.png", image_x =MAT_WIDTH+30, image_y =MAT_HEIGHT+150)
        pile = arcade.SpriteSolidColor(MAT_WIDTH+30, MAT_HEIGHT+150, arcade.csscolor.BROWN)
        pile.position = START_X + X_SPACING -150, BOTTOM_Y+113
        
        self.pile_mat_list.append(pile)
        
             
        
        #Sprite list with all the Customers, no matter what pile they are in
        
        self.Customer_list = arcade.SpriteList()
        
        self.add_customers()
           
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # Accumulate the total time
        self.total_time += delta_time

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        self.seconds = int(self.total_time) % 60

        # Calculate 100s of a second
        seconds_100s = int((self.total_time - self.seconds) * 100)

        # Use string formatting to create a new text string for our timer
           
                
    def add_customers(self):
        Add = 0
        tmp = 0
        
        
        #Create every customers
        for tmp in CUSTOMER_MODEL:
         pp = self.seconds %10
         if pp == 0:
            tmp = random.choice(CUSTOMER_MODEL)
            customers = Customers.Customers(tmp, CUSTOMER_SCALE)
            customers.position = START_X, BOTTOM_Y + Add
            self.Customer_list.append(customers)
            Add += 110
            
                              
   
        
    def pull_to_top(self, customer: arcade.Sprite):
        """Pull the customer to top of rendering order(last to render, looks on-top)"""
        
        #Remove, and append to the end
        self.Customer_list.remove(customer)
        self.Customer_list.append(customer)
        
    def on_mouse_press(self, x, y, button, key_modifiers):
        #called when you press a button
        
        #Get list of customers we've clicked on
        
        customers = arcade.get_sprites_at_point((x,y), self.Customer_list)
        
        #Have we clicked on a customer?
        if len(customers)> 0 :
            
            #Might be a stack of customers, get one
            first_customer = customers[-1]
            
            
            #All others cases, grab  the customers we are clicking on
            self.held_Customers = [first_customer]
            
            #Save the position
            self.held_Customers_original_position = [self.held_Customers[0].position]
            
            #put on top 
            self.pull_to_top(self.held_Customers[0])
    
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        #User moves mouse
        for customers in self.held_Customers:
            customers.center_x += dx
            customers.center_y += dy
            
    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        #called when the user presses a mouse button
        
        #If we don't have any customers, who cares
        if len(self.held_Customers) == 0:
            return
        
        #find the closest pile, in case we are in contact with more than one
        table, distance = arcade.get_closest_sprite(self.held_Customers[0], self.tables_list) 
        reset_position = True
        
        
        customer_split = self.held_Customers[0]
        
        
        #See if we are in contact with the closest pile
        if arcade.check_for_collision(self.held_Customers[0], table):
            
        
           # For customers seated  || Identify the table where we are dropping the customer
         hit_list = arcade.check_for_collision_with_list(customer_split, self.tables_list)
         
         # deleting the empty table and replace it with Table seated
         
         for stand in hit_list:
             
             if stand == self.tables_list[0]:
                 
              stand.remove_from_sprite_lists()
              customer_split.remove_from_sprite_lists()
              stand = arcade.Sprite("Images\seated.png", TABLE_SCALE)
              stand.center_x = table.center_x
              stand.center_y = table.center_y
              self.tables_seated.append(stand)
              # removing the customer that is saved in the held_Customers list to avoid error
              self.held_Customers.pop(0)
              
            
             
             elif stand == self.tables_list[1]:
                 
              stand.remove_from_sprite_lists()
              customer_split.remove_from_sprite_lists()
              stand = arcade.Sprite("Images\seated1.png", TABLE_SCALE)
              stand.center_x = table.center_x
              stand.center_y = table.center_y
              self.tables_seated.append(stand)
              # removing the customer that is saved in the held_Customers list to avoid error
              self.held_Customers.pop(0)
              
              
             elif stand == self.tables_list[2]:
                 
              stand.remove_from_sprite_lists()
              customer_split.remove_from_sprite_lists()
              stand = arcade.Sprite("Images\seated2.png", TABLE_SCALE)
              stand.center_x = table.center_x
              stand.center_y = table.center_y
              self.tables_seated.append(stand)
              # removing the customer that is saved in the held_Customers list to avoid error
              self.held_Customers.pop(0)
             
              
             if stand == self.tables_list[3]:
                 
              stand.remove_from_sprite_lists()
              customer_split.remove_from_sprite_lists()
              stand = arcade.Sprite("Images\seated3.png", TABLE_SCALE)
              stand.center_x = table.center_x
              stand.center_y = table.center_y
              self.tables_seated.append(stand)
              # removing the customer that is saved in the held_Customers list to avoid error
              self.held_Customers.pop(0)
             
        if reset_position == True:
            #Where-ever we were dropped, it wasn't valid. Reset customer's position
            #to its original spot
            for table_index, customers in enumerate(self.held_Customers):
                customers.position = self.held_Customers_original_position[table_index]
                   
        for i, dropped_customers in enumerate(self.held_Customers):
            #Move customers to proper position
            dropped_customers = table.center_x, table.center_y
            
        #Success, don't reset position of customers
        reset_position = False
            
        
        #release on top play pile? And only one card held?
        
        
        
        #We are no longer holding customers
        self.held_Customers = []
        
    def on_draw(self):
            #Render the screen
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        
        self.tables_list.draw()
        
        #self.manager.draw()
        
        #feature
        
        self.features_list.draw()
        
        
        #Draw the mats the cards go on to
        self.pile_mat_list.draw()
        
        #Draw
        self.Customer_list.draw()
        
        #table seated
        self.tables_seated.draw()
                    
    
def main():
        #main function
        window = MyGame()
        window.setup()
        arcade.run()
        