import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def menu_open(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_rom import clean_screen
    from get_item_rom import get_chulsuk, get_post
    from collection_rom import collection_start

    try:
        print("menu_open")

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
                print("menu_restart", imgs_.x, imgs_.y)

                # 출석
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(770, 290, 800, 320, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("get_chulsuk : menu_point", imgs_.x, imgs_.y)
                    get_chulsuk(cla)
                else:
                    # 우편
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 290, 840, 320, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("get_post : menu_point", imgs_.x, imgs_.y)
                        get_post(cla)
                    else:
                        # 콜렉
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 85, 880, 110, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("get_collection : menu_point", imgs_.x, imgs_.y)
                            if v_.collection_today == True:
                                collection_start(cla)
                            else:
                                menu_opened = True
                        else:
                            menu_opened = True


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

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        juljun_off(cla)

                    clean_screen(cla)
            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0


def menu_open_pure(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_rom import clean_screen
    from get_item_rom import get_chulsuk, get_post
    from collection_rom import collection_start

    try:
        print("menu_open_pure")

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
                print("menu_restart", imgs_.x, imgs_.y)

                menu_opened = True


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

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        juljun_off(cla)

                    clean_screen(cla)
            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from dead import dead_check, dead_recover

    try:

        out_ = False

        print("out_check")
        # 좌측 하단 키보드 설정
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\out\\out_keyboard.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 360, 40, 410, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("out_keyboard", imgs_.x, imgs_.y)
            out_ = True
        # 수시로 체크
        result_dead = dead_check(cla)
        if result_dead == True:
            dead_recover(cla)

        return out_


    except Exception as e:
        print(e)
        return 0

def juljun_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:

        juljun_ = False

        print("juljun_check")
        # 튜토 완료 확인
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("juljun_on", imgs_.x, imgs_.y)
            juljun_ = True

        return juljun_

    except Exception as e:
        print(e)
        return 0

def juljun_on(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_rom import clean_screen

    try:

        for i in range(10):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("juljun_on", imgs_.x, imgs_.y)
                break
            else:
                result_out = out_check(cla)

                if result_out == True:
                    click_pos_2(16, 420, cla)

                    for c in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("juljun_on", imgs_.x, imgs_.y)
                            break
                        time.sleep(0.2)

                else:
                    clean_screen(cla)
            time.sleep(0.3)


        juljun_ = False

        print("juljun_check")
        # 튜토 완료 확인
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("juljun_on", imgs_.x, imgs_.y)
            juljun_ = True

        return juljun_

    except Exception as e:
        print(e)
        return 0

def juljun_off(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    try:
        # 튜토 완료 확인
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            drag_pos(470, 250, 900, 250, cla)

            for i in range(10):
                result_out = out_check(cla)
                if result_out == True:
                    break
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        drag_pos(470, 250, 900, 250, cla)
                time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def confirm_all(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:

        clicked = False

        print("confirm_all")
        # 튜토 완료 확인
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\confirm\\tuto_complete_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(490, 340, 600, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("tuto_complete_confirm", imgs_.x, imgs_.y)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            clicked = True
        else:
            # 튜토 이동 확인
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\confirm\\tuto_move_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 300, 700, 600, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("tuto_move_confirm", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clicked = True

        return clicked

    except Exception as e:
        print(e)
        return 0

def moving_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:

        move_ = False

        print("moving")
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\move\\move_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 350, 600, 380, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("move_1", imgs_.x, imgs_.y)
            move_ = True
        else:
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\move\\move_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(470, 350, 600, 380, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("move_2", imgs_.x, imgs_.y)
                move_ = True
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\move\\move_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 350, 600, 380, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("move_3", imgs_.x, imgs_.y)
                    move_ = True


        return move_

    except Exception as e:
        print(e)
        return 0
