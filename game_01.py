import pyxel

class App:
    # 座標は画面左上が(0,0)
    WIDTH = 160		# Width of the window
    HEIGHT = 120		# Height of the window
    def __init__(self):		# Constructor
        pyxel.init(self.WIDTH, self.HEIGHT, title="Pyxel Game")
        pyxel.run(self.update, self.draw)		# Run the game     
        
    def update(self):		# Update method(30 FPS:default)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()		# Exit the game when ESC is pressed
    
    def draw(self):		# Draw method(下のレイヤーから順に描画する)
        pyxel.cls(pyxel.COLOR_DARK_BLUE)		# 背景色をダークブルーに設定
        pyxel.text(self.WIDTH//2-20, self.HEIGHT//2-2, "Start Game", pyxel.COLOR_YELLOW)		# 画面中央にテキストを描画
print("Start")
App()
print("End")
