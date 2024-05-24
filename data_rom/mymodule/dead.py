import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dead_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check
    from schedule import myQuest_play_add, myQuest_play_check

    try:
        print("dead_check")

        recovery = False

        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\dead_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 170, 520, 220, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("dead_title", imgs_.x, imgs_.y)
            recovery = True

        else:
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\experience_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                recovery = True

        if recovery == True:

            result_schedule = myQuest_play_check(v_.now_cla, "check")
            print("result_schedule", result_schedule)
            character_id = result_schedule[0][1]
            result_schedule_ = result_schedule[0][2]

            if result_schedule_ == "튜토육성" or result_schedule_ == "의뢰하기" or result_schedule_ == "악령의탑":
                myQuest_play_add(cla, result_schedule_)
                if result_schedule_ == "튜토육성":
                    v_.collection_today = True
            elif "혼돈의성채" in result_schedule_ or "정령의성채" in result_schedule_:
                myQuest_play_add(cla, result_schedule_)


        return recovery
    except Exception as e:
        print(e)
        return 0


def dead_recover(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_rom import out_check, confirm_all
    from clean_screen_rom import clean_screen
    from massenger import line_to_me


    try:
        print("dead_recover")

        print("경험치 복구 확인")

        recover_start = False

        for i in range(10):
            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\experience_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                recover_start = True

                # full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\dead_confirm.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(410, 410, 540, 450, cla, img, 0.7)
                # if imgs_ is not None and imgs_ != False:
                #     print("dead_confirm", imgs_.x, imgs_.y)
                #     recover_start = True
                #     click_pos_reg(imgs_.x, imgs_.y, cla)
                #     time.sleep(0.5)
            else:

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\dead_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 170, 520, 220, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("dead_title", imgs_.x, imgs_.y)
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\dead_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 410, 540, 450, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("dead_confirm", imgs_.x, imgs_.y)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\title\\title_dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 950, 80, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        click_pos_2(700, 50, cla)
                        time.sleep(0.5)

                    else:
                        click_pos_2(735, 50, cla)
                        time.sleep(0.5)
            time.sleep(1)

        if recover_start == True:

            dead_ = False
            dead_count = 0
            while dead_ is False:
                dead_count += 1
                if dead_count > 7:
                    dead_ = True

                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\experience_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("experience_title", imgs_.x, imgs_.y)
                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\experience_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 110, 100, 220, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("experience_click", imgs_.x, imgs_.y)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\free_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(70, 400, 170, 430, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("free_click", imgs_.x, imgs_.y)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\recover_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 210, 540, 240, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("recover_title", imgs_.x, imgs_.y)

                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\free_recover.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(490, 370, 600, 400, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("free_recover", imgs_.x, imgs_.y)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        result_confirm = confirm_all(cla)
                                        if result_confirm == True:
                                            break

                                time.sleep(0.2)
                        else:
                            # 경험치 골드 체크확인하기
                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 350, 90, 390, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    # 여기에 추후 복구할 경험치 클릭하기
                                    click_pos_2(100, 415, cla)
                                    break
                                else:
                                    click_pos_2(73, 370, cla)
                                time.sleep(0.2)

                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\recover_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 210, 540, 240, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("recover_title", imgs_.x, imgs_.y)

                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\recover.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(490, 370, 600, 400, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("dead_confirm", imgs_.x, imgs_.y)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\dead_confirm.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(490, 370, 600, 400, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("dead_confirm", imgs_.x, imgs_.y)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                time.sleep(0.2)

                            # why = "롬 무료 복구 없다. 정비하라"
                            # line_to_me(cla, why)
                            clean_screen(cla)
                    else:
                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\not_recover_item.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(130, 210, 210, 250, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            dead_ = True
                else:
                    click_pos_2(735, 50, cla)

                time.sleep(0.5)

            print("장비 복구 확인")

            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\experience_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                dead_ = False
                dead_count = 0
                while dead_ is False:
                    dead_count += 1
                    if dead_count > 7:
                        dead_ = True

                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\item_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("item_title", imgs_.x, imgs_.y)


                        full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\not_recover_item.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(130, 210, 210, 250, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            dead_ = True
                        else:

                            # 장비 골드 체크확인하기
                            for i in range(10):
                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 350, 90, 390, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\not_recover_item.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(130, 210, 210, 250, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        # 여기에 추후 복구할 아이템 넣기
                                        click_pos_2(120, 140, cla)
                                        time.sleep(0.2)
                                        click_pos_2(100, 415, cla)

                                        for b in range(10):
                                            full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\recover_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(440, 210, 540, 240, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                print("recover_title", imgs_.x, imgs_.y)

                                                full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\dead_confirm.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(490, 370, 600, 400, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("dead_confirm", imgs_.x, imgs_.y)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    break
                                            time.sleep(0.2)
                                else:
                                    click_pos_2(73, 370, cla)
                                time.sleep(0.2)

                            # for i in range(10):
                            #     full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\recover_title.PNG"
                            #     img_array = np.fromfile(full_path, np.uint8)
                            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #     imgs_ = imgs_set_(440, 210, 540, 240, cla, img, 0.7)
                            #     if imgs_ is not None and imgs_ != False:
                            #         print("recover_title", imgs_.x, imgs_.y)
                            #
                            #         full_path = "c:\\my_games\\rom\\data_rom\\imgs\\dead\\dead_confirm.PNG"
                            #         img_array = np.fromfile(full_path, np.uint8)
                            #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #         imgs_ = imgs_set_(490, 370, 600, 400, cla, img, 0.7)
                            #         if imgs_ is not None and imgs_ != False:
                            #             print("dead_confirm", imgs_.x, imgs_.y)
                            #             click_pos_reg(imgs_.x, imgs_.y, cla)
                            #
                            #             # 장비 복구 메신져 보내기
                            #             # why = "장비 복구 했다. 반드시 확인 후 다시 켜라"
                            #             # line_to_me(cla, why)
                            #             #
                            #             # v_.onCollection = False
                            #             #
                            #             # dir_path_col = "C:\\my_games\\" + str(v_.game_folder)
                            #             # file_path_col = dir_path_col + "\\mysettings\\collection\\collection_toggle.txt"
                            #             #
                            #             # with open(file_path_col, "w", encoding='utf-8-sig') as file:
                            #             #     file.write("off")
                            #             #     time.sleep(0.2)
                            #             #
                            #             # dir_path = "C:\\my_games\\load\\rom"
                            #             # file_path = dir_path + "\\start.txt"
                            #             # file_path2 = dir_path + "\\cla.txt"
                            #             # with open(file_path, "w", encoding='utf-8-sig') as file:
                            #             #     data = 'no'
                            #             #     file.write(str(data))
                            #             #     time.sleep(0.2)
                            #             # with open(file_path2, "w", encoding='utf-8-sig') as file:
                            #             #     data = v_.now_cla
                            #             #     file.write(str(data))
                            #             #     time.sleep(0.2)
                            #             # os.execl(sys.executable, sys.executable, *sys.argv)
                            #             #
                            #             # break
                            #     time.sleep(0.2)



                    else:
                        click_pos_2(25, 195, cla)

                    time.sleep(0.5)
        else:
            # 장비 복구 메신져 보내기
            why = "죽고나서 운없게도 장비 복구 못했다. 반드시 확인 후 다시 켜라"
            line_to_me(cla, why)

            v_.onCollection = False

            dir_path_col = "C:\\my_games\\" + str(v_.game_folder)
            file_path_col = dir_path_col + "\\mysettings\\collection\\collection_toggle.txt"

            with open(file_path_col, "w", encoding='utf-8-sig') as file:
                file.write("off")
                time.sleep(0.2)

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

        clean_screen(cla)

    except Exception as e:
        print(e)
        return 0



