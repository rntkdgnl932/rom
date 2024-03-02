import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def collection_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open_pure
    from clean_screen_rom import clean_screen

    try:
        print("collection_start")

        collect_ = False
        collect_count = 0
        while collect_ is False:
            collect_count += 1
            if collect_count > 7:
                collect_ = True
                v_.collection_today = False
                clean_screen(cla)

            # 스타트버튼
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_collect.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 30, 940, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("title_collect", imgs_.x, imgs_.y)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\collection\\col_title_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(140, 80, 600, 110, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    collect_count = 3

                    print("col_title_point", imgs_)
                    click_pos_2(50, 105, cla)
                    time.sleep(0.2)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

                    for c in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\collection\\col_des_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 120, 350, 540, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("col_des_point 1", imgs_)
                            click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\collection\\col_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(550, 420, 640, 460, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\collection\\col_des_point.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 120, 350, 540, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("col_des_point 2", imgs_)
                                        click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                                time.sleep(0.2)

                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\collection\\col_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 350, 600, 380, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(444, 333, cla)
                                time.sleep(0.2)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                        else:
                            print("e n d")
                            break
                        time.sleep(0.1)
                else:
                    collect_count += 1
            else:
                menu_open_pure(cla)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\collection\\menu_collect.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 80, 930, 150, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_collect.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(830, 30, 940, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



