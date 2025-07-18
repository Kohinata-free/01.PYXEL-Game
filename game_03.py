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
        pyxel.run(self.update, self.draw)		# Run the game
        
        
    def update(self):		# Update method(30 FPS:default)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()		# Exit the game when ESC is pressed
    
        # [03]02で作成したものを削除
    
    def draw(self):		# Draw method(下のレイヤーから順に描画する)
        pyxel.cls(pyxel.COLOR_DARK_BLUE)		# 背景色をダークブルーに設定

        # [03]02で作成したものを削除

        pyxel.blt(self.WIDTH // 2 - 4, 0, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK)		# Draw the apple sprite blt引数=(x, y, img, u, v, w, h, colkey)
        pyxel.blt(self.WIDTH // 2 - 4, self.HEIGHT-10, 0, 8, 8, 8, 8, pyxel.COLOR_BLACK)		# Draw the bowl sprite blt引数=(x, y, img, u, v, w, h, colkey)
App()
