import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def potion_buy(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, juljun_off, moving_check
    from clean_screen_rom import clean_screen
    from get_item_rom import get_chulsuk

    try:
        print("potion_buy")

        buy_ = False
        buy_count = 0
        while buy_ is False:
            buy_count += 1
            if buy_count > 7:
                buy_ = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                juljun_off(cla)
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\maul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 70, 50, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    buy_ = True

                    print("마을이다")
                    get_chulsuk(cla)
                    clean_screen(cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_jabhwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 30, 950, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            # 물약사기
                            potion_buy_start(cla)
                            time.sleep(0.5)
                            clean_screen(cla)
                            break
                        else:
                            result_moving = moving_check(cla)
                            if result_moving == False:
                                click_pos_2(65, 210, cla)
                            else:
                                click_pos_2(75, 210, cla)
                                time.sleep(0.5)
                        time.sleep(1)

                else:
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\maul.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 70, 50, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\maul_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(315, 520, 350, 560, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                clean_screen(cla)
                        time.sleep(0.5)

            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def potion_buy_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, juljun_off, moving_check
    from clean_screen_rom import clean_screen

    try:
        print("potion_buy_start")

        buy_ = False
        buy_count = 0
        while buy_ is False:
            buy_count += 1
            if buy_count > 7:
                buy_ = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_jabhwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 30, 950, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:



                # # 내 가방 확인용 클릭
                # for i in range(10):
                #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\clicked.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(900, 200, 930, 260, cla, img, 0.7)
                #     if imgs_ is not None and imgs_ != False:
                #         print("clicked 1", imgs_)
                #         break
                #     else:
                #         click_pos_2(935, 235, cla)
                #     time.sleep(0.5)
                # # 내 잡화 물약 클릭
                # for i in range(10):
                #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\clicked.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(25, 150, 55, 210, cla, img, 0.7)
                #     if imgs_ is not None and imgs_ != False:
                #         print("clicked 2", imgs_)
                #         break
                #     else:
                #         click_pos_2(23, 185, cla)
                #     time.sleep(0.5)

                # # 내 잡화 큰 물약 사기
                #
                # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\full_potion.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(110, 130, 200, 160, cla, img, 0.7)
                # if imgs_ is not None and imgs_ != False:
                #     buy_ = True
                # else:
                #
                #     for i in range(10):
                #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\buy_title.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(450, 150, 550, 210, cla, img, 0.7)
                #         if imgs_ is not None and imgs_ != False:
                #             print("buy_title", imgs_)
                #             full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\big_potion_des.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(360, 190, 470, 230, cla, img, 0.7)
                #             if imgs_ is not None and imgs_ != False:
                #
                #                 full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\max2.PNG"
                #                 img_array = np.fromfile(full_path, np.uint8)
                #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                 imgs_ = imgs_set_(520, 250, 590, 300, cla, img, 0.7)
                #                 if imgs_ is not None and imgs_ != False:
                #                     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\buy_confirm.PNG"
                #                     img_array = np.fromfile(full_path, np.uint8)
                #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                     imgs_ = imgs_set_(500, 400, 640, 440, cla, img, 0.7)
                #                     if imgs_ is not None and imgs_ != False:
                #                         click_pos_reg(imgs_.x, imgs_.y, cla)
                #                         break
                #                 else:
                #                     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\max.PNG"
                #                     img_array = np.fromfile(full_path, np.uint8)
                #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                     imgs_ = imgs_set_(560, 290, 660, 350, cla, img, 0.7)
                #                     if imgs_ is not None and imgs_ != False:
                #                         click_pos_reg(imgs_.x, imgs_.y, cla)
                #
                #
                #         else:
                #             full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\big_potion.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(40, 110, 110, 450, cla, img, 0.7)
                #             if imgs_ is not None and imgs_ != False:
                #                 click_pos_reg(imgs_.x + 80, imgs_.y, cla)
                #         time.sleep(0.5)
                #
                #     # 내 잡화 양고기 사기
                #     for i in range(10):
                #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\buy_title.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(450, 150, 550, 210, cla, img, 0.7)
                #         if imgs_ is not None and imgs_ != False:
                #             print("buy_title", imgs_)
                #             full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\yangogi_des.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(360, 190, 470, 230, cla, img, 0.7)
                #             if imgs_ is not None and imgs_ != False:
                #
                #                 full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\plus10.PNG"
                #                 img_array = np.fromfile(full_path, np.uint8)
                #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                 imgs_ = imgs_set_(380, 295, 460, 340, cla, img, 0.7)
                #                 if imgs_ is not None and imgs_ != False:
                #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                #
                #                     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\buy_confirm.PNG"
                #                     img_array = np.fromfile(full_path, np.uint8)
                #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                     imgs_ = imgs_set_(500, 400, 640, 440, cla, img, 0.7)
                #                     if imgs_ is not None and imgs_ != False:
                #                         click_pos_reg(imgs_.x, imgs_.y, cla)
                #                         break
                #
                #
                #
                #         else:
                #             full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\yangogi.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(40, 110, 110, 450, cla, img, 0.7)
                #             if imgs_ is not None and imgs_ != False:
                #                 click_pos_reg(imgs_.x + 80, imgs_.y, cla)
                #         time.sleep(0.5)
                #
                #
                #     # 내 잡화 주문서 클릭
                #     for i in range(10):
                #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\clicked.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(25, 205, 55, 260, cla, img, 0.7)
                #         if imgs_ is not None and imgs_ != False:
                #             print("clicked 3", imgs_)
                #             break
                #         else:
                #             click_pos_2(23, 233, cla)
                #         time.sleep(0.5)
                #
                #     # 내 잡화 마을 귀환서 사기
                #     for i in range(10):
                #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\buy_title.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(450, 150, 550, 210, cla, img, 0.7)
                #         if imgs_ is not None and imgs_ != False:
                #             print("buy_title", imgs_)
                #             full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\plus10.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(380, 295, 460, 340, cla, img, 0.7)
                #             if imgs_ is not None and imgs_ != False:
                #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                #
                #                 full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\buy_confirm.PNG"
                #                 img_array = np.fromfile(full_path, np.uint8)
                #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                 imgs_ = imgs_set_(500, 400, 640, 440, cla, img, 0.7)
                #                 if imgs_ is not None and imgs_ != False:
                #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                #                     break
                #         else:
                #             full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\jab_maul.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(40, 110, 110, 505, cla, img, 0.7)
                #             if imgs_ is not None and imgs_ != False:
                #                 click_pos_reg(imgs_.x + 80, imgs_.y, cla)
                #         time.sleep(0.5)
                #
                #     # 내 잡화 텔레포트 사기
                #     for i in range(10):
                #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\buy_title.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(450, 150, 550, 210, cla, img, 0.7)
                #         if imgs_ is not None and imgs_ != False:
                #             print("buy_title", imgs_)
                #             full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\plus10.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(380, 295, 460, 340, cla, img, 0.7)
                #             if imgs_ is not None and imgs_ != False:
                #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                #
                #                 full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\buy_confirm.PNG"
                #                 img_array = np.fromfile(full_path, np.uint8)
                #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                 imgs_ = imgs_set_(500, 400, 640, 440, cla, img, 0.7)
                #                 if imgs_ is not None and imgs_ != False:
                #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                #                     break
                #         else:
                #             full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\jab_teleport.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(40, 110, 110, 505, cla, img, 0.7)
                #             if imgs_ is not None and imgs_ != False:
                #                 click_pos_reg(imgs_.x + 80, imgs_.y, cla)
                #         time.sleep(0.5)

                # 자동 사기로 대체함
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\full_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(110, 130, 200, 160, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("full_potion", imgs_.x, imgs_.y)
                    buy_ = True
                else:
                    click_pos_2(820, 550, cla)


            else:
                potion_buy(cla)
                buy_ = True

            time.sleep(0.5)

    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\bag_maul.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(700, 110, 930, 505, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("bag_maul 1", imgs_)
    #
    # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\bag_teleport.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(700, 110, 930, 505, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("bag_teleport 1", imgs_)

    except Exception as e:
        print(e)
        return 0



def juljun_potion_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, juljun_on
    from collection_rom import collection_start
    from boonhae_rom import boonhae_start

    try:
        print("juljun_potion_check")

        is_potion = True

        check_ = False
        check_count = 0
        while check_ is False:
            check_count += 1
            if check_count > 7:
                check_ = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                check_ = True

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\juljun_potion_zero.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 30, 740, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("물약 없다")
                    is_potion = False
                else:
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\juljun_number\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 45, 700, 75, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("물약 100 자릿수 number is... ", i)
                            break

                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\juljun_number\\no_number.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 45, 700, 75, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("물약 100개 이하.......")
                            is_potion = False
                            break

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\full_bag_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(720, 50, 780, 85, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("가방 꽉 찼다")
                    v_.collection_today = True
                    if v_.onCollection == True:
                        collection_start(cla)
                        time.sleep(0.5)
                    boonhae_start(cla)
                    time.sleep(0.5)
                    juljun_on(cla)


            else:
                juljun_on(cla)

            time.sleep(0.5)

        return is_potion
    except Exception as e:
        print(e)
        return 0

def out_potion_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, juljun_on
    from clean_screen_rom import clean_screen

    try:
        print("out_potion_check")

        is_potion = True

        check_ = False
        check_count = 0
        while check_ is False:
            check_count += 1
            if check_count > 7:
                check_ = True

            result_out = out_check(cla)

            if result_out == True:

                check_ = True

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\out_big_zero.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 540, 725, 570, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("out_big_zero 1", imgs_.x, imgs_.y)
                    is_potion = False
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\out_small_zero.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 540, 725, 570, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("out_small_zero 2", imgs_.x, imgs_.y)
                        is_potion = False
                    else:
                        # 707, 552, 712, 560
                        for i in range(10):
                            print("현재 숫자", i)
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\out_number\\" + str(i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 530, 713, 560, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("물약 100 자릿수 number is... ", i)
                                break

                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\potion\\out_number\\no_number.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 530, 713, 560, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("물약 100개 이하.......")
                                is_potion = False
                                break


            else:
                clean_screen(cla)

            time.sleep(0.5)

        return is_potion
    except Exception as e:
        print(e)
        return 0