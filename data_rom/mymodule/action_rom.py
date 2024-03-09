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
                            if v_.collection_today == True:
                                collection_start(cla)
                            else:
                                menu_opened = True
                        else:
                            menu_opened = True


            else:
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

                    clean_screen(cla)
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

                    clean_screen(cla)
            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2


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

        crash_check(cla, "check")


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

        # 수시로 체크
        result_dead = dead_check(cla)
        if result_dead == True:
            dead_recover(cla)
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
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\logout.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 180, 520, 260, cla, img, 0.8)
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
                                for i in range(10):
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\server_select_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(280, 470, 410, 520, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(5)

            if logout_ == True:

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
                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\logout.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 180, 520, 330, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                why = "롬 카카오 로그인 화면"
                                break
                            else:
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\server_select_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(280, 470, 410, 520, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    why = "롬 팅겨서 바깥 화면임"
                                    click_pos_2(670, 240, cla)

                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\logout\\logout.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 180, 520, 330, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    # click_pos_2(475, 360, cla)
                                    why = "롬 인증 실패 화면"
                                    break
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
            drag_pos(470, 250, 900, 250, cla)

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
