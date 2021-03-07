from sys import exit
from random import choice, random
from math import log
import pygame


# DEFINE COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLDEN = (255, 215, 0)


# DEFINE TILES
A = 0 # Agent
G = 1 # Ground
W = 2 # Wall
E = 3 # Exit

# Link a tile to its color
TileImage = {A : pygame.image.load("character_grass.jpg"),
             G : pygame.image.load("grass.jpg"),
             W : pygame.image.load("brick.jpg"),
             E : pygame.image.load("victory_grass.jpg")
             }


# DEFINE MAPS
def map_very_easy():
  return [[G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, E],
          ]

def map_easy():
  return [[G, G, G, G, W, W, W, W, W, W],
          [G, G, G, G, G, W, W, W, W, W],
          [G, G, G, G, G, G, W, W, W, W],
          [G, G, G, G, G, G, G, W, W, W],
          [W, G, G, G, G, G, G, G, W, W],
          [W, W, G, G, G, G, G, G, G, W],
          [W, W, W, G, G, G, G, G, G, G],
          [W, W, W, W, G, G, G, G, G, G],
          [W, W, W, W, W, G, G, G, G, G],
          [W, W, W, W, W, W, G, G, G, E],
          ]

def map_medium():
  return [[G, G, G, G, G, W, W, W, W, W],
          [G, G, G, G, G, W, G, G, G, G],
          [G, G, G, G, G, W, G, W, G, G],
          [G, G, G, G, G, W, W, W, G, G],
          [G, G, G, G, G, W, W, W, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, W, G, W, G, G],
          [G, G, G, G, G, W, G, W, G, G],
          [G, G, G, G, G, W, W, W, G, G],
          [G, G, G, G, G, W, W, W, G, E],
          ]

def map_hard():
  return [[G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, E],
          ]


