SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
UNIT = 30
GRID = []
for i in range(0, SCREEN_HEIGHT, UNIT):
    for j in range(0, SCREEN_WIDTH, UNIT):
        GRID.append([j, i])