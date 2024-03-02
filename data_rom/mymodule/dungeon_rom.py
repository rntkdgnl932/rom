import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dungeon_start(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open, juljun_off, juljun_on
    from potion_rom import juljun_potion_check

    try:
        print("dungeon_start", data)

        # 절전 던전 모드 확인하기
        result_check = dungeon_check(cla, data)

        if result_check[0] == True and result_check[1] == True:
            print("정상 사냥 중", data)
            # 물약 파악
            juljun_potion_check(cla)

        elif result_check[0] == False:
            # 사냥터로 이동
            dun_ = False
            dun_count = 0
            while dun_ is False:
                dun_count += 1
                if dun_count > 7:
                    dun_ = True

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 30, 950, 80, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    dun_ = True

                    print("title_dungeon", imgs_.x, imgs_.y)
                    # 던전 입장
                    dungeon_join(cla, data)

                else:
                    menu_open(cla)

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\menu_dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(740, 170, 935, 300, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_dungeon", imgs_.x, imgs_.y)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_dungeon.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 30, 950, 80, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)
                time.sleep(0.5)
        elif result_check[1] == False:
            # 절전풀고 공격하기
            juljun_off(cla)
            click_pos_2(910, 450, cla)
            juljun_on(cla)



    except Exception as e:
        print(e)
        return 0

def dungeon_join(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import menu_open, out_check
    from schedule import myQuest_play_add

    try:
        print("dungeon_join", data)

        complete_dun = False

        # 던전_일반_고대미궁_1,2
        # 던전_일반_카타콤_1,2,3
        # 던전_일반_드베르그_1,2,3(시간제한)
        # 던전_일반_사막동굴_1,2
        # 던전_일반_지하신전_1,2
        # 던전_특수_환영의유적_1~5(시간제한)
        # 던전_특수_시간의미궁_1~5(시간제한)
        # 던전_특수_얼음신전_1~5(시간제한)
        # 던전_특수_혼돈의성채_1,2(시간제한_일주일)
        # 던전_특수_정령의성채_1,2(시간제한_일주일)

        dun_ = data.split("_")
        dun_1 = dun_[1] # 일반, 특수
        dun_2 = dun_[2] # 종류
        dun_3 = dun_[3] # 층수
        print("던전정보", dun_1, dun_2, dun_3)

        dun_ = False
        dun_count = 0
        while dun_ is False:
            dun_count += 1
            if dun_count > 7:
                dun_ = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_dungeon.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 950, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("title_dungeon", imgs_.x, imgs_.y)

                dun_ = True

                if dun_1 == "일반":
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_clicked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(15, 100, 90, 130, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("dun_clicked", imgs_.x, imgs_.y)
                            break
                        else:
                            click_pos_2(50, 105, cla)
                        time.sleep(0.5)

                    if dun_2 == "고대미궁":
                        for i in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\godae_migoong_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 150, 430, 190, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("godae_migoong_title", imgs_.x, imgs_.y)
                                break
                            else:
                                click_pos_2(90, 300, cla)
                            time.sleep(0.5)

                        for i in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("move_title", imgs_.x, imgs_.y)
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                if dun_3 == "1":
                                    click_pos_2(470, 220, cla)
                                else:
                                    click_pos_2(470, 260, cla)
                            time.sleep(0.5)

                    elif dun_2 == "카타콤":
                        for i in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\katacom_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 150, 430, 190, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("katacom_title", imgs_.x, imgs_.y)
                                break
                            else:
                                click_pos_2(250, 300, cla)
                            time.sleep(0.5)
                        for i in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("move_title", imgs_.x, imgs_.y)
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                if dun_3 == "1":
                                    click_pos_2(470, 220, cla)
                                elif dun_3 == "2":
                                    click_pos_2(470, 260, cla)
                                else:
                                    click_pos_2(470, 300, cla)
                            time.sleep(0.5)


                    elif dun_2 == "드베르그":


                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(460, 410, 495, 435, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            complete_dun = True
                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dberg_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 150, 430, 190, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("dberg_title", imgs_.x, imgs_.y)
                                    break
                                else:
                                    click_pos_2(420, 300, cla)
                                time.sleep(0.5)

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_title", imgs_.x, imgs_.y)
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    if dun_3 == "1":
                                        click_pos_2(470, 220, cla)
                                    elif dun_3 == "2":
                                        click_pos_2(470, 260, cla)
                                    else:
                                        click_pos_2(470, 300, cla)
                                time.sleep(0.5)

                    elif dun_2 == "사막동굴":
                        for i in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\samac_cave_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 150, 430, 190, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("samac_cave_title", imgs_.x, imgs_.y)
                                break
                            else:
                                click_pos_2(590, 300, cla)
                            time.sleep(0.5)

                        for i in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("move_title", imgs_.x, imgs_.y)
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                if dun_3 == "1":
                                    click_pos_2(470, 220, cla)
                                else:
                                    click_pos_2(470, 260, cla)
                            time.sleep(0.5)

                    elif dun_2 == "지하신전":

                        for i in range(10):
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("move_title", imgs_.x, imgs_.y)
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                click_pos_2(760, 300, cla)
                            time.sleep(0.5)

                elif dun_1 == "특수":
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_clicked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(95, 100, 160, 130, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("dun_clicked", imgs_.x, imgs_.y)
                            break
                        else:
                            click_pos_2(125, 105, cla)
                        time.sleep(0.5)

                    if dun_2 == "환영의유적":


                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(130, 410, 160, 435, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            complete_dun = True
                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\hwanyuong_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 150, 430, 190, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("hwanyuong_title", imgs_.x, imgs_.y)
                                    break
                                else:
                                    click_pos_2(90, 300, cla)
                                time.sleep(0.5)

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_title", imgs_.x, imgs_.y)
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    if dun_3 == "1":
                                        click_pos_2(470, 220, cla)
                                    elif dun_3 == "2":
                                        click_pos_2(470, 260, cla)
                                    elif dun_3 == "3":
                                        click_pos_2(470, 300, cla)
                                    elif dun_3 == "4":
                                        click_pos_2(470, 340, cla)
                                    else:
                                        click_pos_2(470, 380, cla)
                                time.sleep(0.5)

                    elif dun_2 == "시간의미궁":


                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(295, 410, 325, 435, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            complete_dun = True
                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\time_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 150, 430, 190, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("time_title", imgs_.x, imgs_.y)
                                    break
                                else:
                                    click_pos_2(250, 300, cla)
                                time.sleep(0.5)

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_title", imgs_.x, imgs_.y)
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    if dun_3 == "1":
                                        click_pos_2(470, 220, cla)
                                    elif dun_3 == "2":
                                        click_pos_2(470, 260, cla)
                                    elif dun_3 == "3":
                                        click_pos_2(470, 300, cla)
                                    elif dun_3 == "4":
                                        click_pos_2(470, 340, cla)
                                    else:
                                        click_pos_2(470, 380, cla)
                                time.sleep(0.5)

                    elif dun_2 == "얼음신전":


                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(460, 410, 495, 435, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            complete_dun = True
                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\ice_temple_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 150, 430, 190, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("ice_temple_title", imgs_.x, imgs_.y)
                                    break
                                else:
                                    click_pos_2(420, 300, cla)
                                time.sleep(0.5)

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_title", imgs_.x, imgs_.y)
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    if dun_3 == "1":
                                        click_pos_2(470, 220, cla)
                                    elif dun_3 == "2":
                                        click_pos_2(470, 260, cla)
                                    elif dun_3 == "3":
                                        click_pos_2(470, 300, cla)
                                    elif dun_3 == "4":
                                        click_pos_2(470, 340, cla)
                                    else:
                                        click_pos_2(470, 380, cla)
                                time.sleep(0.5)
                    elif dun_2 == "혼돈의성채":


                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(630, 410, 660, 435, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            complete_dun = True
                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dberg_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 150, 430, 190, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("dberg_title", imgs_.x, imgs_.y)
                                    break
                                else:
                                    click_pos_2(420, 300, cla)
                                time.sleep(0.5)

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_title", imgs_.x, imgs_.y)
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    if dun_3 == "1":
                                        click_pos_2(470, 220, cla)
                                    else:
                                        click_pos_2(470, 260, cla)
                                time.sleep(0.5)

                    elif dun_2 == "정령의성채":


                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(795, 410, 830, 435, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            complete_dun = True
                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dberg_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 150, 430, 190, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("dberg_title", imgs_.x, imgs_.y)
                                    break
                                else:
                                    click_pos_2(420, 300, cla)
                                time.sleep(0.5)

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\move_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(430, 200, 510, 250, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_title", imgs_.x, imgs_.y)
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\dun_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(490, 360, 600, 400, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    if dun_3 == "1":
                                        click_pos_2(470, 220, cla)
                                    else:
                                        click_pos_2(470, 260, cla)
                                time.sleep(0.5)
                # 던전 입장 여부 및 완료여부
                if complete_dun == True:
                    myQuest_play_add(cla, data)
                else:
                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:
                            # 공격버튼 누르기
                            click_pos_2(895, 455, cla)
                            break
                        time.sleep(2)

            else:
                menu_open(cla)

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\menu_dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 170, 935, 300, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("menu_dungeon", imgs_.x, imgs_.y)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_dungeon.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 30, 950, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def dungeon_check(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open, juljun_on

    try:
        print("dungeon_check", data)

        where_ = False
        hunting_ = False

        # 던전_일반_고대미궁_1,2
        # 던전_일반_카타콤_1,2,3
        # 던전_일반_드베르그_1,2,3(시간제한)
        # 던전_일반_사막동굴_1,2
        # 던전_일반_지하신전_1,2
        # 던전_특수_환영의유적_1~5(시간제한)
        # 던전_특수_시간의미궁_1~5(시간제한)
        # 던전_특수_얼음신전_1~5(시간제한)
        # 던전_특수_혼돈의성채_1,2(시간제한_일주일)
        # 던전_특수_정령의성채_1,2(시간제한_일주일)

        dun_ = data.split("_")
        dun_1 = dun_[1]  # 일반, 특수
        dun_2 = dun_[2]  # 종류
        dun_3 = dun_[3]  # 층수

        # 절전 던전 모드 확인하기
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("절전모드")

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

                if dun_2 == "고대미궁":
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\where_godae_migoong.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 498, 150, 530, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        where_ = True
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_hunting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 110, 550, 165, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            hunting_ = True

                elif dun_2 == "카타콤":
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\where_katacom.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 498, 150, 530, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        where_ = True
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_hunting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 110, 550, 165, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            hunting_ = True

                elif dun_2 == "드베르그":
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\where_dberg.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 498, 150, 530, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        where_ = True
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_hunting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 110, 550, 165, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            hunting_ = True

                elif dun_2 == "사막동굴":
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\where_samac_cave.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 498, 150, 530, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        where_ = True
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_hunting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 110, 550, 165, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            hunting_ = True
                elif dun_2 == "지하신전":
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\where_under_temple.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 498, 150, 530, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        where_ = True
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_hunting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 110, 550, 165, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            hunting_ = True
                elif dun_2 == "환영의유적":
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\where_hwanyuong.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 498, 150, 530, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        where_ = True
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_hunting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 110, 550, 165, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            hunting_ = True
                elif dun_2 == "시간의미궁":
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\where_time.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 498, 150, 530, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        where_ = True
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_hunting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 110, 550, 165, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            hunting_ = True
                elif dun_2 == "얼음신전":
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dungeon\\where_ice_temple.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 498, 150, 530, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        where_ = True
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_hunting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 110, 550, 165, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            hunting_ = True
                # elif dun_2 == "혼돈의성채":
                #
                # elif dun_2 == "정령의성채채":


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
        return where_, hunting_
    except Exception as e:
        print(e)
        return 0