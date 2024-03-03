import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def auction_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from property_rom import my_property_upload
    from schedule import myQuest_play_add, myQuest_play_check
    from action_rom import menu_open
    from clean_screen_rom import clean_screen

    try:
        print("auction_start")

        auction_in = False
        auction_in_count = 0
        while auction_in is False:
            auction_in_count += 1
            if auction_in_count > 7:
                auction_in = True
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 30, 940, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                auction_in = True

                # 정산부터 체크하기

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\point_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(210, 70, 260, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 30, imgs_.y + 8, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\clicked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(170, 100, 240, 125, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\calculate.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(820, 530, 930, 570, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)



                # 판매하기 클릭
                for i in range(10):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 100, 155, 125, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(130, 105, cla)
                    time.sleep(0.5)
                # 회수하기
                for i in range(10):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\recall.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(560, 130, 690, 530, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for c in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\recall_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 370, 600, 410, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            time.sleep(0.3)

                    else:
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\recall_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(490, 370, 600, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                    time.sleep(0.5)
                # 판매 시작하기

                for z in range(4):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\all_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(900, 150, 925, 220, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(930, 185, cla)
                    time.sleep(0.5)

                file_path_1 = "C:\\my_games\\rom\\data_rom\\imgs\\auction\\list_10.txt"
                file_path_2 = "C:\\my_games\\rom\\data_rom\\imgs\\auction\\list_all.txt"
                ###
                with open(file_path_1, "r", encoding='utf-8-sig') as file:
                    jaelyo_1_ready = file.read().splitlines()
                    print("jaelyo_1_ready", jaelyo_1_ready)
                with open(file_path_2, "r", encoding='utf-8-sig') as file:
                    jaelyo_2_ready = file.read().splitlines()
                    print("jaelyo_2_ready", jaelyo_2_ready)
                ##jaelyo_1_ready##
                for i in range(len(jaelyo_1_ready)):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\list\\" + jaelyo_1_ready[i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 130, 920, 530, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("거래물건 있음", jaelyo_1_ready[i])
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for e in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\auction_enroll_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 100, 530, 140, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\dia_ten.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(520, 430, 600, 455, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(430, 490, cla)
                                    for v in range(10):
                                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\dia_ten.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(520, 430, 600, 455, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(430, 490, cla)
                                        else:
                                            break
                                        time.sleep(0.2)
                                    break
                                else:
                                    click_pos_2(545, 490, cla)
                                    for v in range(10):
                                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\sell_enroll_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(430, 190, 520, 230, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(0.2)

                                time.sleep(0.5)

                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\sell_enroll_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 190, 520, 230, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\recall_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 370, 600, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break

                            time.sleep(0.5)
                        # 혹시 모를 마무리
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\sell_enroll_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 190, 520, 230, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            for x in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\recall_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 370, 600, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    break
                                time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\auction_enroll_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 100, 530, 140, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                for x in range(10):
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\dia_ten.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(520, 430, 600, 455, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(430, 490, cla)
                                    else:
                                        break
                                    time.sleep(0.5)

                    time.sleep(0.5)
                ##jaelyo_2_ready##
                for i in range(len(jaelyo_2_ready)):
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\list\\" + jaelyo_2_ready[
                        i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 130, 920, 530, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("거래물건 있음", jaelyo_2_ready[i])
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for e in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\auction_enroll_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 100, 530, 140, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(545, 490, cla)
                                for v in range(10):
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\sell_enroll_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(430, 190, 520, 230, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.2)

                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\sell_enroll_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 190, 520, 230, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\recall_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 370, 600, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break

                            time.sleep(0.5)
                        # 혹시 모를 마무리
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\sell_enroll_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 190, 520, 230, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            for x in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\recall_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 370, 600, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    break
                                time.sleep(0.5)
                    time.sleep(0.5)

                # 골드, 다이아 업로드
                my_property_upload(cla)
                time.sleep(0.5)

                # 마무리 나가기
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(830, 30, 940, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    clean_screen(cla)
            else:
                menu_open(cla)
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\menu_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(720, 30, 960, 90, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(830, 30, 940, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\menu_auction.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(720, 30, 960, 90, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                if i > 7:
                                    auction_in = True
                        time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0



