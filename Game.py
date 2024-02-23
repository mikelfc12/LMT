import pygame, random
from pygame import *

SCREEN_SIZE = pygame.Rect((0, 0, 800, 640))
TILE_SIZE = 32 
GRAVITY = pygame.Vector2((0, 0.3))
LEVEL_NUM = 1
LEVEL_VER = 1

class CameraAwareLayeredUpdates(pygame.sprite.LayeredUpdates):
    def __init__(self, target, world_size):
        super().__init__()
        self.target = target
        self.cam = pygame.Vector2(0, 0)
        self.world_size = world_size
        if self.target:
            self.add(target)

        #Level
        #self.level_num = 1

    def update(self, *args):
        super().update(*args)
        if self.target:
            x = -self.target.rect.center[0] + SCREEN_SIZE.width/2
            y = -self.target.rect.center[1] + SCREEN_SIZE.height/2
            self.cam += (pygame.Vector2((x, y)) - self.cam) * 0.05
            self.cam.x = max(-(self.world_size.width-SCREEN_SIZE.width), min(0, self.cam.x))
            self.cam.y = max(-(self.world_size.height-SCREEN_SIZE.height), min(0, self.cam.y))

    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect.move(self.cam))
            if rec is init_rect:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty  
    
restart_tiles = pygame.sprite.Group()

def gameLevel(level_num):
    global LEVEL_NUM
    global LEVEL_VER
    # Level
    #level_num = 1

    #Tutorial 1
    tutorial1 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                   P",
        "P                             PP    P",
        "P                             EP    P",
        "P                    PPPPPPPPPPP    P",
        "P                                   P",
        "P                                   P",
        "P        x                          P",
        "P    PPPPPPPP                       P",
        "P                              x    P",
        "P                    R     PPPPPPP  P",
        "P                 PPPPPP            P",
        "P            x                      P",
        "P         PPPPPPP                   P",
        "P                        x          P",
        "P                     PPPPPP        P",
        "P    x                              P",
        "P   PPPPPPPPPPP                     P",
        "P                                   P",
        "P                 PPPPPPPPPPP       P",
        "P                                   P",
        "P     PPPPP                         P",
        "P                                   P",
        "P     C               PPPP          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level1.1
    level1V1 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                     P",
        "P                                     P",
        "P                                PP   P",
        "P                                EP   P",
        "P                       PPPPPPPPPPP   P",
        "P                                     P",
        "P                    PPPPPP           P",
        "P                                     P",
        "P                 PPPPPP              P",
        "P                                     P",
        "P              PPPPPP                 P",
        "P                                     P",
        "P           PPPPPP                    P",
        "P                                     P",
        "P         PPPPPP                      P",
        "P                                     P",
        "P      PPPPPP                         P",
        "P       R                             P",
        "P   PPPPPP                            P",
        "P                                     P",
        "PPPPPPP                               P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level1.2
    level1V2 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                     P",
        "P                                     P",
        "P                    PP               P",
        "P                    EP               P",
        "P           PPPPPPPPPPP               P",
        "P                                     P",
        "P    PPPPPP                           P",
        "P                                     P",
        "P PPPPPP                              P",
        "P                                     P",
        "P    PPPPPP                           P",
        "P                                     P",
        "P PPPPPP                              P",
        "P                                     P",
        "P   PPPPPP                            P",
        "P                                     P",
        "P PPPPPP                              P",
        "P     R                               P",
        "P   PPPPPP                            P",
        "P                                     P",
        "P PPPPPP                              P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level2.1
    level2V1 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P       X                             P",
        "P       PP                    PP      P",
        "P                             EP      P",
        "P                    PPPPPPPPPPP      P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P       PPPPP                         P",
        "P                          PPPPPP     P",
        "P                                     P",
        "P         PPPPPPP                     P",
        "P                                     P",
        "P   PP                                P",
        "P                                     P",
        "P   PPPPPP                            P",
        "P                                     P",
        "P                  PPPP               P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                         PPPP        P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level2.2
    level2V2 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P       X                             P",
        "P       PP                    PP      P",
        "P                             EP      P",
        "P                    PPPPPPPPPPP      P",
        "P                                     P",
        "P                 PPPPPPPPP           P",
        "P                                     P",
        "P                                     P",
        "P                          PPPPPP     P",
        "P                                     P",
        "P         PPPPPPP                     P",
        "P                                     P",
        "P   PP                                P",
        "P                                     P",
        "P   PPPPPP                            P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                                     P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level3.1
    level3V1 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                   PPP",
        "P                                   EPP",
        "P                          PPPPPPPPPPPP",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P               PPPPP                 P",
        "P                                     P",
        "P                          PPPPPP     P",
        "P                                     P",
        "P         PPPPPPP                     P",
        "P                                     P",
        "P   PP                                P",
        "P    x                                P",
        "P   PPPPPP                            P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                                     P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level3.2
    level3V2 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                   PPP",
        "P                          P        EPP",
        "P                          PPPPPPPPPPPP",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P               PPPPP                 P",
        "P                                     P",
        "P    PPPPPP                           P",
        "P                                     P",
        "PPPPPPPP                              P",
        "P                                     P",
        "P   PP                                P",
        "P                                     P",
        "P   PPPPPP                            P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                                     P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level4.1
    level4V1 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                     P",
        "P         PPP                         P",
        "P          E                          P",
        "P     PPPPPPPPPPP                     P",
        "P                                     P",
        "P                                     P",
        "P PPPPP                               P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P PPPP                                P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P PPP                                 P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                                     P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level4.2
    level4V2 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                     P",
        "P              PP                     P",
        "P              EP                     P",
        "P     PPPPPPPPPPP                     P",
        "P                                     P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                                     P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level5.1
    level5V1 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P       X                             P",
        "P       PP                    PP      P",
        "P                             EP      P",
        "P                    PPPPPPPPPPP      P",
        "P                                     P",
        "P                                     P",
        "P                                     P",
        "P       PP                            P",
        "P                          PPPPPP     P",
        "P                                     P",
        "P         PP                          P",
        "P                                     P",
        "P   PP                                P",
        "P                                     P",
        "P    PP                               P",
        "P                                     P",
        "P                    PP               P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                         PPPP        P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
    #Level5.2
    level5V2 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P       X                             P",
        "P       PP                    PP      P",
        "P                             EP      P",
        "P                    PPPPPPPPPPP      P",
        "P                                     P",
        "P                    PP               P",
        "P                                     P",
        "P                                     P",
        "P                          PP         P",
        "P                                     P",
        "P                         PP          P",
        "P                                     P",
        "P                 PP                  P",
        "P                                     P",
        "P                              PP     P",
        "P                                     P",
        "P                    PP               P",
        "P                                     P",
        "P PP                                  P",
        "P                                     P",
        "P                         PPPP        P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    
    

    if random.random() <= 0.5:
        LEVEL_VER = 1
    else:
        LEVEL_VER = 2
        
    if LEVEL_NUM == 1:
        return tutorial1
    elif LEVEL_NUM == 2 and LEVEL_VER == 1:
        return level1V1
    elif LEVEL_NUM == 2 and LEVEL_VER == 2:
        return level1V2
    elif LEVEL_NUM == 3 and LEVEL_VER == 1:
        return level2V1
    elif LEVEL_NUM == 3 and LEVEL_VER == 2:
        return level2V2
    elif LEVEL_NUM == 4 and LEVEL_VER == 1:
        return level3V1
    elif LEVEL_NUM == 4 and LEVEL_VER == 2:
        return level3V2
    elif LEVEL_NUM == 5 and LEVEL_VER == 1:
        return level4V1
    elif LEVEL_NUM == 5 and LEVEL_VER == 2:
        return level4V2
    elif LEVEL_NUM == 6 and LEVEL_VER == 1:
        return level5V1
    elif LEVEL_NUM == 6 and LEVEL_VER == 2:
        return level5V2
    else:
        return "END GAME"
            
