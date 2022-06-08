import arcade



class Customers(arcade.Sprite):
    #Customers sprite
    
    def __init__(self, model, scale = 1):
        #Customers constructor
        
        #attributes for models
        self.model = model
        
        #Image to use for customers 
        self.image_file_name = f"Images\{self.model}.png"
        
        #Call the parent
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")