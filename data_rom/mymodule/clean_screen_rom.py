import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def clean_screen(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, confirm_all

    try:
        print("clean_screen")

        out_ = False
        out_count = 0
        while out_ is False:
            out_count += 1
            if out_count > 7:
                out_ = True

            result_out = out_check(cla)

            if result_out == True:
                result_clean = clean_screen_start(cla)
                if result_clean == True:
                    out_ = True
                    print("out_ok")
            else:
                clean_screen_start(cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def clean_screen_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, confirm_all
    from action_rom import juljun_off

    try:
        print("clean_screen")

        clean = True

        # 모두 예 처리
        result_confirm = confirm_all(cla)
        if result_confirm == True:
            clean = False
        time.sleep(0.5)

        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            clean = False
            juljun_off(cla)

        else:
            # dead 복구 닫기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\dead_close.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 70, 250, 105, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("dead_close", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False

            # lv 닫기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 70, 250, 120, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("lv_close", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False

            # x 닫기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 140, 660, 180, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("x_close", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\lv_close.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 115, 800, 150, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("x_close", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    clean = False

            # 가방 닫기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\bag_close.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(910, 70, 960, 105, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("bag_close", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False

            # 레벨업 닫기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\bag_close.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 70, 250, 105, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("bag_close", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False

            # 메뉴 닫기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\menu_close.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(910, 30, 950, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("menu_close", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False

            # 각종 컨텐츠 닫기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\skip\\skip_5.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 480, 960, 580, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\cleen_screen\\all_close.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 30, 960, 80, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("all_close", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    clean = False


        return clean
    except Exception as e:
        print(e)
        return 0
