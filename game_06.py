import pyxel

# [06] Create a class for the apple
class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def update(self):
        if self.y < App.HEIGHT:
            self.y += 1		# Move the apple down
    
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK)		#[05] change self.apple_y # Draw the apple sprite blt引数=(x, y, img, u, v, w, h, colkey)


class App:
    # 座標は画面左上が(0,0)
    WIDTH = 160		# Width of the window
    HEIGHT = 120		# Height of the window
    APPLE_INTERVAL = 30		# [06] Interval for apple appearance = 30 frames
    def __init__(self):		# Constructor
        pyxel.init(self.WIDTH, self.HEIGHT, title="Pyxel Game")
        pyxel.mouse(True)		# [02]Enable mouse input
        # [03]02で作成したものを削除
        pyxel.load("my_resource.pyxres") # [03]Load assets
        self.bowl_x = self.WIDTH // 2 - 4		# [04]Set the initial x position of the bowl
        self.bowl_y = self.HEIGHT-10	# [05]Set the initial y position of the bowl

        # [06] self.apple_x, self.apple_yを削除
        self.apples = []	# [06] Create a list to hold apples

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
        
        # [06] self.apple_yの更新を削除
        if pyxel.frame_count % self.APPLE_INTERVAL == 0:		# [06] Check if it's time to create a new apple
            self.apples.append(Apple(pyxel.rndi(0, self.WIDTH - 8), 0))		# [06] Generate a random x position for the apple
        # [06] Update the position of each stone
        for apple in self.apples.copy():
            apple.update()		# Update each stone's position
            if (self.bowl_x-4 <= apple.x <= self.bowl_x+4) and \
				(self.bowl_y <= apple.y <= self.bowl_y+8):		# [05]Check for collision with the bowl
                self.is_collision = True		# [05]Set collision flag to True
            if apple.y >= self.HEIGHT:		# [06] Remove the apple if it goes off the screen
                self.apples.remove(apple)		# [06] Remove the apple from the list
    
    def draw(self):		# Draw method(下のレイヤーから順に描画する)
        pyxel.cls(pyxel.COLOR_DARK_BLUE)		# 背景色をダークブルーに設定

        # [03]02で作成したものを削除

		# [06] pyxel.blt appleを削除
        
        for apple in self.apples:		# [06] Draw each apple
            apple.draw()		# [06]Draw each apple
            
        pyxel.blt(self.bowl_x, self.bowl_y, 0, 8, 8, 8, 8, pyxel.COLOR_BLACK)		# [04]change self.bowl_x # Draw the bowl sprite blt引数=(x, y, img, u, v, w, h, colkey)
        
        if self.is_collision:
            pyxel.text(self.WIDTH // 2 - 20, self.HEIGHT // 2, "Game Over", pyxel.COLOR_YELLOW)		# [05]Display collision message
App()
