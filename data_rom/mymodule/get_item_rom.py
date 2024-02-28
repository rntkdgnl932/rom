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

    try:
        print("get_item_start")



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
                            imgs_ = imgs_set_(80, 90, 240, 120, cla, img, 0.65)
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
                                imgs_ = imgs_set_(80, 90, 240, 120, cla, img, 0.65)
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
                            imgs_ = imgs_set_(50, 80, 250, 105, cla, img, 0.7)
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
    from action_rom import out_check, menu_open
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
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\tuto\\main_quest_clicked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(240, 105, 320, 125, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("main_quest_clicked 2", imgs_.x, imgs_.y)
                            break
                        else:
                            click_pos_2(280, 105, cla)
                        time.sleep(0.3)


                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\chul_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(110, 110, 145, 300, cla, img, 0.7)
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

                menu_open(cla)
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


