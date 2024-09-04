import pygame

class SpriteSheet():
    def __init__(self,image):
        self.sheet = image

    def get_image(self,frame,width,height,scale,color,square_width,square_height,png = False):
     

        border = frame + 1
        image = pygame.Surface((width, height), pygame.SRCALPHA)  # Use SRCALPHA to handle transparency
        image.blit(self.sheet, (0, 0), ((frame * square_width) + 2 * border, square_height, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)  # Set the transparent color key
    
            
        return image
