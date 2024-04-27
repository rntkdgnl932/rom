import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def menu_open(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_rom import clean_screen
    from get_item_rom import get_chulsuk, get_post
    from collection_rom import collection_start

    try:
        print("menu_open")

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\action\\menu_open\\menu_restart.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 290, 930, 360, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("menu_restart", imgs_.x, imgs_.y)

                # 출석
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(770, 290, 800, 320, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("get_chulsuk : menu_point", imgs_.x, imgs_.y)
                    get_chulsuk(cla)
                else:
                    # 우편
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 290, 840, 320, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("get_post : menu_point", imgs_.x, imgs_.y)
                        get_post(cla)
                    else:
                        # 콜렉
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\point\\menu_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 85, 880, 110, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("get_collection : menu_point", imgs_.x, imgs_.y)
                            if v_.collection_today == True and v_.onCollection == True:
                                collection_start(cla)
                            else:
                                menu_opened = True
                        else:
                            menu_opened = True


            else:
                clean_screen(cla)

                result_out = out_check(cla)

                if result_out == True:
                    click_pos_2(930, 45, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\action\\menu_open\\menu_restart.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 290, 930, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                else:

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        juljun_off(cla)


            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0


def menu_open_pure(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_rom import clean_screen
    from get_item_rom import get_chulsuk, get_post
    from collection_rom import collection_start

    try:
        print("menu_open_pure")

        menu_opened = False
        menu_opened_count = 0
        while menu_opened is False:
            menu_opened_count += 1
            if menu_opened_count > 7:
                menu_opened = True

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\action\\menu_open\\menu_restart.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 290, 930, 360, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("menu_restart", imgs_.x, imgs_.y)

                menu_opened = True


            else:

                clean_screen(cla)

                result_out = out_check(cla)

                if result_out == True:
                    click_pos_2(930, 45, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\action\\menu_open\\menu_restart.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 290, 930, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                else:

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        juljun_off(cla)


            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from character_select import character_screen_check


    try:

        out_ = False

        print("out_check")
        # 좌측 하단 키보드 설정
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\out\\out_keyboard.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 360, 40, 410, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("out_keyboard", imgs_.x, imgs_.y)
            out_ = True
        else:
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\character_select\\game_start.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(810, 520, 940, 560, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                character_screen_check(cla, v_.character_number)

        crash_check(cla, "check...")


        return out_


    except Exception as e:
        print(e)
        return 0

def crash_check(cla, data):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from dead import dead_check, dead_recover
    from massenger import line_to_me

    try:
        print("crash_check")

        dead_crash_on = False

        # 수시로 체크
        result_dead = dead_check(cla)
        if result_dead == True:
            dead_recover(cla)
            dead_crash_on = True
        else:

            crash_game = False
            logout_ = False
            why = "none"

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\logout.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 100, 650, 450, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                why = "롬 종료 되었따."
                logout_ = True


            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\server_select_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 470, 410, 520, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    logout_ = True
                    crash_game = True
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\inspection.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 100, 650, 500, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        why = "롬 점검중."
                        logout_ = True
                    else:
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\kakao_login_btn.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 150, 1900, 900, "one", img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            why = "롬 카카오 로그인 화면"
                            logout_ = True
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_logout.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 80, 520, 140, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                why = str(data)
                                logout_ = True
                                crash_game = True
                                for i in range(180):
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\server_select_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(280, 470, 410, 520, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\character_select\\game_start.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(810, 520, 940, 560, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                    time.sleep(5)

            if logout_ == True:

                dead_crash_on = True

                if crash_game == True:
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\character_select\\game_start.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(810, 520, 940, 560, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            why = "롬 밖으로 튕겼지만 재 로그인 성공"
                            line_to_me(v_.now_cla, why)
                            logout_ = False
                            break
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\kakao_login_btn.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(280, 150, 1900, 900, "one", img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                why = "롬 카카오 로그인 화면"
                                logout_ = True
                                break
                            else:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\logout.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 180, 520, 330, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    # click_pos_2(475, 360, cla)
                                    why = "롬 인증 실패 화면"
                                    logout_ = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_logout.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 80, 520, 140, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        logout_ = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\server_select_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(280, 470, 410, 520, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            why = "롬 팅겨서 바깥 화면임"
                                            click_pos_2(670, 240, cla)
                                        else:
                                            why = "튕김 취소"
                                            logout_ = False


                        time.sleep(1)

                if logout_ == True:
                    print(why)
                    line_to_me(v_.now_cla, why)



                    dir_path = "C:\\my_games\\load\\rom"
                    file_path = dir_path + "\\start.txt"
                    file_path2 = dir_path + "\\cla.txt"
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        data = 'no'
                        file.write(str(data))
                        time.sleep(0.2)
                    with open(file_path2, "w", encoding='utf-8-sig') as file:
                        data = v_.now_cla
                        file.write(str(data))
                        time.sleep(0.2)
                    os.execl(sys.executable, sys.executable, *sys.argv)

        return dead_crash_on


    except Exception as e:
        print(e)
        return 0

def juljun_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:

        juljun_ = False

        print("juljun_check")
        # 튜토 완료 확인
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("juljun_on", imgs_.x, imgs_.y)
            juljun_ = True

        return juljun_

    except Exception as e:
        print(e)
        return 0

def juljun_on(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_rom import clean_screen

    try:

        for i in range(10):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("juljun_on", imgs_.x, imgs_.y)
                break
            else:
                result_out = out_check(cla)

                if result_out == True:
                    click_pos_2(16, 420, cla)

                    for c in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("juljun_on", imgs_.x, imgs_.y)
                            break
                        time.sleep(0.2)

                else:
                    clean_screen(cla)
            time.sleep(0.3)


        juljun_ = False

        print("juljun_check")
        # 튜토 완료 확인
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("juljun_on", imgs_.x, imgs_.y)
            juljun_ = True

        return juljun_

    except Exception as e:
        print(e)
        return 0

def juljun_off(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    try:
        # 튜토 완료 확인
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            drag_pos(440, 250, 900, 250, cla)


            for i in range(10):
                result_out = out_check(cla)
                if result_out == True:
                    break
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        drag_pos(470, 250, 900, 250, cla)
                time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def confirm_all(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:

        clicked = False

        print("confirm_all")
        # 튜토 완료 확인
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\confirm\\tuto_complete_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(490, 340, 600, 400, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("tuto_complete_confirm", imgs_.x, imgs_.y)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            clicked = True
        else:
            # 튜토 이동 확인
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\confirm\\tuto_move_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 300, 700, 600, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("tuto_move_confirm", imgs_.x, imgs_.y)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clicked = True

        return clicked

    except Exception as e:
        print(e)
        return 0

def moving_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:

        move_ = False

        print("moving")
        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\move\\move_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 350, 600, 380, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("move_1", imgs_.x, imgs_.y)
            move_ = True
        else:
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\move\\move_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(470, 350, 600, 380, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("move_2", imgs_.x, imgs_.y)
                move_ = True
            else:
                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\move\\move_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 350, 600, 380, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("move_3", imgs_.x, imgs_.y)
                    move_ = True


        return move_

    except Exception as e:
        print(e)
        return 0


def huntig_check(cla, data):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, menu_open, juljun_off, juljun_on
    from potion_rom import juljun_potion_check, potion_buy
    from dungeon_rom import dungeon_check
    from jadong_rom import jadong_check
    from datetime import datetime
    from datetime import date, timedelta

    try:


        if "던전" in data:

            # 절전 던전 모드 확인하기

            huntig_continue = True
            while huntig_continue is True:

                print("hunting checking", data)


                nowDay_ = datetime.today().strftime("%Y%m%d")
                nowDay = int(nowDay_)
                nowTime = int(datetime.today().strftime("%H"))
                yesterday_ = date.today() - timedelta(1)
                yesterday = int(yesterday_.strftime('%Y%m%d'))


                dir_path = "C:\\my_games\\" + str(v_.game_folder)
                file_path2 = dir_path + "\\mysettings\\refresh_time\\quest.txt"
                file_path13 = dir_path + "\\mysettings\\refresh_time\\refresh_time.txt"

                isRefresh = False
                while isRefresh is False:
                    if os.path.isfile(file_path13) == True:
                        with open(file_path13, "r", encoding='utf-8-sig') as file:
                            isRefresh = True
                            refresh_time = file.read()
                            print("refresh_time", refresh_time)
                    else:
                        with open(file_path13, "w", encoding='utf-8-sig') as file:
                            file.write(str(6))

                if nowTime >= int(refresh_time):
                    nowDay = str(nowDay)
                    print("초기화", nowDay)
                else:
                    nowDay = yesterday
                    nowDay = str(nowDay)

                # 스케쥴 초기화 관련
                if os.path.isfile(file_path2) == True:
                    print("nowDay : ", nowDay)
                    # 파일 읽기
                    with open(file_path2, "r", encoding='utf-8-sig') as file:
                        lines2 = file.read().splitlines()
                        day_ = lines2[0].split(":")

                    if day_[0] != nowDay:
                        print("스케쥴 초기화 해야함")
                        huntig_continue = False
                    else:

                        result_out = out_check(cla)
                        if result_out == True:
                            potion_buy(cla)
                            huntig_continue = False
                        else:
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:


                                # 절전 던전 모드 확인하기
                                result_check = dungeon_check(cla, data)

                                if result_check[0] == True and result_check[1] == True:
                                    print("정상 던전 사냥 중 : ", data)
                                    # 물약 파악
                                    result_potion = juljun_potion_check(cla)
                                    if result_potion == False:
                                        potion_buy(cla)
                                        huntig_continue = False
                                elif result_check[0] == True and result_check[1] == False:
                                    juljun_off(cla)
                                    time.sleep(0.2)
                                    click_pos_2(895, 455, cla)
                                    time.sleep(0.2)
                                    juljun_on(cla)
                                else:
                                    huntig_continue = False

                        # dead
                        why = "롬 : " + str(data) + " 던전 사냥 중 튕겼다.."
                        result_crash = crash_check(cla, why)
                        if result_crash == True:
                            huntig_continue = False


        elif "자동사냥" in data:

            # 절전 자동 모드 확인하기

            huntig_continue = True
            while huntig_continue is True:

                print("hunting checking", data)

                nowDay_ = datetime.today().strftime("%Y%m%d")
                nowDay = int(nowDay_)
                nowTime = int(datetime.today().strftime("%H"))
                yesterday_ = date.today() - timedelta(1)
                yesterday = int(yesterday_.strftime('%Y%m%d'))

                dir_path = "C:\\my_games\\" + str(v_.game_folder)
                file_path2 = dir_path + "\\mysettings\\refresh_time\\quest.txt"
                file_path13 = dir_path + "\\mysettings\\refresh_time\\refresh_time.txt"

                isRefresh = False
                while isRefresh is False:
                    if os.path.isfile(file_path13) == True:
                        with open(file_path13, "r", encoding='utf-8-sig') as file:
                            isRefresh = True
                            refresh_time = file.read()
                            print("refresh_time", refresh_time)
                    else:
                        with open(file_path13, "w", encoding='utf-8-sig') as file:
                            file.write(str(6))

                if nowTime >= int(refresh_time):
                    nowDay = str(nowDay)
                    print("초기화", nowDay)

                else:
                    nowDay = yesterday
                    nowDay = str(nowDay)

                with open(file_path2, "r", encoding='utf-8-sig') as file:
                    lines2 = file.read().splitlines()
                    day_ = lines2[0].split(":")

                if day_[0] == nowDay:
                    result_out = out_check(cla)
                    if result_out == True:
                        potion_buy(cla)
                        huntig_continue = False
                    else:
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\check\\juljun\\juljun_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            result_check = jadong_check(cla)
                            if result_check == True:
                                print("정상 자동 사냥 중......")
                                # 물약 파악
                                result_potion = juljun_potion_check(cla)
                                if result_potion == False:
                                    potion_buy(cla)
                                    huntig_continue = False
                            else:
                                juljun_off(cla)
                                time.sleep(0.2)
                                click_pos_2(895, 455, cla)
                                time.sleep(0.2)
                                juljun_on(cla)
                    time.sleep(0.2)
                    # dead
                    why = "롬 자동 사냥 중 튕겼다.."
                    result_crash = crash_check(cla, why)
                    if result_crash == True:
                        huntig_continue = False
                else:
                    huntig_continue = False

    except Exception as e:
        print(e)
        return 0



