import os
import sys
import pygame as pg

# ファイルの場所に合わせてカレントディレクトリを変更
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    # 画面サイズの指定
    screen = pg.display.set_mode((800, 600))
    # clock = pg.time.Clock() # ループが無いため不要

    # 背景画像の読み込みと変換
    bg_img = pg.image.load("fig/pg_bg.jpg").convert()
    # bg_img_w = bg_img.get_width() # ループが無いので不要

    # キャラクター画像の読み込み
    kouka_img = pg.image.load("fig/3.png") 
    # 左右反転
    kouka2_img = pg.transform.flip(kouka_img, True, False) 

    # tmr = 0 # ループが無いため不要
    # scroll_x = 0 # ループが無いため不要
    # SCROLL_SPEED = 5 # ループが無いため不要

    # イベントループの代わりに、一度だけ描画処理を実行

    # 背景画像を一度だけ描画
    screen.blit(bg_img, [0, 0]) 
    
    # キャラクター画像を一度だけ描画
    screen.blit(kouka2_img, [300, 200]) 

    # 画面の更新を一度だけ実行
    pg.display.update()

    # *注意*: このプログラムは、画面を更新した後、すぐに次の処理（main関数の終了）に進みます。
    # 実際には、画面がユーザーに見える形で表示される時間は**ほとんどありません**。
    # 画面を表示し続けるには、イベントループ（while True:）が必要です。


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit() # Pygameの終了
    sys.exit() # プログラムの終了