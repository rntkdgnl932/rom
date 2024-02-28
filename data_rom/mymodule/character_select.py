import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def character_screen_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check

    try:
        print("character_screen_check")

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
            imgs_ = imgs_set_(910, 70, 960, 105, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("bag_close", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)

                for i in range(20):
                    result_out = out_check(cla)
                    if result_out == True:
                        selected_ = True
                    else:
                        print("게임 진입 중")
                    time.sleep(0.5)

            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



