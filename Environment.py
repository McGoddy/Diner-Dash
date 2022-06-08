import time
import arcade



SCREEN_WIDTH = 1024
SCREEN_HEIGHT =600
SCREEN_TITLE = "Group8 environment restaurant"
MUSIC_VOLUME = 0.5

class Environment(arcade.Window):
    #Environment class
    
    def __init__(self):
        #Initializer or constructor
        super().__init__()
        self.background = None
        arcade.set_background_color(arcade.color.AMAZON)
        
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None
        
        
    
    
    
    
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
        time.sleep(0.03)
    
    
    def advance_song(self):
            #Advance the pointer to the next song
        self.current_song_index += 1
        if self.current_song_index >= len(self.music_list):
            self.current_song_index = 0
    
    
   
    
        
    def setup(self):
        #set up the game here.
        self.background = arcade.load_texture("Images\RealB.png")
        #list of music
        self.music_list = ["sound\music2.wav", "sound\S4.wav", "sound\S2.ogg", "sound\S1.wav"]
        #Array index of what to play
        self.current_song_index = 0
        #play the song
        self.play_song()
    
    
    def on_draw(self):
            
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
    def on_update(self, dt):
        position = self.music.get_stream_position(self.current_player)
        # The position pointer is reset to 0 right after we finish the song.
        # This makes it very difficult to figure out if we just started playing
        # or if we are doing playing.
        if position == 0.0:
            self.advance_song()
            self.play_song()    