# DEFINE CELLS OCCUPATION
AGENT_NUMBER  = 1000
cells_occupation = [[ AGENT_NUMBER, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          ]

# GRID TO ACTUALLY DISPLAY
grid_to_display_very_easy = [[A, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, E],
          ]

grid_to_display_easy = [[A, G, G, G, W, W, W, W, W, W],
          [G, G, G, G, G, W, W, W, W, W],
          [G, G, G, G, G, G, W, W, W, W],
          [G, G, G, G, G, G, G, W, W, W],
          [W, G, G, G, G, G, G, G, W, W],
          [W, W, G, G, G, G, G, G, G, W],
          [W, W, W, G, G, G, G, G, G, G],
          [W, W, W, W, G, G, G, G, G, G],
          [W, W, W, W, W, G, G, G, G, G],
          [W, W, W, W, W, W, G, G, G, E],
          ]

grid_to_display_medium = [[A, G, G, G, G, W, W, W, W, W],
          [G, G, G, G, G, W, G, G, G, G],
          [G, G, G, G, G, W, G, W, G, G],
          [G, G, G, G, G, W, W, W, G, G],
          [G, G, G, G, G, W, W, W, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, W, G, W, G, G],
          [G, G, G, G, G, W, G, W, G, G],
          [G, G, G, G, G, W, W, W, G, G],
          [G, G, G, G, G, W, W, W, G, E],
          ]

grid_to_display_hard = [[A, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, E],
          ]


# DEFINE DISCOVERY HISTORY
discovery_history = [[True, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          ]


# MAP CLASS
class Map:
    
    # Constructor
    def __init__(self, keyword):
        
        self.cells_occupation = cells_occupation
        self.discovery_history = discovery_history
        
        if keyword == "very_easy":
            self.grid = map_very_easy()
            self.grid_to_display = grid_to_display_very_easy
            
        elif keyword == "easy":
            self.grid = map_easy()
            self.grid_to_display = grid_to_display_easy
            
        elif keyword == "medium":
            self.grid = map_medium()
            self.grid_to_display = grid_to_display_medium
            
        elif keyword == "hard":
            self.grid = map_hard()
            self.grid_to_display = grid_to_display_hard
        
        
    # Decrease count when an agent leaves the tile  
    def decrease_count(self, agent):
        
        row = agent.row
        col = agent.col
        self.cells_occupation[row][col] -= 1
    
    
    # Increase count when an agent gets to the tile
    def increase_count(self, agent):
        
        row = agent.row
        col = agent.col
        self.cells_occupation[row][col] += 1
    

    # All the tiles with at list one agent must display one
    def update_tiles(self):
        
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                
                if self.cells_occupation[row][col] > 0:
                    self.grid_to_display[row][col] = A  
                else:
                    self.grid_to_display[row][col] = self.grid[row][col]
     

    # Change the discovery state of a cell 
    def discover_cell(self, agent):
      self.discovery_history[agent.row][agent.col] = True


    # Reinitialization at the end of each generation
    def reinitialize(self, keyword):
        
        self.cells_occupation = [[AGENT_NUMBER, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          ]

        self.discovery_history = [[True, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          ]
        
        if keyword == "very_easy":
            
            self.grid = [[G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, E],
          ]
            
            self.grid_to_display = [[A, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, G],
          [G, G, G, G, G, G, G, G, G, E],
          ]
            
        elif keyword == "easy":
            
            self.grid = [[G, G, G, G, W, W, W, W, W, W],
          [G, G, G, G, G, W, W, W, W, W],
          [G, G, G, G, G, G, W, W, W, W],
          [G, G, G, G, G, G, G, W, W, W],
          [W, G, G, G, G, G, G, G, W, W],
          [W, W, G, G, G, G, G, G, G, W],
          [W, W, W, G, G, G, G, G, G, G],
          [W, W, W, W, G, G, G, G, G, G],
          [W, W, W, W, W, G, G, G, G, G],
          [W, W, W, W, W, W, G, G, G, E],
          ]
            
            self.grid_to_display = [[A, G, G, G, W, W, W, W, W, W],
          [G, G, G, G, G, W, W, W, W, W],
          [G, G, G, G, G, G, W, W, W, W],
          [G, G, G, G, G, G, G, W, W, W],
          [W, G, G, G, G, G, G, G, W, W],
          [W, W, G, G, G, G, G, G, G, W],
          [W, W, W, G, G, G, G, G, G, G],
          [W, W, W, W, G, G, G, G, G, G],
          [W, W, W, W, W, G, G, G, G, G],
          [W, W, W, W, W, W, G, G, G, E],
          ]
                  
        elif keyword == "medium": 
        
            self.grid = [[G, G, G, G, G, W, W, W, W, W],
              [G, G, G, G, G, W, G, G, G, G],
              [G, G, G, G, G, W, G, W, G, G],
              [G, G, G, G, G, W, W, W, G, G],
              [G, G, G, G, G, W, W, W, G, G],
              [G, G, G, G, G, G, G, G, G, G],
              [G, G, G, G, G, W, G, W, G, G],
              [G, G, G, G, G, W, G, W, G, G],
              [G, G, G, G, G, W, W, W, G, G],
              [G, G, G, G, G, W, W, W, G, E],
              ]


            self.grid_to_display = [[A, G, G, G, G, W, W, W, W, W],
              [G, G, G, G, G, W, G, G, G, G],
              [G, G, G, G, G, W, G, W, G, G],
              [G, G, G, G, G, W, W, W, G, G],
              [G, G, G, G, G, W, W, W, G, G],
              [G, G, G, G, G, G, G, G, G, G],
              [G, G, G, G, G, W, G, W, G, G],
              [G, G, G, G, G, W, G, W, G, G],
              [G, G, G, G, G, W, W, W, G, G],
              [G, G, G, G, G, W, W, W, G, E],
              ]
            
        elif keyword == "hard":
            
            self.grid = [[G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, E],
          ]
            
            self.grid_to_display = [[A, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, G, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, W, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, G],
          [G, G, G, G, G, G, G, W, G, E],
          ]


# GENOME GENERATION
# Choose randomly the directions to create the genome of size GENOME_SIZE
def generate_genome():
    
  available_choices = ["up", "down", "left", "right"]
  genome = []

  for i in range(GENOME_SIZE):
    genome.append(choice(available_choices))

  return genome


# GET EXIT COORDS
# Find the exit to compute the distance between it and an agent later
def get_exit_coords(map):
    
  row_exit = 0
  col_exit = 0
  
  for row in range(MAP_HEIGHT):
    for col in range(MAP_WIDTH):
        
      if map.grid[row][col] == 3:
        row_exit = row
        col_exit = col
        break
  
  return (row_exit, col_exit)


# AGENT CLASS
class Agent:

  # Constructor
  def __init__(self):
    
    # The agent coords
    self.row = 0
    self.col = 0
    
    # If the agent is dead, it doesn't move anymore
    self.state = "alive"
    
    # Randomly generated genome
    self.genome = generate_genome()
    
    # The score that we want to maximize
    self.score = 0


  # Up move
  def go_up(self):
    
    self.row -= 1

    
  # Down move
  def go_down(self):
      
    self.row += 1
 

  # Left move
  def go_left(self):
      
    self.col -= 1

        
  # Right move
  def go_right(self):
        
    self.col += 1

    
  # Make a move
  def move(self, direction):    
    
    if direction == "up":
      self.go_up()

    elif direction == "down":
      self.go_down()

    elif direction == "left":
      self.go_left()

    elif direction == "right":
      self.go_right()
 

  # Check if the move is valid
  def check_move_validity(self, direction):
    
    test = False   
    
    if direction == "up":
        test = self.row > 0 and map.grid[self.row - 1][self.col] != 2
        
    elif direction == "down":
        test = self.row < MAP_HEIGHT - 1 and map.grid[self.row + 1][self.col] != 2
        
    elif direction == "left":
        test = self.col > 0 and map.grid[self.row][self.col - 1] != 2
    
    elif direction == "right":
        test =  self.col < MAP_HEIGHT - 1 and map.grid[self.row][self.col + 1] != 2    
    
    return test


  # Bonus if the agent discovers new cells
  def has_discovered_new_cells(self, map):
    return  (map.discovery_history[self.row][self.col] == False)
        

  # The agent can't move anymore
  def die(self):
    self.state = "dead"

    
  # Manhattan distance
  def compute_distance(self):
    
    return  abs(get_exit_coords(map)[1] - self.col) + abs(get_exit_coords(map)[0] - self.row)


# AGENTS INITIALIZATION
# Create the starting agents list
def initialize_agents_list(AGENT_NUMBER):
  
  listAgents = []
  
  for i in range(AGENT_NUMBER):
    agent = Agent()
    listAgents.append(agent)
  
  return listAgents


# GET ALIVE AGENTS NUMBER
# Compute the alive agent number
def get_alive_agents_number(agents_list):
  
  count = 0
  
  for agent in agents_list:
    if (agent.state == "alive"):
      count +=1

  return count


# RANKING
# Do the ranking of the agents
def get_ranking(agents_list):
  
  scores = []
  
  for agent_index in range(len(agents_list)):
    scores.append(agents_list[agent_index].score)

  ranking_indexes = sorted(range(len(scores)), key=scores.__getitem__)
  ranking_indexes.reverse()

  ranking = []
  
  for i in ranking_indexes:
    ranking.append(agents_list[i])

  return ranking


# CROSS-OVER
# Use the half of the genomes of 2 agents to create a new one
def cross_over(agent1, agent2):
  
  new_agent = Agent()
  new_genome = agent1.genome[0:TILES_NUMBER] + agent2.genome[TILES_NUMBER:]
  new_agent.genome = new_genome
  
  return new_agent


# MUTATION
# Change randomly a portion of the genome of an agent
def mutation(agent):
    
  for gene in range(len(agent.genome)):
    
    if random() <= MUTATION_RATE:
        
        if agent.genome[gene] == "up":
            new_gene = choice(["down", "right", "left"])

        elif agent.genome[gene] == "down":
            new_gene = choice(["up", "right", "left"])

        elif agent.genome[gene] == "left":
            new_gene = choice(["up", "down", "right"])

        elif agent.genome[gene] == "right":
            new_gene = choice(["up", "down", "left"])

        agent.genome[gene] = new_gene


# REINITIALIZATION
# Reinitialization of the agents at the end of each generation
def reinitialize_agents_list(agents_list):
  
  for agent in agents_list:
    agent.row = 0
    agent.col = 0
    agent.state = "alive"
    agent.score = 0
    agent.discovery_history = [[True, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          ]


# GAME OVER
# Screen displayed if the agents don't find the exit
def game_over():
    
    font_cambria_game_over = pygame.font.SysFont("Cambria", 64)
    pygame.mixer.music.load("game_over.ogg")
    
    DISPLAY.fill(BLACK)
    label = font_cambria_game_over.render("GAME OVER", True, WHITE)
    DISPLAY.blit(label, (MAP_WIDTH * TILE_SIZE - label.get_rect().width/2 , MAP_HEIGHT * TILE_SIZE/2 - label.get_rect().height/2))
    pygame.display.update()

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
              
    pygame.quit()
    exit()


# VICTORY
# Screen displayed if the agents find the exit
def victory():

    font_cambria_victory = pygame.font.SysFont("Cambria", 64)
    pygame.mixer.music.load("victory.ogg")
    
    DISPLAY.fill(BLACK)
    label = font_cambria_victory.render("YOU DEFEATED", True, GOLDEN)
    DISPLAY.blit(label, (MAP_WIDTH * TILE_SIZE - label.get_rect().width/2 , MAP_HEIGHT * TILE_SIZE/2 - label.get_rect().height/2))
    pygame.display.update()

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                pygame.quit()
                exit()
        
    pygame.quit()
    exit()


# GAME LAUNCHING
# Parameters to change
keyword = "hard"
map = Map(keyword)
TILE_SIZE = 30
MAP_WIDTH = len(map.grid[0])
MAP_HEIGHT = len(map.grid)
TILES_NUMBER = MAP_WIDTH * MAP_HEIGHT
GENOME_SIZE = 40
GENERATION_NUMBER = 1000
KEEPING_RATE = 0.05
MUTATION_RATE = 1/40


# Initialization
agents_list = initialize_agents_list(AGENT_NUMBER)

# Display
pygame.init()
pygame.display.set_caption("Labypath Adventure")
pygame.display.set_icon(pygame.image.load("character_grass.jpg"))
DISPLAY = pygame.display.set_mode((2 * MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))
font_cambria = pygame.font.SysFont("Cambria", 24)

# Musics
pygame.mixer.init()
pygame.mixer.music.load("battle_theme.ogg")
pygame.mixer.music.play(-1)


best_score = 0
main_screen = True

while main_screen :
        
    # Exploration
    for generation in range(GENERATION_NUMBER):

        # Texts display
        DISPLAY.fill(BLACK)
        label = font_cambria.render("Generation {}".format(generation + 1), True, WHITE)
        DISPLAY.blit(label, (MAP_WIDTH * TILE_SIZE * 5/4, label.get_rect().height))
        label = font_cambria.render("Best score :  {}".format(round(best_score, 2)), True, GOLDEN)
        DISPLAY.blit(label, (MAP_WIDTH * TILE_SIZE * 6/5, label.get_rect().height * 2))

        # Map exploration for each agent
        for agent in agents_list:
            for direction in agent.genome:
              for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

              # Valid move
              if agent.check_move_validity(direction):
                
                map.decrease_count(agent)
                agent.move(direction)
                map.increase_count(agent)
                map.update_tiles()
                agent.score += 1

                if agent.has_discovered_new_cells(map):
                  map.discover_cell(agent)
                  agent.score += 10
                  
              else:
                    agent.die()

              # No need to continue if the agent is dead
              if agent.state == "dead":
                agent.score = 0
                break
                
            if agent.state == "alive":
                
                if map.grid[agent.row][agent.col] == 3:
                    victory()    
                
                else:
                    # Score evaluation
                    agent.score += log(agent.score + 1) + 1 / agent.compute_distance() 
        
        # Draw map
        for row in range(MAP_HEIGHT):
            for col in range(MAP_WIDTH):
                DISPLAY.blit(TileImage[map.grid_to_display[row][col]], (col * TILE_SIZE, row * TILE_SIZE))
        
        # Ranking
        ranking = get_ranking(agents_list)
        temp = ranking[0].score
        
        if temp > best_score:
            best_score = temp
        
        # Display ranking
        label = font_cambria.render("1 : {}".format(str(round(ranking[0].score, 2))), True, GOLDEN)
        DISPLAY.blit(label, (MAP_WIDTH * TILE_SIZE * 1.35, label.get_rect().height * 3))
        label = font_cambria.render("2 : {}".format(str(round(ranking[1].score, 2))), True, GOLDEN)
        DISPLAY.blit(label, (MAP_WIDTH * TILE_SIZE * 1.35, label.get_rect().height * 4))
        label = font_cambria.render("3 : {}".format(str(round(ranking[2].score, 2))), True, GOLDEN)
        DISPLAY.blit(label, (MAP_WIDTH * TILE_SIZE * 1.35, label.get_rect().height * 5))
        label = font_cambria.render("4 : {}".format(str(round(ranking[3].score, 2))), True, GOLDEN)
        DISPLAY.blit(label, (MAP_WIDTH * TILE_SIZE * 1.35, label.get_rect().height * 6))
        label = font_cambria.render("5 : {}".format(str(round(ranking[4].score, 2))), True, GOLDEN)
        DISPLAY.blit(label, (MAP_WIDTH * TILE_SIZE * 1.35, label.get_rect().height * 7))
        pygame.display.update()

        # New agents list
        new_list = []

        # The best are kept for the next generation
        keeping_range = int(KEEPING_RATE * AGENT_NUMBER)
        
        for agent in range(keeping_range):
            new_list.append(ranking[agent])

        # Cross-over
        rest_range = AGENT_NUMBER - keeping_range
        
        i = 0
        while len(new_list) != AGENT_NUMBER:
            temp = list(range(rest_range))
            
            if i in temp:
                temp.remove(i)
            
            j = 0
            while len(new_list) != AGENT_NUMBER:
                new_agent = cross_over(agents_list[i], agents_list[j])
                new_list.append(new_agent)
                j += 1
            
            i += 1

        # Update the agents list
        agents_list = new_list

        # Mutation
        for agent in agents_list:
            mutation(agent)

        if (generation != GENERATION_NUMBER - 1):
            map.reinitialize(keyword)
            reinitialize_agents_list(agents_list)

    main_screen = False
    pygame.mixer.stop()

game_over()