def main(level, entities, restart_tiles):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()
    
    platforms = pygame.sprite.Group()
    pickups = pygame.sprite.Group()
    player = Player(platforms, restart_tiles, (TILE_SIZE, SCREEN_SIZE.height - TILE_SIZE), entities)
    level_width  = len(level[0])*TILE_SIZE
    level_height = len(level)*TILE_SIZE
    entities = CameraAwareLayeredUpdates(player, pygame.Rect(0, 0, level_width, level_height))
    
    # build the level
    x = y = 0
    for row in level:
        col_index=0
        for col in row:
            if col == "P":
                Platform((x, y), platforms, entities)
            if col == "x":
                PlatformX((x, y), platforms, entities)
            if col == "E":
                ExitBlock((x, y), platforms, entities)
            if col == "R":
                RestartTile((x, y), platforms, entities)
            if col == "C":
                Pickup((x, y), platforms, entities)
            x += TILE_SIZE
            col_index += 1
        y += TILE_SIZE
        x = 0
    
    while 1:

        for e in pygame.event.get():
            if e.type == QUIT: 
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        entities.update()
        pickups.update()
        screen.fill((0, 0, 0))
        entities.draw(screen)
        pickups.draw(screen)
        pygame.display.update()
        timer.tick(60)

def restart_level(entities, restart_tiles):
    global LEVEL_NUM
    global LEVEL_VER
    print("Restarting Level:", LEVEL_NUM)
    main(gameLevel(LEVEL_NUM), entities, restart_tiles)

