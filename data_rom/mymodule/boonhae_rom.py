import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def boonhae_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check
    from schedule import myQuest_play_add, myQuest_play_check
    from clean_screen_rom import clean_screen

    try:
        print("boonhae_start")

        boonhae_ = False
        boonhae_count = 0
        while boonhae_ is False:
            boonhae_count += 1
            if boonhae_count > 7:
                boonhae_ = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 80, 780, 115, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(705, 385, 745, 420, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("checked 1", imgs_)
                else:
                    click_pos_2(750, 405, cla)
                    time.sleep(0.3)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(770, 385, 810, 420, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("checked 2", imgs_)
                else:
                    click_pos_2(810, 405, cla)
                    time.sleep(0.3)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\0_20.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 385, 940, 420, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("0_20 0_20 0_20", imgs_)
                    boonhae_ = True
                else:
                    click_pos_2(900, 405, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_result.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 130, 520, 170, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("boonhae_title", imgs_)
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 400, 600, 440, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("boonhae_confirm", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\last_boonhae_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(340, 100, 600, 380, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("last_boonhae_title", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break

                        time.sleep(0.2)


            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(855, 50, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\bag_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 80, 780, 115, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(760, 385, 820, 425, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for x in range(10):
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(700, 80, 780, 115, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.2)
                            break
                        time.sleep(0.5)
                else:
                    clean_screen(cla)

            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0


def auction_ready_boonhae_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check
    from schedule import myQuest_play_add, myQuest_play_check
    from clean_screen_rom import clean_screen

    try:
        print("boonhae_start")

        boonhae_ = False
        boonhae_count = 0
        while boonhae_ is False:
            boonhae_count += 1
            if boonhae_count > 7:
                boonhae_ = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 80, 780, 115, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(705, 385, 745, 420, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("checked 1", imgs_)
                else:
                    click_pos_2(750, 405, cla)
                    time.sleep(0.3)

                # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\checked.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(770, 385, 810, 420, cla, img, 0.8)
                # if imgs_ is not None and imgs_ != False:
                #     print("checked 2", imgs_)
                # else:
                #     click_pos_2(810, 405, cla)
                #     time.sleep(0.3)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\0_20.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 385, 940, 420, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("0_20 0_20 0_20", imgs_)
                    boonhae_ = True
                else:
                    click_pos_2(900, 405, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_result.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 130, 520, 170, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("boonhae_title", imgs_)
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 400, 600, 440, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("boonhae_confirm", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\last_boonhae_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(340, 100, 600, 380, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("last_boonhae_title", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break

                        time.sleep(0.2)


            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(855, 50, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\bag_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 80, 780, 115, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(760, 385, 820, 425, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for x in range(10):
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\boonhae\\boonhae_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(700, 80, 780, 115, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.2)
                            break
                        time.sleep(0.5)
                else:
                    clean_screen(cla)

            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0
