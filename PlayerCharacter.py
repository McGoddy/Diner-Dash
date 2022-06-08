import arcade
import random

CHARACTER_SCALING = 3


# How fast to move, and how fast to run the animation

MOVEMENT_SPEED = 5

UPDATES_PER_FRAME = 5



# Constants used to track if the player is facing left or right

RIGHT_FACING = 0

LEFT_FACING = 1

UP_FACING = 0

DOWN_FACING = 1






def load_texture_pair(filename):

    """

    Load a texture pair, with the second being a mirror image.

    """

    return [

        arcade.load_texture(filename),

        arcade.load_texture(filename, flipped_horizontally=True)

    ]



class PlayerCharacter(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()


        # Default to face-right

        self.character_face_direction = RIGHT_FACING

        self.character_face_direction1 = UP_FACING


        # Used for flipping between image sequences

        self.cur_texture = 0



        self.scale = CHARACTER_SCALING



        # Adjust the collision box. Default includes too much empty space

        # side-to-side. Box is centered at sprite center, (0, 0)

        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]



        # --- Load Textures ---



        # Images from assets

        main_path = "Images/flo/flo"


        # Load textures for idle standing

        self.idle_texture_pair = load_texture_pair(f"{main_path}_resting.png")



        # Load textures for walking

        self.side_walk_textures = []

        for i in range(12):

            texture = load_texture_pair(f"{main_path}_walking_side_step{i+1}.png")

            self.side_walk_textures.append(texture)


        self.up_walk_textures = []

        for i in range(12):

            texture = load_texture_pair(f"{main_path}_walking_front_step{i+1}.png")

            self.up_walk_textures.append(texture)
            

    def update_animation(self, delta_time: float = 1 / 60):



        # Figure out if we need to flip face left or right

        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:

            self.character_face_direction = LEFT_FACING

        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:

            self.character_face_direction = RIGHT_FACING
            
        elif self.change_y < 0 and self.character_face_direction1 == UP_FACING:
    
            self.character_face_direction1 = DOWN_FACING
            
        elif self.change_y > 0 and self.character_face_direction1 == DOWN_FACING:
    
            self.character_face_direction1 = UP_FACING



        # Idle animation

        if self.change_x == 0 and self.change_y == 0:

            self.texture = self.idle_texture_pair[self.character_face_direction]

            return



        # Walking animation

        self.cur_texture += 1

        if self.cur_texture > 11 * UPDATES_PER_FRAME:

            self.cur_texture = 0

        frame = self.cur_texture // UPDATES_PER_FRAME

        direction1 = self.character_face_direction
        
        direction2 = self.character_face_direction1

        self.texture = self.side_walk_textures[frame][direction1]
        
        # self.texture = self.up_walk_textures[frame][direction2]