class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        self.image = Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

class Player(Entity):
    def __init__(self, platforms, restart_tiles, pos, *groups):
        super().__init__(Color("#0000FF"), pos)
        # Load the player image
        self.image = pygame.image.load("player.png")    #NEW
        self.rect = self.image.get_rect()               #NEW
        self.rect.topleft = pos                         #NEW
        #Previous Code
        self.vel = pygame.Vector2((0, 0))
        self.onGround = False
        self.platforms = platforms
        self.restart_tiles = restart_tiles  # Include restart_tiles group
        self.speed = 8
        self.jump_strength = 10
        #self.level_num = 1

    def update_image(self):
        # Change the player's image based on the direction of movement
        if self.vel.x < 0:
            self.image = pygame.image.load("LEFT.png")
        elif self.vel.x > 0:
            self.image = pygame.image.load("RIGHT.png")

    def update(self):
        pressed = pygame.key.get_pressed()
        up = pressed[K_UP]
        left = pressed[K_LEFT]
        right = pressed[K_RIGHT]
        running = pressed[K_SPACE]
        
        if up:
            # only jump if on the ground
            if self.onGround: self.vel.y = -self.jump_strength
        if left:
            self.vel.x = -self.speed
        if right:
            self.vel.x = self.speed
        if running:
            self.vel.x *= 1.5
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.vel += GRAVITY
            # max falling speed
            if self.vel.y > 100: self.vel.y = 100
        #print(self.vel.y)
        if not(left or right):
            self.vel.x = 0
        # increment in x direction
        self.rect.left += self.vel.x
        # do x-axis collisions
        self.collide(self.vel.x, 0, self.platforms)
        # increment in y direction
        self.rect.top += self.vel.y
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.vel.y, self.platforms)
        # Check for restart tile collisions
        for r in pygame.sprite.spritecollide(self, self.restart_tiles, False):
            restart_level()
        # Update the player's image based on direction after updating the position
        self.update_image()

    def collide(self, xvel, yvel, platforms):
        global LEVEL_NUM
        global LEVEL_VER
        
        for p in platforms:                                     # Iterate through list of platforms
            if pygame.sprite.collide_rect(self, p):             # If there is a collision between the player and a platform
                if isinstance(p, ExitBlock):
                    #pause = True
                    #pygame.display.quit()

                    LEVEL_NUM += 1
                    print(LEVEL_NUM)

                    print(LEVEL_VER)

                    if gameLevel(LEVEL_NUM) != "END GAME":
                        main(gameLevel(LEVEL_NUM), entities, restart_tiles)
                        #Pause = False
                    else:
                        pygame.event.post(pygame.event.Event(QUIT))
                if isinstance(p, RestartTile):
                    restart_level(entities, restart_tiles)
                    
                if xvel > 0:                                    # If x speed is greater than 0, then we are moving right . . .
                    self.rect.right = p.rect.left
                    self.update_image()               # So the right bounding box becomes equal to the left bounding box of all platforms
                if xvel < 0:                                    # If x speed is less than 0, then we are moving left . . .
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.vel.y = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.vel.y = 0

class Platform(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#DDDDDD"), pos, *groups)
        # Add image
        self.image = pygame.image.load("Platform.png") #NEW
        self.rect = self.image.get_rect()               #NEW
        self.rect.topleft = pos                         #NEW

class PlatformX(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#E3F10A"), pos, *groups)
        # Add image
        self.image = pygame.image.load("PlatformX.png") #NEW
        self.rect = self.image.get_rect()               #NEW
        self.rect.topleft = pos                         #NEW

class ExitBlock(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#F10A1F"), pos, *groups)
        # Add image
        self.image = pygame.image.load("exitblock.png") #NEW
        self.rect = self.image.get_rect()               #NEW
        self.rect.topleft = pos                         #NEW

class RestartTile(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#F10A1F"), pos, *groups)
        # Add image
        self.image = pygame.image.load("Restart.png") #NEW
        self.rect = self.image.get_rect()             #NEW
        self.rect.topleft = pos                       #NEW

class Pickup(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#00FF00"), pos, *groups)
        # Add image
        self.image = pygame.image.load("Coin.png") #NEW
        self.rect = self.image.get_rect()             #NEW
        self.rect.topleft = pos                       #NEW

if __name__ == "__main__":
    restart_tiles = pygame.sprite.Group()
    entities = CameraAwareLayeredUpdates(None, None) 
    main(gameLevel(LEVEL_NUM), entities, restart_tiles)