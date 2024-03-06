import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def request_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_rom import menu_open, confirm_all
    from get_item_rom import get_upjuk
    from schedule import myQuest_play_add

    try:
        print("request_start")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        # 퀘스트 컨텐츠
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_quest.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(870, 30, 940, 80, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("title_quest", imgs_.x, imgs_.y)

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\upjuk_point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 80, 350, 105, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("upjuk_point", imgs_.x, imgs_.y)
                get_upjuk(cla)

            else:
                # 의뢰 클릭
                for i in range(10):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 105, 250, 125, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("main_quest_clicked 1", imgs_.x, imgs_.y)
                        time.sleep(0.2)
                        break
                    else:
                        click_pos_2(205, 105, cla)
                    time.sleep(0.3)

                # 의뢰 보상받기
                for i in range(10):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\re_complete.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(235, 115, 290, 450, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("re_complete", imgs_.x, imgs_.y)
                        click_pos_2(870, 550, cla)
                        time.sleep(0.2)
                    else:
                        break
                    time.sleep(0.3)

                # 의뢰 완료 되었는지 파악

                re_complete_ = False

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\re_zero_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(65, 445, 100, 470, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("re_zero_1", imgs_)
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\re_zero_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 445, 285, 470, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("re_zero_2", imgs_)
                        re_complete_ = True

                if re_complete_ == True:
                    myQuest_play_add(cla, "의뢰하기")
                else:

                    # 의뢰 진행중인지 파악
                    re_ing = False

                    for i in range(3):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\request_ing.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(235, 115, 290, 450, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("request_ing", imgs_.x, imgs_.y)
                            re_ing = True
                            break
                        else:
                            drag_pos(170, 380, 170, 140, cla)
                        time.sleep(0.3)

                    if re_ing == True:
                        # 퀘스트 진행중
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\request_ing.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(235, 115, 290, 450, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("request_ing", imgs_.x, imgs_.y)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.3)

                            # 레벨 맞는지 다시 체크

                            over_lv = True

                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\30_39.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 120, 600, 180, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                over_lv = False
                            else:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\30_39_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 120, 600, 180, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    over_lv = False
                                else:
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\40_49.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 120, 600, 180, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        over_lv = False
                                    else:
                                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\40_49_3.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(300, 120, 600, 180, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            over_lv = False
                            if over_lv == False:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\quest_ing_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 520, 940, 570, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("퀘스트 진행중")
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)

                                    for c in range(10):
                                        result_move = confirm_all(cla)
                                        if result_move == True:
                                            break
                                        time.sleep(0.2)

                                for i in range(50):
                                    result_tuto = tuto_ing(cla)
                                    if result_tuto == True:
                                        break
                                    time.sleep(1)
                            else:
                                click_pos_2(730, 550, cla)
                                for i in range(10):
                                    result_confirm = confirm_all(cla)
                                    if result_confirm == True:
                                        break
                                    time.sleep(0.3)

                    else:
                        # 의뢰 대기중
                        click_pos_2(125, 105, cla)
                        time.sleep(0.5)
                        for p in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(170, 105, 250, 125, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\re_ready.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                # 235, 115, 290, 450
                                for ix in pyautogui.locateAllOnScreen(img, region=(235 + plus, 115, 55, 335),
                                                                      confidence=0.85):
                                    print(ix, ix.left, ix.top)
                                    click_pos_reg(ix.left, ix.top, cla)

                                    time.sleep(0.3)

                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\30_39.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 120, 600, 180, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(870, 550, cla)
                                    else:
                                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\30_39_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(300, 120, 600, 180, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(870, 550, cla)
                                        else:
                                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\40_49.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(300, 120, 600, 180, cla, img, 0.9)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_2(870, 550, cla)
                                            else:
                                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\request\\40_49_3.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(300, 120, 600, 180, cla, img, 0.9)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_2(870, 550, cla)
                                                else:
                                                    pass
                                    time.sleep(0.7)


                                break
                            else:
                                click_pos_2(205, 105, cla)
                            time.sleep(1)
        else:

            tuto_ing(cla)

            menu_open(cla)
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\menu_quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 30, 925, 85, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("menu_quest", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_quest.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(870, 30, 940, 80, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def tuto_ing(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from potion_rom import out_potion_check, potion_buy

    try:
        print("tuto_ing")

        tuto_complete = False

        # 레벨업 포인트
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\lv_point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(25, 30, 50, 50, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("lv_point", imgs_.x, imgs_.y)
            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)

            for i in range(10):
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\lv\\status.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 80, 85, 115, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\lv\\zero.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 110, 220, 145, cla, img, 0.88)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(200, 375, cla)
                        break
                    else:
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\lv\\zero2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(170, 110, 220, 145, cla, img, 0.88)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(200, 375, cla)
                            break
                        else:
                            click_pos_2(210, 225, cla)
                    time.sleep(0.2)
                else:
                    time.sleep(0.3)
            for i in range(10):
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\bag_close.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 70, 250, 105, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("bag_close", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    break
                time.sleep(0.3)
        # 우측 상단 스킵
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 10, 960, 80, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_.x, imgs_.y)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\skip\\skip_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 10, 960, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("skip_2", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\skip\\skip_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(830, 530, 960, 580, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("skip_3", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\skip\\skip_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 10, 960, 80, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("skip_4", imgs_.x, imgs_.y)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

        # 하단 대화 스킵
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\skip\\skip_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(830, 480, 960, 580, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("skip_5", imgs_.x, imgs_.y)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 퀘스트 완료
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\tuto_complete.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 220, 530, 260, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("tuto_complete", imgs_.x, imgs_.y)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            tuto_complete = True

        # 물약 체크
        result_potion = out_potion_check(cla)
        if result_potion == True:
            print("물약 있음")
        else:
            print("물약 없어서 사러 가야함")
            potion_buy(cla)



        return tuto_complete

    except Exception as e:
        print(e)
        return 0

