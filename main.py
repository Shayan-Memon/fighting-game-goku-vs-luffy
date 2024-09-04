import pygame
from sprites import SpriteSheet

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


sprite_sheet_image = pygame.image.load("Assets/luffy.png").convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)

sprite_sheet_image_2 = pygame.image.load("Assets/goku_2.png").convert_alpha()
sprite_sheet_2 = SpriteSheet(sprite_sheet_image_2)
pygame.mixer.music.load("Assets/sounds/background.mp3")  # Update with the actual path
pygame.mixer.music.set_volume(0.1)

# Play the music indefinitely (-1 means loop indefinitely)
pygame.mixer.music.play(-1)



aura_image_2 = pygame.image.load("Assets/aura.png").convert_alpha()
aura_sheet_2 = SpriteSheet(aura_image_2)

hit_image_2 = pygame.image.load("Assets/hit.png").convert_alpha()
hit_sheet_2 = SpriteSheet(hit_image_2)

BG = (50, 50, 50)
sprite_transparency = (180, 180, 255)
sprite_transparency_2 = (0,255,80)
custom_font = pygame.font.Font("Assets/DeadKnight.otf", 36)  # Update with the actual path
Goku_font_surface = custom_font.render("GOKU", True, (255, 255, 255))  # Yellow color text
Luffy_font_surface = custom_font.render("LUFFY", True, (255, 255, 255))  # Yellow color text



pygame.display.set_caption('Shayan Games')






def set_sprites(animation_square,animation_steps,sprite_sheet,sprite_transparency,size):
    action_ = 0
    animation_list = []
    for animation in animation_steps:
        temporary_list = []
        step_counter = 0
        
        for _ in range(animation):
            image = sprite_sheet.get_image(step_counter, animation_square[action_][0], animation_square[action_][2], size, sprite_transparency, animation_square[action_][0], animation_square[action_][1])
            temporary_list.append(image)
            step_counter += 1
        action_ += 1
        animation_list.append(temporary_list)
    return animation_list


animation_steps = [4, 8, 3, 7, 7,5,15,4,4,3]
animation_square = [[112, 740, 117], [100, 863, 145], [93, 1014, 110], [120, 1130, 172], [304, 5542, 222],[195,6189,210],[304, 5542, 222], [139,7125,116],[155,8048,108],[161,8165,120]]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 130
frame = 0



#[160, 5096, 172]
animation_steps_2 = [6,8,4,6,9,3,4,7]
animation_square_2 = [[108, 884, 126],[106,1415,162],[167,1987,105],[94, 386, 162],[135,6076,134],[102,1581,117],[96,6375,129], [145,4175,159]]
action_2 = 0
last_update_2 = pygame.time.get_ticks()
last_update_3 = pygame.time.get_ticks()
animation_cooldown_2 = 130
frame_2 = 0

animation_list = set_sprites(animation_square,animation_steps,sprite_sheet,sprite_transparency,1)
animation_list_2 = set_sprites(animation_square_2,animation_steps_2,sprite_sheet_2,sprite_transparency_2,1)
aura_list = set_sprites([[207,0,390]],[4],aura_sheet_2,(0,0,0),1.4)

hit_list = set_sprites([[185,0,390]],[5],hit_sheet_2,(0,0,0),1.4)
aura_frame = 0
hit_frame = 0



# animation_list_2 = []
# animation_steps_2 = [4, 8, 3, 7, 7,5,15]
# animation_square_2 = [[112, 740, 117], [100, 863, 145], [93, 1014, 110], [120, 1130, 172], [304, 5542, 222],[195,6189,210],[304, 5542, 222]]
# action_2 = 0
# last_update_2 = pygame.time.get_ticks()
# animation_cooldown_2 = 130
# frame_2 = 0
# action__ = 0



# for animation in animation_steps_2:
#     temporary_list = []
#     step_counter = 0
    
#     for _ in range(animation):
#         image = sprite_sheet.get_image(step_counter, animation_square[action_][0], animation_square[action_][2], 1, sprite_transparency, animation_square[action_][0], animation_square[action_][1])
#         temporary_list.append(image)
#         step_counter += 1
#     action_ += 1
#     animation_list.append(temporary_list)
Run = True

