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
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos, get_region, text_check_get, in_number_check, int_put_, imgs_set_num
    from dungeon_rom import dungeon_start, dungeon_check
    from dead import dead_recover
    from clean_screen_rom import clean_screen
    from auction_rom import auction_start, collection_before_auction_start
    from property_rom import my_property_upload, mine_check
    from clean_screen_rom import clean_screen
    from boonhae_rom import boonhae_start
    from jadong_rom import jadong_spot

    from get_item_rom import get_chulsuk, get_post, get_upjuk, get_mission, get_sangjum
    from potion_rom import potion_buy, juljun_potion_check, out_potion_check, potion_buy_start
    from collection_rom import collection_start


    print("test")
    cla = "two"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3

    get_chulsuk(cla)

    # print("test")
    # pyautogui.screenshot('asd.png', region=(get_region(700, 530, 713, 561, cla)))
    # for i in range(10):
    #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\out_number\\" + str(i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(700, 530, 713, 561, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("물약 100 자릿수 number is... ", i)
    #         break

    # read_dia = " | 466"
    #
    # digit_ready = in_number_check(read_dia)
    # print("digit_ready", digit_ready)
    # if digit_ready == True:
    #     read_data_int = int(int_put_(read_dia))
    #     print("read_data_int", read_data_int)
    #     dia_ = read_data_int

    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\gold.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(360, 30, 600, 70, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("gold", imgs_)
    #     # 481
    #     x_reg_1 = imgs_.x - plus
    #
    #     for i in range(4):
    #         read_gold = text_check_get(x_reg_1 + 10 + i, 38, x_reg_1 + 80, 50, cla)
    #         if read_gold == "":
    #             print("골드 못 읽음")
    #         else:
    #             print("read_gold", read_gold)
    #             break

    # 던전_특수_정령의성채_1

    # data = "던전_특수_정령의성채_1"
    # data = "던전_일반_카타콤_1"
    # dungeon_start(cla, data)

    #####################################로그인 부분##################################################

    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\kakao_login_btn.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(280, 150, 1900, 900, "one", img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #
    #     print("kakao_login_btn", imgs_)
    #     click_pos_reg(imgs_.x, imgs_.y, cla)
    #     for i in range(10):
    #
    #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\kakao_login_click_btn.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(280, 350, 1900, 900, "one", img, 0.7)
    #         if imgs_ is not None and imgs_ != False:
    #             print("kakao_login_click_btn", imgs_)
    #             break
    #         else:
    #             full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\auto_login_btn.PNG"
    #             img_array = np.fromfile(full_path, np.uint8)
    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #             imgs_ = imgs_set_(280, 150, 1900, 900, "one", img, 0.7)
    #             if imgs_ is not None and imgs_ != False:
    #                 print("auto_login_btn", imgs_)
    #                 full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\auto_login_confirm.PNG"
    #                 img_array = np.fromfile(full_path, np.uint8)
    #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #                 imgs_ = imgs_set_(280, 150, 1900, 900, "one", img, 0.7)
    #                 if imgs_ is not None and imgs_ != False:
    #                     print("auto_login_confirm", imgs_)
    #                     click_pos_reg(imgs_.x, imgs_.y, cla)
    #             else:
    #                 full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\kakao_login_btn.png"
    #                 img_array = np.fromfile(full_path, np.uint8)
    #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #                 imgs_ = imgs_set_(280, 150, 1900, 900, "one", img, 0.7)
    #                 if imgs_ is not None and imgs_ != False:
    #                     print("kakao_login_btn", imgs_)
    #                     click_pos_reg(imgs_.x, imgs_.y, cla)
    #         time.sleep(0.5)
    #
    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\kakao_login_click_btn.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(280, 350, 1900, 900, "one", img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("kakao_login_click_btn", imgs_)
    #
    #
    #
    #     # id => y - 170
    #     click_pos_reg(imgs_.x, imgs_.y - 170, cla)
    #     time.sleep(0.3)
    #     click_pos_reg(imgs_.x, imgs_.y - 170, cla)


        # pw => y - 110

    #####################################로그인 부분##################################################

    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\full_potion.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(110, 130, 200, 160, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #
    #     print("full_potion", imgs_.x, imgs_.y)
    #
    # # result_num = text_check_get(707, 552, 712, 560, cla)
    # # print("result_num", result_num)
    #
    # for i in range(10):
    #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\juljun_number\\" + str(i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(680, 45, 700, 75, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("물약 100 자릿수 number is... ", i)
    #         break
    #
    #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\juljun_number\\no_number.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(680, 45, 700, 75, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("물약 100개 이하.......")
    #         is_potion = False
    #         break

    # # 707, 552, 712, 560
    # for i in range(10):
    #     print("현재 숫자", i)
    #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\out_number\\" + str(i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(700, 530, 713, 560, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("number is... ", i)
    #         break
    #
    #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\out_number\\no_number.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(700, 530, 713, 560, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("no_number.......")
    #         break


    # result_num = text_check_get(693, 66, 699, 75, cla)
    # print("result_num", result_num)

    # # 693, 66, 699, 75
    # for i in range(10):
    #     print("현재 숫자", i)
    #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\number\\" + str(i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(680, 45, 700, 75, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("number is... ", i)
    #         break
    #
    #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\number\\no_number.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(680, 45, 700, 75, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("no_number.......")
    #         break

    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\full_potion.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(110, 130, 200, 160, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("full_potion", imgs_.x, imgs_.y)

    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\30_39.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(300, 120, 600, 180, "two", img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("933333333333")
    #
    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\40_49.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(300, 120, 600, 180, "two", img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("90000000000000000")
    #
    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\40_49_3.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(300, 120, 600, 180, "two", img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("90000000000084888888888447777666600000")
    #
    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\server_select_btn.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(280, 470, 410, 520, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("server_select_btn")

    # collection_start(cla)

    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(170, 105, 250, 125, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("main_quest_clickedmain_quest_clickedmain_quest_clickedmain_quest_clicked 1", imgs_)
    #
    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\re_ready.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # # 235, 115, 290, 450
    # for ix in pyautogui.locateAllOnScreen(img, region=(235 + plus, 115, 55, 335),
    #                                       confidence=0.9):
    #     print(ix, ix.left, ix.top)
    #     click_pos_reg(ix.left, ix.top, cla)
    #
    #     time.sleep(0.3)


    # my_property_upload(cla)

    # read_dia = text_check_get(518, 77, 549, 90, cla)
    # if read_dia == "":
    #     print("다이아 못 읽음")
    # else:
    #     print("read_dia", read_dia)
    #
    # read_gold = text_check_get(500, 99, 549, 112, cla)
    # if read_gold == "":
    #     print("골드 못 읽음")
    # else:
    #     print("read_gold", read_gold)

    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\list\\skillbook_knight_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(680, 130, 920, 530, cla, img, 0.75)
    # if imgs_ is not None and imgs_ != False:
    #     print("거래물건 있음 skillbook_knight_1", imgs_)
    # else:
    #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\list\\skillbook_knight_2.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(680, 130, 920, 530, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("거래물건 있음 skillbook_knight_2", imgs_)
    #     else:
    #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\list\\skillbook_knight_3.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(680, 130, 920, 530, cla, img, 0.75)
    #         if imgs_ is not None and imgs_ != False:
    #             print("거래물건 있음 skillbook_knight_3", imgs_)

    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\mission_complete_full.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(680, 330, 750, 475, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("mission_complete_full", imgs_.x, imgs_.y)
    #
    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\mission_complete_full.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for ix in pyautogui.locateAllOnScreen(img, region=(370 + plus, 330, 70, 475), confidence=0.97):
    #     print(ix, ix.left, ix.top)
    #     click_pos_reg(ix.left + 46, ix.top, cla)
    #     for c in range(5):
    #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(530, 140, 580, 170, cla, img, 0.7)
    #         if imgs_ is not None and imgs_ != False:
    #             print("lv_close", imgs_.x, imgs_.y)
    #             click_pos_reg(imgs_.x, imgs_.y, cla)
    #             time.sleep(0.2)
    #             break
    #         time.sleep(0.1)
    #
    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\mission_complete_full.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for iy in pyautogui.locateAllOnScreen(img, region=(680 + plus, 330, 70, 475), confidence=0.97):
    #     print(iy, iy.left, iy.top)
    #     click_pos_reg(iy.left + 46, iy.top, cla)
    #     for c in range(5):
    #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(530, 140, 580, 170, cla, img, 0.7)
    #         if imgs_ is not None and imgs_ != False:
    #             print("lv_close", imgs_.x, imgs_.y)
    #             click_pos_reg(imgs_.x, imgs_.y, cla)
    #             time.sleep(0.2)
    #             break
    #         time.sleep(0.1)
    #     # last_x = i.left
    #     # last_y = i.top
    #     # print("last_x", last_x)
    #     # print("last_y", last_y)

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