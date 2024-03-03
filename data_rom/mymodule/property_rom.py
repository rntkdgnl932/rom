import time
# import os
import sys


import variable as v_
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

import requests
from ftplib import FTP
import os

# 이건 엑셀로 변환시 필요한 것...
# import pandas

ftp_username = 'gamer'
ftp_password = 'coobccocco'
data_list = []  # data_list 변수를 전역 변수로 초기화



def my_property_upload(cla):
    import cv2
    import time
    import os
    import numpy as np
    from action_rom import out_check
    from clean_screen_rom import clean_screen
    from function_game import imgs_set_, click_pos_2

    try:


        # 1. coob, ccocco 파악

        dir_path = "C:\\my_games"
        file_path = dir_path + "\\line\\line.txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            line = file.read()
            line_ = line.split(":")
            print('line', line)
            # line_[0] => coob, ccocco
            # line_[1] => 컴퓨터번호

        # 2. game 파악

        game_name = v_.this_game

        # 3. 게임 서버 파악

        file_path3 = dir_path + "\\rom\\mysettings\\game_server\\game_server.txt"

        isstart1 = False
        while isstart1 is False:
            if os.path.isfile(file_path) == True:
                with open(file_path3, "r", encoding='utf-8-sig') as file:
                    isstart1 = True
                    game_server = file.read()
                    print('롬 game server', game_server)
                    # line3 => 게임서버
            else:
                with open(file_path3, "w", encoding='utf-8-sig') as file:
                    data = 'none'
                    file.write(str(data))




        # 4. 다이야, 골드 파악

        result_mine = mine_check(cla)
        print("result_mine", result_mine)
        # result_mine[0] => 골드
        # result_mine[1] => 다이아

        # 다이야 0이면 업로드 안하기

        if int(result_mine[1]) != 0:

            # 5. 내 서버 ip 불러오기

            ftp_server = ftp_ip_get()



            # 업로드 처리 과정

            # 6. 로컬 파일 경로 (절대 경로 사용)
            local_file_path = 'C:/my_games/rom/mysettings/my_property/my_property.txt'

            dir_path = "C:\\my_games\\rom\\mysettings\\my_property"
            file_path = dir_path + "\\my_property.txt"

            isstart1 = False
            while isstart1 is False:
                if os.path.isdir(dir_path) == True:
                    isstart1 = True
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        # data = 사용자:게임이름:게임서버:다이아:골드
                        data = str(line_[0]) + ':' + str(game_name) + ':' + str(game_server) + ':' + str(result_mine[1]) + ':' + str(
                            result_mine[0])
                        file.write(str(data))

                else:
                    os.makedirs(dir_path)




            # 7. 원격 파일 경로 (FTP 서버 내)
            remote_directory = '/rom/' + str(line_[0])  # 원격 디렉토리 경로
            remote_file_path = '/rom/' + str(line_[0]) + '/' + str(line_[1]) + '.txt'
            print("7", remote_file_path)

            # # 미리 삭제해버리자?
            # if os.path.isdir(remote_directory) == False:
            #     os.makedirs(remote_directory)
            #
            # if os.path.isfile(remote_file_path) == True:
            #     os.remove(file_path)
            #     print('기존 파일이 삭제되었습니다.')

            # FTP 연결 및 파일 업로드
            try:
                print("aaa")
                with FTP(ftp_server) as ftp:
                    ftp.login(ftp_username, ftp_password)

                    # # 원격 디렉토리가 이미 존재하지 않는 경우에만 생성
                    # if remote_directory not in ftp.nlst():
                    #     ftp.mkd(remote_directory)
                    #     print("remote_directory")
                    # if remote_file_path in ftp.nlst():
                    #     ftp.delete(remote_file_path)
                    #     print("delete")
                    # else:
                    #     print(" not delete")

                    with open(local_file_path, 'rb') as file:
                        # 파일 업로드시 UTF-8 인코딩 사용
                        ftp.storbinary('STOR ' + remote_file_path, file, 8192)
                    print(f'로컬 파일 {local_file_path}을 FTP 서버의 {remote_file_path}로 업로드했습니다.')
            except Exception as e:
                print(f'파일 업로드 실패: {e}')

    except Exception as e:
        print(e)
        return 0

def ftp_ip_get():
    try:
        url = "https://raw.githubusercontent.com/rntkdgnl932/server/master/server_ip.txt"

        response = requests.get(url, headers={'Cache-Control': 'no-cache'})
        # response = requests.get(url, headers={'Cache-Control': 'no-cache'})
        data = response.text

        print("ftp_ip_get", data)
        return data
    except Exception as e:
        print(e)
        return 0

def mine_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, text_check_get, in_number_check, int_put_
    from schedule import myQuest_play_add
    from action_rom import menu_open
    from clean_screen_rom import clean_screen

    try:
        print("mine_check")

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 + 960
        if cla == 'four':
            plus = 960 + 960 + 960

        gold_ = 0
        dia_ = 0

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

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\gold.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 30, 600, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("gold", imgs_)
                    # 481
                    x_reg_1 = imgs_.x - plus

                    for i in range(4):
                        read_gold = text_check_get(x_reg_1 + 10 + i, 38, x_reg_1 + 80, 50, cla)
                        if read_gold == "":
                            print("골드 못 읽음")
                        else:
                            print("read_gold", read_gold)
                            break



                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\auction\\dia.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 30, 600, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("dia", imgs_)
                    # 426
                    x_reg_2 = imgs_.x - plus

                    for i in range(4):
                        read_dia = text_check_get(x_reg_2 + 4 + i, 38, x_reg_2 + 30, 50, cla)
                        if read_dia == "":
                            print("다이아 못 읽음")
                        else:
                            print("read_dia", read_dia)
                            break

                if dia_ == 0:
                    clean_screen(cla)
                    time.sleep(0.3)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\property\\property_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 50, 480, 75, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            read_dia = text_check_get(518, 77, 549, 90, cla)
                            if read_dia == "":
                                print("다이아 못 읽음")
                            else:
                                print("read_dia", read_dia)

                            read_gold = text_check_get(500, 99, 549, 112, cla)
                            if read_gold == "":
                                print("골드 못 읽음")
                            else:
                                print("read_gold", read_gold)

                            break

                        else:
                            click_pos_2(444, 44, cla)
                        time.sleep(0.5)

                if gold_ == 0:
                    clean_screen(cla)
                    time.sleep(0.3)
                    for i in range(10):
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\property\\property_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 50, 480, 75, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            read_gold = text_check_get(500, 99, 549, 112, cla)
                            if read_gold == "":
                                print("골드 못 읽음")
                            else:
                                print("read_gold", read_gold)

                            break

                        else:
                            click_pos_2(444, 44, cla)
                        time.sleep(0.5)

                digit_ready = in_number_check(read_gold)
                print("digit_ready", digit_ready)
                if digit_ready == True:
                    read_data_int = int(int_put_(read_gold))
                    print("read_data_int", read_data_int)
                    gold_ = read_data_int

                digit_ready = in_number_check(read_dia)
                print("digit_ready", digit_ready)
                if digit_ready == True:
                    read_data_int = int(int_put_(read_dia))
                    print("read_data_int", read_data_int)
                    dia_ = read_data_int


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

        return gold_, dia_

    except Exception as e:
        print(e)
        return 0