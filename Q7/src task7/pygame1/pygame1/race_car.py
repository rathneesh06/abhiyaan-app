# Modules
import pygame
import time
import random

# Initiate pygame. Always needed
# pygame.init() 
# mixer.init()
# mixer.music.load('Initial D - Deja Vu.mp3')
# mixer.music.set_volume(0.7)
# mixer.music.play()
# Clock
clock = pygame.time.Clock()

# RGB Color
BLACK = (0,0,0)
RED = (255,0,0)

# window with size of 500 x 400 pixels
wn_width = 500
wn_height = 400
wn = pygame.display.set_mode((wn_width,wn_height))
pygame.display.set_caption('Race car with road block')

# image
bg = pygame.image.load('/home/vboxuser/task7/images/3lane.png')
carimg = pygame.image.load('/home/vboxuser/task7/images/porsche.png')
DEFAULT_IMAGE_SIZE=(wn_width,wn_height)
bg = pygame.transform.scale(bg, DEFAULT_IMAGE_SIZE)
CAR_SIZE=(60,100)
carimg = pygame.transform.scale(carimg, CAR_SIZE)

# boundary
west_b = 100
east_b = 380

class Block:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speedy = 1
        self.dodged = 0
        
        
    def update(self):
        self.y = self.y + self.speedy
       # check boundary (block)
        if self.y > wn_height:
           self.y = 0 - self.height
           self.x = random.randrange(west_b,east_b-self.width)

           self.dodged = self.dodged + 1

    def draw(self,wn):
        pygame.draw.rect(wn, RED, [self.x, self.y, self.width, self.height])
                  
class Player:
    def __init__(self):
        self.image = carimg
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.rect = self.image.get_rect()
        self.rect.x = int(wn_width * 0.5)
        self.rect.y = int(wn_height * 0.5)
        self.is_moving=False
        self.speedx = 0
        
    def start_moving(self):
        self.is_moving=True
        
    def stop_moving(self):
        self.is_moving=False
            
    def update(self):
                
        self.rect.x = self.rect.x + self.speedx        

       # check boundary (west)
        if  self.rect.left < west_b:
           self.rect.left = west_b
       # check boundary (east)
        if  self.rect.right > east_b:
           self.rect.right = east_b
        if  self.is_moving:
           self.rect.x+=self.speedx
           
# Functions


def scan_obstacles(bg_image, car_rect):
    detection_range = 400
    detection_area_rect = car_rect.copy()

    # Adjust detection area based on car's direction (assuming car_direction is always "up")
    detection_area_rect.y -= detection_range
    detection_area_rect.height += detection_range

    # Ensure the detection area stays within the background image
    detection_area_rect = detection_area_rect.clip(bg_image.get_rect())

    # Extract detection area from background image
    detection_area = bg_image.subsurface(detection_area_rect)

    # Define the range for the red color (adjust as needed)
    RED_RANGE = (200, 255)  # Minimum and maximum red values

    # Loop through each pixel in the detection area
    for x in range(detection_area.get_width()):
        for y in range(detection_area.get_height()):
            pixel_color = detection_area.get_at((x, y))
            # Check if the pixel color is within the red range
            if RED_RANGE[0] <= pixel_color[0] <= RED_RANGE[1]:  # Check red component
                # If a red pixel is found, return True
                return True

    # If no red pixel is found, return False
    return False



    
# def game function 
def game_loop():
    
    block_width = 80
    block_height = 20
    block_x = random.randrange(west_b, east_b - block_width)
    block_y = -100

    player = Player()
    block = Block(block_x,block_y,block_width,block_height)
    obstacle_rect = pygame.Rect(0, 0, block_width, block_height)
    while True:
       obstacles_detected = scan_obstacles(bg, player.rect)
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
         if obstacles_detected ==True:
            player.start_moving()
            
    # Move with speed 5 in the x-direction until no longer in front of the obstacle
            if player.rect.y > obstacle_rect.y:  # If car is below obstacle
               if player.rect.centerx<obstacle_rect.centerx:  # If car is to the left of obstacle
                  player.rect.speedx += 5  # Move player 5 pixels to the right
  # Move right
               elif player.rect.centerx < obstacle_rect.centerx:  # If car is to the right of obstacle
                  player.rect.speedx -= 5  # Move player 5 pixels up
  # Move left
            else:
               player.speedx = 0  # Stop moving in x-direction
         else:
            player.stop_moving()
            player.speedx = 0  # Reset speed if no obstacles


 
         player.update()
         block.update()

       player.update()
       block.update()

       wn.blit(bg,(0,0)) # (0,0)location on the wn
       wn.blit(player.image,(player.rect.x,player.rect.y))
       block.draw(wn)
       
       

##     
          
       pygame.display.update()
       clock.tick(60) 
       


### pygame quit
game_loop()
pygame.quit()
quit()
	

