
import arcade
import random
from PlayerCharacter import PlayerCharacter
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "DINER DASH"

CHARACTER_SCALING = 3

TILE_SCALING = 0.5
COUNTER_SCALING = 1
TRASH_SCALING = 0.5


# How fast to move, and how fast to run the animation

MOVEMENT_SPEED = 5

UPDATES_PER_FRAME = 5

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Set up the game and initialize the variables. """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Background image will be stored in this variable
        self.background = None

        self.counter_list = None   
        self.table_list = None  
        self.trash_list = None   
        
        # Sprite lists
        self.player_list = None

        # Set up the player
        self.score = 0
        self.player = None

    def setup(self):
        
        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        # Image from:
        # https://wallpaper-gallery.net/single/free-background-images/free-background-images-22.html
        self.background = arcade.load_texture("Images/background.png")

        self.counter_list = arcade.SpriteList() 
        self.table_list = arcade.SpriteList()
        self.trash_list = arcade.SpriteList()       
        
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player = PlayerCharacter()

        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = 1

        self.player_list.append(self.player)
        
        coordinate_list = [[400, 200], [400, 100], [600, 100], [600, 200]]
        
        for coordinate in coordinate_list:
            counter = arcade.Sprite("Images/table.png", TILE_SCALING)
            
            counter.position = coordinate
            self.counter_list.append(counter)
            
        coordinate_list2 = [[480, 400]]
        
        for coordinate2 in coordinate_list2:
            table = arcade.Sprite("Images/counter.png", COUNTER_SCALING)
            
            table.position = coordinate2
            self.table_list.append(table)
            
            
        coordinate_list3 = [[700, 400]]
        
        for coordinate3 in coordinate_list3:
            trash = arcade.Sprite("Images/trash_can.png", COUNTER_SCALING)
            
            trash.position = coordinate3
            self.trash_list.append(trash)
        # Set the background color
       # arcade.set_background_color(arcade.color.AMAZON)
       
      

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        
        
        
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Draw all the sprites.
      #  self.coin_list.draw()
        self.player_list.draw()
        self.counter_list.draw()
        self.table_list.draw()
        self.trash_list.draw()
        
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0 
    
    def on_mouse_press(self, x, y, button, modifiers):
            """Called whenever the left mouse button is pressed."""
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.player.change_x = x
                self.player.change_y = y
                
    def on_mouse_release(self, x, y, button, modifiers):
            """Called whenever the left mouse button is pressed."""
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.player.change_x = 0
                self.player.change_y = 0
                

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player_list.update()


        # Update the players animation

        self.player_list.update_animation()


        # Generate a list of all sprites that collided with the player.
      
        # Loop through each colliding sprite, remove it, and add to the score.
       

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()