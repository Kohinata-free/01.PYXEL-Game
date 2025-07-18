import pyxel

class App:
    # 座標は画面左上が(0,0)
    WIDTH = 160		# Width of the window
    HEIGHT = 120		# Height of the window
    def __init__(self):		# Constructor
        pyxel.init(self.WIDTH, self.HEIGHT, title="Pyxel Game")
        pyxel.mouse(True)		# [02]Enable mouse input
        self.number = 0		# [02]Initialize a number variable
        self.MINUS_X = self.WIDTH//2-20     # [02]Calculate the X position for the minus sign
        self.MINUS_Y = self.HEIGHT//2-2		# [02]Calculate the Y position for the minus sign
        self.PLUS_X = self.WIDTH//2+20.5     # [02]Calculate the X position for the plus sign
        self.PLUS_Y = self.HEIGHT//2-2		# [02]Calculate the Y position for the plus sign
        pyxel.run(self.update, self.draw)		# Run the game
        
        
    def update(self):		# Update method(30 FPS:default)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()		# Exit the game when ESC is pressed
    
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):		# [02]Check if the left mouse button is pressed
            if self.MINUS_X-2 <= pyxel.mouse_x <= self.MINUS_X + 5 and self.MINUS_Y-1 <= pyxel.mouse_y < self.MINUS_Y + 6:		# [02]Check if the mouse is over the minus sign
                self.number -= 1		# [02]Decrease the number by 1
            elif self.PLUS_X-2 <= pyxel.mouse_x <= self.PLUS_X + 5 and self.PLUS_Y-1 <= pyxel.mouse_y < self.PLUS_Y + 6:		# [02]Check if the mouse is over the plus sign
                self.number += 1		# [02]Increase the number by 1
    
    def draw(self):		# Draw method(下のレイヤーから順に描画する)
        pyxel.cls(pyxel.COLOR_DARK_BLUE)		# 背景色をダークブルーに設定
        pyxel.text(self.WIDTH//2-0.5, self.HEIGHT//2-2, f"{self.number}", pyxel.COLOR_YELLOW)		# [02]画面中央に数値を表示
        pyxel.text(self.MINUS_X, self.MINUS_Y, "-", pyxel.COLOR_WHITE)		# [02]数値の左に"-"を表示
        pyxel.text(self.PLUS_X, self.PLUS_Y, "+", pyxel.COLOR_WHITE)		# [02]数値の右に"+"を表示
App()
