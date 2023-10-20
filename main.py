import pygame

class Jogador:
  def __init__(self):
    self.posicao = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

  def mover(self, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.posicao.y -= 300 * dt
    if keys[pygame.K_s]:  
      self.posicao.y += 300 * dt
    if keys[pygame.K_a]:
      self.posicao.x -= 300 * dt      
    if keys[pygame.K_d]:
      self.posicao.x += 300 * dt

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

jogador = Jogador() 

while running:

  # event handling  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # desenhar tela
  screen.fill("dark blue")

  dt = clock.tick(60) / 1000

  jogador.mover(dt)

  pygame.draw.circle(screen, "red", jogador.posicao, 40)

  pygame.display.flip()

pygame.quit()
