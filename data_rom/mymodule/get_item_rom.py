import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_item_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check
    from boonhae_rom import auction_ready_boonhae_start

    try:
        print("get_item_start")

        auction_ready_boonhae_start(cla)

        get_chulsuk(cla)
        get_post(cla)
        get_upjuk(cla)
        get_mission(cla)



    except Exception as e:
        print(e)
        return 0


def get_chulsuk(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open
    from clean_screen_rom import clean_screen

    try:
        print("get_chulsuk")

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\action\\menu_open\\menu_restart.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 290, 930, 360, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                menu_opened = True
                print("menu_restart", imgs_.x, imgs_.y)

                # 출석
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(770, 290, 800, 320, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("get_chulsuk : menu_point", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_chulsuk.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_chulsuk.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("title_chulsuk", imgs_.x, imgs_.y)

                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\chul_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(80, 90, 350, 120, cla, img, 0.65)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point 1", imgs_.x, imgs_.y)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                                time.sleep(0.5)

                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(880, 445, 920, 475, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("menu_point 2", imgs_.x, imgs_.y)
                                    click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                            else:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\chul_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(80, 90, 350, 120, cla, img, 0.65)
                                if imgs_ is not None and imgs_ != False:
                                    print("menu_point 1", imgs_.x, imgs_.y)
                                    click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                                    time.sleep(0.5)

                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(880, 445, 920, 475, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("menu_point 2", imgs_.x, imgs_.y)
                                        click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)

                                else:
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_chulsuk.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                        time.sleep(0.5)


            else:
                result_out = out_check(cla)

                if result_out == True:
                    click_pos_2(930, 45, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\action\\menu_open\\menu_restart.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 290, 930, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                else:
                    clean_screen(cla)
            time.sleep(0.5)


        for i in range(10):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_chulsuk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.3)




    except Exception as e:
        print(e)
        return 0



def get_post(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open
    from clean_screen_rom import clean_screen

    try:
        print("get_post")

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\action\\menu_open\\menu_restart.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 290, 930, 360, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                menu_opened = True
                print("menu_restart", imgs_.x, imgs_.y)

                # 우편
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(810, 290, 840, 320, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("get_post : menu_point", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("title_post", imgs_.x, imgs_.y)

                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\chul_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 80, 350, 105, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point 1", imgs_.x, imgs_.y)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                                time.sleep(0.5)
                                click_pos_2(865, 550, cla)
                            else:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_post.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                        time.sleep(0.5)


            else:
                result_out = out_check(cla)

                if result_out == True:
                    click_pos_2(930, 45, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\action\\menu_open\\menu_restart.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 290, 930, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                else:
                    clean_screen(cla)
            time.sleep(0.5)


        for i in range(10):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.3)




    except Exception as e:
        print(e)
        return 0


def get_upjuk(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open_pure
    from clean_screen_rom import clean_screen

    try:
        print("get_upjuk")

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            # 퀘스트 컨텐츠
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("title_quest", imgs_.x, imgs_.y)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\upjuk_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 80, 350, 105, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("upjuk_point", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)

                    time.sleep(0.5)

                    # 업적 클릭
                    for i in range(5):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(240, 105, 320, 125, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("main_quest_clicked 2", imgs_.x, imgs_.y)
                            break
                        else:
                            click_pos_2(280, 105, cla)
                        time.sleep(0.3)


                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\chul_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(110, 110, 145, 300, cla, img, 0.65)
                    if imgs_ is not None and imgs_ != False:
                        print("chul_point 4", imgs_.x, imgs_.y)
                        click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)

                        time.sleep(0.5)

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\upjuk_bosang.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 110, 960, 560, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("upjuk_bosang", imgs_.x, imgs_.y)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    menu_opened = True
                    # 퀘스트 진행중
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\quest_ing.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(235, 115, 285, 550, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("quest_ing", imgs_.x, imgs_.y)
                    else:
                        # 퀘스트 대기중
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\quest_ready.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(235, 115, 285, 550, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("quest_ready", imgs_.x, imgs_.y)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\quest_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 520, 940, 570, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("quest_move", imgs_.x, imgs_.y)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

            else:

                menu_open_pure(cla)
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\menu_quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(865, 30, 925, 85, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("menu_quest", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_quest.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 30, 950, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)







    except Exception as e:
        print(e)
        return 0


def get_mission(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open_pure
    from clean_screen_rom import clean_screen

    try:
        print("get_mission")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            # 퀘스트 컨텐츠
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 115, 800, 150, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("x_close", imgs_.x, imgs_.y)

                menu_opened = True

                # click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\mission_complete_full.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                for ix in pyautogui.locateAllOnScreen(img, region=(370 + plus, 330, 70, 475), confidence=0.97):
                    print(ix, ix.left, ix.top)
                    click_pos_reg(ix.left + 46, ix.top, cla)
                    for c in range(5):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 140, 580, 170, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("lv_close", imgs_.x, imgs_.y)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            break
                        time.sleep(0.1)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\mission_complete_full.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                for iy in pyautogui.locateAllOnScreen(img, region=(680 + plus, 330, 70, 475), confidence=0.97):
                    print(iy, iy.left, iy.top)
                    click_pos_reg(iy.left + 46, iy.top, cla)
                    for c in range(5):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 140, 580, 170, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("lv_close", imgs_.x, imgs_.y)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            break
                        time.sleep(0.1)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 115, 800, 150, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            else:

                menu_open_pure(cla)
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\menu_mission.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 130, 950, 250, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("menu_mission", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 115, 800, 150, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)







    except Exception as e:
        print(e)
        return 0

def get_sangjum(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open_pure
    from clean_screen_rom import clean_screen

    try:
        print("get_sangjum")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            # 퀘스트 컨텐츠
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(840, 30, 940, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("title_sangjum", imgs_.x, imgs_.y)

                menu_opened = True

                # 소환가기

                for i in range(7):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(80, 100, 170, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("main_quest_clicked 2", imgs_.x, imgs_.y)
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sangjum_gold.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(170, 270, 630, 315, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sangjum_gold 2", imgs_.x, imgs_.y)
                            # 소환상품 얻기
                            sohwan_get(cla)
                            break
                        else:
                            click_pos_2(50, 215, cla)
                    else:
                        click_pos_2(125, 100, cla)
                    time.sleep(0.5)

                # 일반 가기

                for i in range(7):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 100, 240, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("main_quest_clicked 2", imgs_.x, imgs_.y)
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sangjum_gold.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(170, 270, 630, 315, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sangjum_gold 2", imgs_.x, imgs_.y)
                            # 일반에서 방어구 사기
                            bangugoo_title_click(cla)
                            break
                        else:
                            click_pos_2(50, 175, cla)
                    else:
                        click_pos_2(205, 100, cla)
                    time.sleep(0.5)

                # 재화 가기

                for i in range(7):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 100, 320, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("main_quest_clicked 2", imgs_.x, imgs_.y)
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sangjum_gold.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 470, 210, 515, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sangjum_gold 2", imgs_.x, imgs_.y)
                            # 재화에서 크리스탈 랜덤 상자 사기
                            crystal_title_click(cla)
                            break
                        else:
                            click_pos_2(50, 175, cla)
                    else:
                        click_pos_2(285, 100, cla)
                    time.sleep(0.5)

                # 나가기
                clean_screen(cla)

            else:

                menu_open_pure(cla)
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\menu_sangjum.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 30, 810, 90, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("menu_sangjum", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(840, 30, 940, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\next_time_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)

            time.sleep(0.5)





    except Exception as e:
        print(e)
        return 0

def sohwan_get(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open_pure
    from clean_screen_rom import clean_screen

    try:
        print("sohwan_get")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3





        # 1_3
        for i in range(5):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sold_out.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 210, 665, 240, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sold_out", imgs_.x, imgs_.y)
                break
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sohwan_gold_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 120, 410, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 440, 615, 465, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        sangjum_click(cla)
                else:
                    click_pos_2(630, 220, cla)
            time.sleep(0.3)

        # 1_2
        for i in range(5):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sold_out.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(405, 210, 465, 240, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sold_out", imgs_.x, imgs_.y)
                break
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sohwan_gold_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 120, 410, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 440, 615, 465, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        sangjum_click(cla)
                else:
                    click_pos_2(435, 220, cla)
            time.sleep(0.3)

        # 1_1
        for i in range(5):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sold_out.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(205, 210, 265, 240, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sold_out", imgs_.x, imgs_.y)
                break
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sohwan_gold_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 120, 410, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 440, 615, 465, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        sangjum_click(cla)
                else:
                    click_pos_2(230, 220, cla)

            time.sleep(0.3)

        # 2_3
        for i in range(5):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sold_out.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 410, 665, 440, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sold_out", imgs_.x, imgs_.y)
                break
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sohwan_gold_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 120, 410, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 440, 615, 465, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        sangjum_click(cla)
                else:
                    click_pos_2(630, 430, cla)
            time.sleep(0.3)

        # 2_2
        for i in range(5):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sold_out.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(405, 410, 465, 440, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sold_out", imgs_.x, imgs_.y)
                break
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sohwan_gold_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 120, 410, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 440, 615, 465, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        sangjum_click(cla)
                else:
                    click_pos_2(430, 430, cla)
            time.sleep(0.3)

        # 2_1
        for i in range(5):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sold_out.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(205, 410, 265, 440, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sold_out", imgs_.x, imgs_.y)
                break
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sohwan_gold_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 120, 410, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 440, 615, 465, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        sangjum_click(cla)
                else:
                    click_pos_2(230, 430, cla)
            time.sleep(0.3)


    except Exception as e:
        print(e)
        return 0

def sangjum_click(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open_pure
    from clean_screen_rom import clean_screen

    try:
        print("sangjum_click")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            # 모두 열기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\all_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(410, 510, 545, 545, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("all_open", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            # 나가기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\exit_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(410, 510, 545, 545, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("exit_btn", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                menu_opened = True

            time.sleep(1)

        # 나가기
        for i in range(5):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\exit_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(410, 510, 545, 545, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("exit_btn", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.3)




    except Exception as e:
        print(e)
        return 0


def bangugoo_title_click(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open_pure
    from clean_screen_rom import clean_screen

    try:
        print("bangugoo_title_click")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            # 방어구 타이틀 열기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_joomoonser_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 120, 380, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bangugoo_joomoonser_title", imgs_.x, imgs_.y)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\5.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(440, 330, 500, 360, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("5", imgs_.x, imgs_.y)
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 440, 615, 465, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        menu_opened = True
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(540, 330, 600, 360, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("max", imgs_.x, imgs_.y)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sold_out.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(590, 200, 660, 240, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sold_out", imgs_.x, imgs_.y)
                    menu_opened = True
                else:

                    clicked = False

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_joomoonser_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 120, 380, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            clicked = True
                            break
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(130, 110, 920, 360, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)

                    if clicked == False:
                        menu_opened = True

            time.sleep(0.5)

        # 나가기
        for i in range(5):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_joomoonser_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 120, 380, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bangugoo_joomoonser_title", imgs_.x, imgs_.y)
                click_pos_2(695, 125, cla)
            time.sleep(0.3)




    except Exception as e:
        print(e)
        return 0


def crystal_title_click(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open_pure
    from clean_screen_rom import clean_screen

    try:
        print("crystal_title_click")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            # 방어구 타이틀 열기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\crystal_random_box_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 120, 380, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("crystal_random_box_title", imgs_.x, imgs_.y)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(440, 330, 500, 360, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("2", imgs_.x, imgs_.y)
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\bangugoo_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 440, 615, 465, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        menu_opened = True
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(540, 330, 600, 360, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("max", imgs_.x, imgs_.y)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\sold_out.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(175, 200, 310, 310, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sold_out", imgs_.x, imgs_.y)
                    menu_opened = True
                else:
                    click_pos_2(230, 250, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\crystal_random_box_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 120, 380, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)

            time.sleep(0.5)

        # 나가기
        for i in range(5):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\get_item\\crystal_random_box_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 120, 380, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("crystal_random_box_title", imgs_.x, imgs_.y)
                click_pos_2(695, 125, cla)
            time.sleep(0.3)




    except Exception as e:
        print(e)
        return 0

