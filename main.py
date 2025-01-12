import pygame
import random
import time
from background import Background
from human import Human
from food import Food


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)

# set up variables for the display
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 750
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

background = Background(0, 0)
fish = Human(0, 0)
food1 = Food(500, 500)
food2 = Food(1000, 1000)
food3 = Food(1000, 1000)
food4 = Food(1000, 1000)
food5 = Food(1000, 1000)
food6 = Food(1000, 1000)
food7 = Food(1000, 1000)
food8 = Food(1000, 1000)
food9 = Food(1000, 1000)

noteaten1 = True
noteaten2 = True
noteaten3 = True
noteaten4 = True
noteaten5 = True
noteaten6 = True
noteaten7 = True
noteaten8 = True
noteaten9 = True

lane1 = "empty"
lane2 = "empty"
lane3 = "empty"
lane4 = "empty"
lane5 = "empty"
lane6 = "empty"
lane7 = "empty"
lane8 = "empty"
lane9 = "empty"

points = 100
respawn = False
points_gotten1 = False
points_gotten2 = False
points_gotten3 = False
points_gotten4 = False
points_gotten5 = False
points_gotten6 = False
points_gotten7 = False
points_gotten8 = False
points_gotten9 = False


playbutton = pygame.image.load("playbutton.png")
playbutton_size = playbutton.get_size()
playbutton_scale_size = (playbutton_size[0] * .1, playbutton_size[1] * .1)
playbutton = pygame.transform.scale(playbutton, playbutton_scale_size)
playbutton_size = playbutton.get_size()
playbutton_rect = pygame.Rect(325, 350, playbutton_size[0], playbutton_size[1])

playagainbutton = pygame.image.load("playagainbutton.png")
playagainbutton_size = playagainbutton.get_size()
playagainbutton_scale_size = (playagainbutton_size[0] * .5, playagainbutton_size[1] * .5)
playagainbutton = pygame.transform.scale(playagainbutton, playagainbutton_scale_size)
playagainbutton_size = playagainbutton.get_size()
playagainbutton_rect = pygame.Rect(475, 300, playagainbutton_size[0], playagainbutton_size[1])

welcome = pygame.image.load("welcome.png")
welcome = pygame.transform.scale(welcome, (750, 500))

end = pygame.image.load("endscreen.png")
end = pygame.transform.scale(end, (750, 500))

display_points = my_font.render("Points:" + str(points), True, (255, 255, 255))
f = Human(40, 30)

run = True
intro_screen = True
game_screen = True
end_screen = False

def change_trash(lane):
    random_direction = random.randint(1, 2)
    foodobj = eval('food' + str(lane))
    foodobj.direction = random_direction
    trashnum = random.randint(1, 9)
    if foodobj.direction == 1:
        foodobj.image = pygame.image.load("food" + str(trashnum) + ".png")
    else:
        foodobj.image = pygame.image.load("food" + str(trashnum) + "left.png")

    foodobj.image_size = foodobj.image.get_size()
    percent_scale_size = random.randint(1, 100)/200
    scale_size = (foodobj.image_size[0] * percent_scale_size, foodobj.image_size[1] * percent_scale_size)
    foodobj.image = pygame.transform.scale(foodobj.image, scale_size)
    foodobj.image_size = foodobj.image.get_size()
    foodobj.rect = pygame.Rect(foodobj.x, foodobj.y, foodobj.image_size[0], foodobj.image_size[1])


def check_food_eaten():
    food_eaten_list = []
    for i in range(9):
        food_num = 'food' + str(i+1)
        if fish.rect.colliderect(eval(food_num).rect):
            overlap = fish.rect.clip(eval(food_num).rect)
            if eval(food_num).check_real_collision(overlap):
                food_eaten_list.append(str(i+1))
                eval(food_num).x = 1000
                eval(food_num).y = 1000
    return food_eaten_list


def move_trash(lane):
    food_name = 'food' + str(lane)
    eval(food_name).x = 1000
    eval(food_name).y = 1000