# Define the constant bottom position for the sprites
constant_bottom_y = SCREEN_HEIGHT - 50  # Adjust this value as needed
gravity = 5
jump_strength = 60
flip = True
flip2 = False
attack11 = "Begin"
attack12 = False
transform_2 = "Begin"
attack21 = "Begin"
attack22 = "Begin"
fall_speed = 0
fall_speed2 = 0
jump_time = 0
rect_2 = pygame.Rect(0,0,0,0)
rect = pygame.Rect(0,0,0,0)
platform = pygame.Rect(0,450,SCREEN_WIDTH,10)
kamehameha_rect = pygame.Rect(0,0,0,0)
move_speed = 8

fly = False

def jump(fall_speed, move_y, rect):
    # Apply gravity to fall_speed
    fall_speed += gravity
    # Update move_y with the new fall_speed
    move_y += fall_speed

    # # Draw the platform (assuming you want to render it here)
    # pygame.draw.rect(screen, 'black', platform)
    
    # Check for collision with the platform
    if rect.colliderect(platform) and fall_speed > 0:
        # Position character on top of the platform
        move_y = platform.y - rect.height +10
        # Reset fall_speed to stop falling
        fall_speed = 0
    
    return fall_speed, move_y


def movement(keys,move_x,move_y,action,current_image,current_image_2):

    global frame,gravity,flip,attack11,attack12,action_2,transform_2,frame_2,attack21,move_x_2,move_y_2,flip2,fall_speed2,fall_speed,jump_time,rect_2,attack22

    flipped_image = current_image
    flipped_image_2 = current_image_2
    
    if keys[pygame.K_LEFT]:
        move_x-=move_speed
        action = 1
        flip = False

    elif keys[pygame.K_RIGHT]:
        move_x+=move_speed
        action = 1
        flip = True
       

    elif keys[pygame.K_DOWN]:
        action = 2
    elif keys[pygame.K_UP] and rect.colliderect(platform):
        action = 3
        fall_speed = -jump_strength
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Assets/sounds/jump.mp3'))
        

        

    elif keys[pygame.K_4] and keys[pygame.K_a] and not attack12:
        action = 6
        frame = 10
        attack12 = True
        
    elif keys[pygame.K_4] and action!=6 and not attack12:
        action = 4
   
        

    
    elif keys[pygame.K_5] and attack11 == "Begin":
        action = 5
        attack11 = "In-between"
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Assets/sounds/luffy punches1.mp3'))

    elif player_1_health <=0 and action !=8 and action!=9:
        action = 8

    elif attack11 != "In-between" and action!=3 and action!=0 and not attack12 and action!=8 and action!=9 :
        frame = 0
        action = 0

    



    

        # Apply gravity
    

    if keys[pygame.K_a]:
        action_2 = 2
        frame_2 = 0
        move_x_2-=move_speed
        flip2 = False

    elif keys[pygame.K_d]:
        action_2 = 2
        frame_2 = 0
        move_x_2+=move_speed
        flip2 = True

    elif keys[pygame.K_s]:
        action_2 = 5


   
        

    elif keys[pygame.K_w] and rect_2.colliderect(platform):
        action_2 = 1
        fall_speed2 = -jump_strength
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('Assets/sounds/jump.mp3'))


    elif transform_2 == "Begin":
        action_2 = 3
        transform_2 = "In-between"

        


    elif keys[pygame.K_k] and attack21 == "Begin":
        action_2 = 4
        attack21 = "In-between"
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('Assets/sounds/kamehameha1.mp3'))

    elif keys[pygame.K_g] and attack22 == "Begin":
        action_2 = 7
        attack22 = "In-between"
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('Assets/sounds/instant transmission.mp3'))
        

    

    elif (transform_2 != "In-between" and attack21  != "In-between" and attack22 != "In-between") and rect_2.colliderect(platform):
        action_2 = 0


    fall_speed2,move_y_2 = jump(fall_speed2,move_y_2,rect_2)
    fall_speed,move_y = jump(fall_speed,move_y,rect)
    

    if frame == animation_steps[action]-1 and action ==3:
        frame = 0
        action = 0


    if flip:
        flipped_image = pygame.transform.flip(current_image, True, False)

    if flip2:
        flipped_image_2 = pygame.transform.flip(current_image_2, True, False)

    
    return move_x,move_y,action,flipped_image,flipped_image_2


