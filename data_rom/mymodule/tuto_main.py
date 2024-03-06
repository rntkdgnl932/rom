import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import menu_open, confirm_all
    from get_item_rom import get_upjuk

    try:
        print("tuto_start")

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
                # 메인퀘스트 클릭
                for i in range(10):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 105, 90, 125, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("main_quest_clicked 1", imgs_.x, imgs_.y)
                        break
                    else:
                        click_pos_2(50, 105, cla)
                    time.sleep(0.3)

                # 퀘스트 진행중
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\quest_ing.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(235, 115, 285, 550, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("quest_ing", imgs_.x, imgs_.y)

                    complete_ = False

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\quest_complete.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 520, 940, 570, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("퀘스트 complete", imgs_)
                        complete_ = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    if complete_ == True:
                        for c in range(10):
                            result_click = confirm_all(cla)
                            if result_click == True:
                                break
                            else:
                                time.sleep(0.3)
                    else:
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\quest_ing_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 520, 940, 570, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("퀘스트 진행중")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for c in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\out_quest.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(750, 75, 795, 115, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("out_quest", imgs_.x, imgs_.y)
                                    click_pos_2(905, 90, cla)
                                    break
                                time.sleep(0.2)
                            for c in range(10):
                                result_move = confirm_all(cla)
                                if result_move == True:
                                    break
                                time.sleep(0.2)
                        else:
                            click_pos_2(875, 550, cla)

                        for i in range(20):
                            result_tuto = tuto_ing(cla)
                            if result_tuto == True:
                                break
                            time.sleep(1)

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
                        click_pos_2(125, 105, cla)
                        time.sleep(0.5)
                        for p in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(5, 105, 80, 125, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\quest_ready.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(235, 115, 285, 550, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    break
                            else:
                                click_pos_2(45, 105, cla)
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
                            for lv in range(2):
                                click_pos_2(210, 225, cla)
                                time.sleep(0.4)
                            click_pos_2(210, 339, cla)
                            time.sleep(0.2)

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
            time.sleep(1)
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

        return tuto_complete

    except Exception as e:
        print(e)
        return 0

