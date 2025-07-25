import pyxel

class App:
    # 座標は画面左上が(0,0)
    WIDTH = 160		# Width of the window
    HEIGHT = 120		# Height of the window
    def __init__(self):		# Constructor
        pyxel.init(self.WIDTH, self.HEIGHT, title="Pyxel Game")
        pyxel.mouse(True)		# [02]Enable mouse input
        # [03]02で作成したものを削除
        pyxel.load("my_resource.pyxres") # [03]Load assets
        self.bowl_x = self.WIDTH // 2 - 4		# [04]Set the initial x position of the bowl
        self.bowl_y = self.HEIGHT-10	# [05]Set the initial y position of the bowl
        self.apple_x = self.WIDTH // 2 - 4		# [05]Set the initial x position of the apple
        self.apple_y = 0		# [05]Set the initial y position of the apple
        self.is_collision = False
        pyxel.run(self.update, self.draw)		# Run the game
        
        
    def update(self):		# Update method(30 FPS:default)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()		# Exit the game when ESC is pressed
    
        # [03]02で作成したものを削除
        
        if pyxel.btn(pyxel.KEY_RIGHT) and self.bowl_x < self.WIDTH-8:		# [04]If the right arrow key is pressed
            self.bowl_x += 1		# Move the bowl right
        elif pyxel.btn(pyxel.KEY_LEFT) and self.bowl_x > 0:		# [04]If the left arrow key is pressed
            self.bowl_x -= 1		# Move the bowl left
        
        if self.apple_y < self.HEIGHT:		# [05]If the apple is not at the bottom
            self.apple_y += 1		# Move the apple down
            
        if (self.bowl_x-4 <= self.apple_x <= self.bowl_x+4) and \
            (self.bowl_y <= self.apple_y <= self.bowl_y+8):		# [05]Check for collision with the bowl
                self.is_collision = True		# [05]Set collision flag to True
    
    def draw(self):		# Draw method(下のレイヤーから順に描画する)
        pyxel.cls(pyxel.COLOR_DARK_BLUE)		# 背景色をダークブルーに設定

        # [03]02で作成したものを削除

        pyxel.blt(self.apple_x, self.apple_y, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK)		#[05] change self.apple_y # Draw the apple sprite blt引数=(x, y, img, u, v, w, h, colkey)
        pyxel.blt(self.bowl_x, self.bowl_y, 0, 8, 8, 8, 8, pyxel.COLOR_BLACK)		# [04]change self.bowl_x # Draw the bowl sprite blt引数=(x, y, img, u, v, w, h, colkey)
        
        if self.is_collision:
            pyxel.text(self.WIDTH // 2 - 20, self.HEIGHT // 2, "Game Over", pyxel.COLOR_YELLOW)		# [05]Display collision message
App()