def check_outbounds():
    food_outbounds_list = []
    for i in range(9):
        food_lane_num = 'food' + str(i+1)
        if (eval(food_lane_num).x > 800 or eval(food_lane_num).x < -50):
            food_outbounds_list.append(i+1)
    return food_outbounds_list

while run == True:

    while intro_screen:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
                intro_screen = False
                game_screen = False
                end_screen = False

            if event.type == pygame.MOUSEBUTTONDOWN and playbutton_rect.collidepoint(event.pos):
                intro_screen = False
                game_screen = True

        screen.blit(welcome, (0, 0))
        screen.blit(playbutton, (325, 350))
        pygame.display.update()

    while game_screen:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
                intro_screen = False
                game_screen = False
                end_screen = False

        keys = pygame.key.get_pressed()  # checking pressed keys

        if keys[pygame.K_d]:
            fish.move_direction("right")

        if keys[pygame.K_a]:
            fish.move_direction("left")

        if keys[pygame.K_w]:
            fish.move_direction("up")

        if keys[pygame.K_s]:
            fish.move_direction("down")

        if respawn == True:
            food1 = Food(500, 500)
            food2 = Food(1000, 1000)
            food3 = Food(1000, 1000)
            food4 = Food(1000, 1000)
            food5 = Food(1000, 1000)
            food6 = Food(1000, 1000)
            food7 = Food(1000, 1000)
            food8 = Food(1000, 1000)
            food9 = Food(1000, 1000)
            respawn = False

        for i in range(9):
            lane_name = 'lane' + str(i+1)
            if locals()[lane_name] == "empty":
                fish_spawn = random.randint(1, 500)
                if (fish_spawn == 500):
                    locals()[lane_name] = "full"
                    change_trash(i + 1)
                    food_name = eval('food' + str(i+1))
                    noteatenname = 'noteaten' + str(i+1)
                    locals()[noteatenname] = True
                    if food_name.direction == 1:
                        food_name.x = -20
                        food_name.y = 50*(i)
                    else:
                        food_name.x = 750
                        food_name.y = 50*(i)

        fish_eaten = check_food_eaten()
        if len(fish_eaten) > 0:
            for i in range(len(fish_eaten)):
                fish_obj = eval('food' + str(fish_eaten[i]))
                fish_points = (fish_obj.image_size[0] + fish_obj.image_size[1])
                if points < fish_points*1.5:
                    end_screen = True
                    game_screen = False
                if points > fish_points and locals()['points_gotten' + str(fish_eaten[i])] == False:
                    points = points + fish_points/3
                    locals()['points_gotten' + str(fish_eaten[i])] = True
                    points = round(points, 2)
                    lane_eaten = 'noteaten' + str(fish_eaten[i])
                    locals()[lane_eaten] = False
                    num_lane = 'lane' + str(fish_eaten[i])
                    locals()[num_lane] = "empty"
                    move_trash(fish_eaten[i])

        out_of_screen = check_outbounds()
        for food in out_of_screen:
            lanename = 'lane' + str(food)
            locals()[lanename] = "empty"

        screen.blit(background.image, (0, 0))
        screen.blit(fish.image, fish.rect)
        display_points = my_font.render("Points:" + str(points), True, (255, 255, 255))
        screen.blit(display_points, (600, 0))

        for i in range(9):
            lanename = locals()['lane' + str(i+1)]
            noteatenname = locals()['noteaten' + str(i+1)]
            foodobj = eval('food' + str(i+1))
            if lanename == "full" and noteatenname == True:
                locals()['points_gotten' + str(i+1)] = False
                screen.blit(foodobj.image, foodobj.rect)
                foodobj.move()

        pygame.display.update()

    while end_screen:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
                intro_screen = False
                game_screen = False
                end_screen = False
            if event.type == pygame.MOUSEBUTTONDOWN and playagainbutton_rect.collidepoint(event.pos):
                game_screen = True
                end_screen = False
                points = 100
                respawn = True

        screen.blit(end, (0, 0))
        screen.blit(playagainbutton, (475, 300))

        pygame.display.update()



