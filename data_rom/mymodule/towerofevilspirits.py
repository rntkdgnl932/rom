import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tower_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check
    from schedule import myQuest_play_add, myQuest_play_check
    from dead import dead_check, dead_recover

    try:
        print("tower_start")

        # 현재 진행중인지 체크
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\towerofevilspirits\\tower_in.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 70, 100, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            result_dead = dead_check(cla)
            if result_dead == True:
                dead_recover(cla)
        else:
            # 진행중이지 않다면 악령의 탑 시작하기
            tower_in(cla)

    except Exception as e:
        print(e)
        return 0


def tower_in(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, confirm_all, menu_open_pure
    from clean_screen_rom import clean_screen
    from massenger import line_to_me
    from schedule import myQuest_play_add


    try:
        print("tower_in")

        # 타워로 들어가기

        tower_in = False
        tower_in_count = 0

        while tower_in is False:
            tower_in_count += 1
            if tower_in_count > 10:
                tower_in = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\towerofevilspirits\\tower_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 70, 100, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                tower_in = True
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\towerofevilspirits\\evil_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 30, 950, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\towerofevilspirits\\all_clear.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(880, 470, 960, 510, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        tower_in = True
                        myQuest_play_add(cla, "악령의탑")
                    else:
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\towerofevilspirits\\progress_order.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 520, 850, 570, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            confirm_all(cla)
                        else:
                            click_pos_2(650, 540, cla)

                else:
                    menu_open_pure(cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\towerofevilspirits\\menu_tower.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 170, 950, 300, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        time.sleep(0.5)


            time.sleep(0.5)



        # 타워로 들어가려는데 모두 소진했다면 스케쥴 add
        # 타워 도중 죽어도 스케쥴 add



    except Exception as e:
        print(e)
        return 0



