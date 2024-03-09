import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, huntig_check
    from potion_rom import juljun_potion_check, potion_buy

    try:
        print("jadong_start")

        # 절전 던전 모드 확인하기
        result_check = jadong_check(cla)

        if result_check == True:

            huntig_check(cla, "자동사냥")

            # print("정상 자동 사냥 중")
            # # 물약 파악
            # result_potion = juljun_potion_check(cla)
            # if result_potion == False:
            #     potion_buy(cla)

        else:
            # 사냥터로 이동
            jadong_spot(cla)


    except Exception as e:
        print(e)
        return 0


def jadong_spot(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, juljun_off, juljun_on
    from clean_screen_rom import clean_screen

    try:
        print("jadong_spot")



        jd_ = False
        jd_count = 0
        while jd_ is False:
            jd_count += 1
            if jd_count > 7:
                jd_ = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_worldmap.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 30, 940, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("title_worldmap", imgs_.x, imgs_.y)
                # click_pos_reg(imgs_.x, imgs_.y, cla)
                for i in range(5):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\jadong\\jadong_move_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 340, 620, 420, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    else:



                        click_pos_2(25, 205, cla)
                        time.sleep(0.5)
                        click_pos_2(130, 170, cla)
                        time.sleep(0.5)


                        # detil om
                        for d in range(10):

                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\jadong\\detail_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(910, 100, 960, 150, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\jadong\\detail_off.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(910, 100, 960, 150, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        ###
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\jadong\\move_zero.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(795, 525, 870, 555, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("move_zero", imgs_.x, imgs_.y)
                            clean_screen(cla)
                            break
                        else:
                            click_pos_2(810, 540, cla)
                            time.sleep(0.5)
                for i in range(20):
                    result_out = out_check(cla)
                    if result_out == True:

                        result_hunting = jadong_check(cla)
                        if result_hunting == False:
                            juljun_off(cla)
                            time.sleep(0.2)
                            click_pos_2(895, 455, cla)
                            time.sleep(0.2)
                            juljun_on(cla)


                        jd_ = True
                        break
                    else:
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\jadong\\jadong_move_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 340, 620, 420, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)

            else:
                result_out = out_check(cla)

                if result_out == True:
                    print("out_ok")
                    click_pos_2(60, 125, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_worldmap.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 30, 940, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                else:
                    juljun_off(cla)
                    clean_screen(cla)

            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def jadong_check(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open, juljun_on, crash_check
    from massenger import line_to_me

    try:
        print("jadong_check")

        hunting_ = False

        dun_ = False
        dun_count = 0
        while dun_ is False:
            dun_count += 1
            if dun_count > 7:
                dun_ = True

            # 절전 던전 모드 확인하기
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                dun_ = True

                print("절전모드")

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_logout.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 80, 520, 140, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("튕김")
                    why = "롬 자동 사냥 중 튕겼다.."
                    crash_check(cla, why)
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_hunting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 110, 550, 165, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        hunting_ = True


            else:
                juljun_on(cla)
                for i in range(10):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
            time.sleep(0.5)
        return hunting_
    except Exception as e:
        print(e)
        return 0

