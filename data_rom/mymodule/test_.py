import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random
    from tuto_main import tuto_start
    from action_rom import menu_open, juljun_off, juljun_on, moving_check
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos, mouse_move_cpp
    from dungeon_rom import dungeon_start, dungeon_check
    from dead import dead_recover
    from clean_screen_rom import clean_screen

    from get_item_rom import get_chulsuk, get_post, get_upjuk
    from potion_rom import potion_buy, juljun_potion_check


    print("test")
    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3

    print("test")

    # 던전_특수_정령의성채_1

    # data = "던전_특수_정령의성채_1"
    # data = "던전_일반_카타콤_1"
    # dungeon_start(cla, data)

    # clean_screen(cla)

    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(200, 70, 250, 120, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("dead_close", imgs_.x, imgs_.y)
    else:
        print("안 보여")

    # data = "던전_일반_카타콤_1"
    # result_check = dungeon_check(cla, data)
    # print("던전 진행 정보", result_check[0], result_check[1])

    # juljun_off(cla)

    # potion_buy(cla)




    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\juljun_potion_zero.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(670, 30, 740, 100, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("물약 없다")
    # else:
    #     print("물약 있다")