move_x = 200
move_y = 280

move_x_2 = 700
move_y_2 = 280

player_1_health = 300
player_2_health = 300

kame = 5 

background = 0

versus = 125

sha_logo = 125

while True:
    title_image = pygame.transform.scale(pygame.image.load("Assets/Title/Title ("+str(sha_logo)+").jpg"),(SCREEN_WIDTH,SCREEN_HEIGHT))

    screen.blit(title_image,(0,0))
    sha_logo-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

    if sha_logo == 0:
        break
    pygame.display.update()








while Run:
    
    kamehameha_image = pygame.transform.scale(pygame.image.load("Assets/kamehameha/"+str(kame)+".png"),(2000,800))

    versus_image = pygame.image.load("Assets/vs/vs ("+str(versus)+").jpg")

    # Set the black color to be transparent
    versus_image.set_colorkey((0, 0, 0))

    # Scale the image
    versus_image = pygame.transform.scale(versus_image, (400, 250))

    if background>6:
        background = 0
    else:
        background+=1

    background_image = pygame.transform.scale(pygame.image.load("Assets/background/"+str(background)+".png"),(SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # sprite_sheet = SpriteSheet(sprite_sheet_image)
    
    
    screen.blit(background_image,(0,0))
    screen.blit(Goku_font_surface, (750, 0))
    screen.blit(Luffy_font_surface, (100, 0))
    screen.blit(versus_image,(300,100))

    if versus!=1:
        versus-=1


   

    
    pygame.draw.rect(screen,'black',(30,30,300,15))
    pygame.draw.rect(screen,'black',(670,30,300,15))
    pygame.draw.rect(screen,'green',(30,30,player_1_health,15))
    pygame.draw.rect(screen,'black',(30,30,300,15),4)
   

    pygame.draw.rect(screen,'green',(670,30,player_2_health,15))
    pygame.draw.rect(screen,'black',(670,30,300,15),4)
    

    current_time = pygame.time.get_ticks()
    

    if action == 4 and frame == 0:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Assets/sounds/luffy gear4.mp3'))
        
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time

     

        
        # if frame < 3 and action == 9:
        #     action
        if frame >= len(animation_list[action]):
            frame = 0

  
            if action == 8:
                action = 9
                
            elif action == 9:
                frame = 2

            if action == 4:

                frame = 3
            elif action == 2:
                frame = 2

            elif action == 6:
                attack12 = False

            if action == 5:
                attack11 = "Begin"

            
                

            
   


    if current_time - last_update_2 >= animation_cooldown_2:
        frame_2 += 1
        aura_frame+=1
        last_update_2 = current_time

        if attack22 == 'In-between' and frame_2 == 1:
            move_x_2 = move_x+50


        if frame_2 >= len(animation_list_2[action_2]):
            frame_2 = 0
            if action_2 == 5:
                frame_2 = 2

            if action_2 == 3:
                transform_2 = "Done"

            if action_2 == 7:
                
                attack22 = "Begin"
            

        # if action_2 == 4 and frame_2 == :
        #     attack21 = False
                
            

        if aura_frame >= 4:
            aura_frame = 0

    # if action_2 == 4 and frame_2 == 0:
    #     frame_2 = 11
       

    # elif action_2 == 4 and frame_2 == 17:
    #     frame_2 = 2


    elif action_2 == 4 and frame_2 == 8:
        attack21 = "Begin"
        action_2 = 0
        frame_2 = 0
        kame = 5


    
        
        

    elif action_2 == 2:
        frame_2 = 1
  

    
    # elif action_2 == 2 and frame_2 ==0:
    #     frame_2 = 1

    # elif action_2 == 2:
    #     frame_2 = 2
            
            

    # Get the current image
    # print(frame)

    



    current_image = animation_list[action][frame]
    try:
        current_image_2 = animation_list_2[action_2][frame_2]

    except:
        frame_2 = 0
    aura_image_frame = aura_list[0][aura_frame]
    

    


    keys = pygame.key.get_pressed()
    move_x,move_y,action,current_image,current_image_2= movement(keys,move_x,move_y,action,current_image,current_image_2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

        if event.type == pygame.KEYDOWN:
            frame = 0
            if (transform_2 != "In-between" and attack21  != "In-between" and attack22 != "In-between"):
                frame_2 = 0

    rect_2 = current_image_2.get_rect()
    rect_2.x = move_x_2
    rect_2.y = move_y_2

    rect = current_image.get_rect()
    rect.x = move_x
    rect.y = move_y

    # Calculate position to align the bottom of the image and center horizontally
    image_rect = current_image.get_rect()
    image_rect.midbottom = (animation_square[action][0]/2, constant_bottom_y)

    # Adjust the x-coordinate to center the sprite based on its width
    centered_x = (animation_square[action][0]/2 - image_rect.width) // 2


    screen.blit(current_image_2, rect_2)
    # Blit the current image at the calculated position
    screen.blit(current_image, rect)

    # pygame.draw.rect(screen,'black',kamehameha_rect)

    if attack21 == "In-between" and frame_2 >3:
        
        if kame>=17:
            kame = 16

        

        

  
        if not flip2:
            kamehameha_image = pygame.transform.flip(kamehameha_image, True, False)
        if current_time - last_update_3 >= 0:
            last_update_3 = current_time
            kame+=1

        kamehameha_rect.width = 900
        kamehameha_rect.height = 50

        if flip2:
            kamehameha_rect.x = move_x_2+100

        else:
            kamehameha_rect.x = move_x_2-kamehameha_rect.width
        kamehameha_rect.y = move_y_2+30
        
        screen.blit(kamehameha_image,(-950+move_x_2,-350+ move_y_2))


    
    transparency = 200  # This value can be adjusted between 0 and 255
    aura_image_frame.set_alpha(transparency)

    if transform_2 == "In-between" or attack21 == "In-between":
        # Blit the aura image frame with transparency onto the screen
        screen.blit(aura_image_frame, (move_x_2 - 95, move_y_2 - 125))



    if attack11 == 'In-between' and rect.colliderect(rect_2):
        player_2_health -= 1
        hit_frame += 1
        action_2 = 6

        if hit_frame > 4:
            hit_frame = 0
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('Assets/sounds/goku-beat.mp3'))

        hit_image_frame = hit_list[0][hit_frame]

        # Calculate the intersection rectangle
        intersection_rect = rect.clip(rect_2)

        # Get the top-left corner of the intersection rectangle
        impact_point = (intersection_rect.x-120, intersection_rect.y-120)

        # Blit the hit image frame at the point of impact
        screen.blit(hit_image_frame, impact_point)


    elif (attack22 == 'In-between' or attack21 == "In-between") and (rect.colliderect(rect_2) or (kamehameha_rect.colliderect(rect) and kame>5)):
        player_1_health -= 4
        hit_frame += 1
        action = 7
        if attack22 == "In-between":
            flip2 = False

            if frame_2 == 3:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('Assets/sounds/goku kick.mp3'))
        elif attack21 == "In-between":
            player_1_health -=6



        if hit_frame > 4:
            hit_frame = 0

        hit_image_frame = hit_list[0][hit_frame]

        # Calculate the intersection rectangle
        intersection_rect = rect.clip(rect_2)

        # Get the top-left corner of the intersection rectangle
        impact_point = (intersection_rect.x-120, intersection_rect.y-120)

        # Blit the hit image frame at the point of impact
        screen.blit(hit_image_frame, impact_point)
        


    
            

        

    
    pygame.display.update()
    # pygame.time.Clock().tick(70)

pygame.quit()
