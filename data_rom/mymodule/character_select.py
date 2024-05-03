import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def character_screen_check(cla, character_id):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check
    from massenger import line_to_me

    try:
        print("character_screen_check")


        screen_ready = False

        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\character_select\\game_start.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(810, 520, 940, 560, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            screen_ready = True
        else:
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\character_select\\server_join_ready.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(410, 170, 530, 215, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                screen_ready = True

        if screen_ready == True:

            character_id = int(character_id)

            selected_ = False
            selected__count = 0
            while selected_ is False:
                selected__count += 1
                if selected__count > 7:
                    selected_ = True



                # 스타트버튼
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\character_select\\game_start.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(810, 520, 940, 560, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("game_start", imgs_.x, imgs_.y)

                    # character_id
                    # 140, 205, 270,  335, 400
                    my_id = 75 + (character_id * 65)

                    click_pos_2(905, my_id, cla)
                    time.sleep(0.5)

                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(20):
                        result_out = out_check(cla)
                        if result_out == True:
                            selected_ = True
                            break
                        else:
                            print("게임 진입 중")
                        time.sleep(1)
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\character_select\\server_join_ready.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 170, 530, 215, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        selected__count = 0
                        print("서버 접속 대기")
                        for i in range(100):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\character_select\\game_start.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(810, 520, 940, 560, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                why = "롬 접속 시도 한다."
                                line_to_me(cla, why)
                                break
                            time.sleep(1)
                time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



