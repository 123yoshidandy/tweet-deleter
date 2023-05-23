import time

import pyautogui
import cv2


def click_center(template, max_loc):
    weight, height = (template.shape[::-1][1], template.shape[::-1][2])
    x = max_loc[0] + weight / 2
    y = max_loc[1] + height / 2

    pyautogui.click(x, y)


def sleep(stop_x, stop_y):
    pyautogui.moveTo(stop_x, stop_y)
    time.sleep(0.3)


def main():
    pyautogui.screenshot("./tmp.png")
    input = cv2.imread("./tmp.png")
    template = cv2.imread("./stop.png")

    result = cv2.matchTemplate(input, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)  # min_val, max_val, min_loc, max_loc

    if max_val > 0.90:
        weight, height = (template.shape[::-1][1], template.shape[::-1][2])
        stop_x = max_loc[0] + weight / 2
        stop_y = max_loc[1] + height / 2

    else:
        print("停止ボタンが見つかりません。プログラムを終了します。")
        return

    while True:
        pyautogui.screenshot("./tmp.png")
        input = cv2.imread("./tmp.png")

        template = cv2.imread("./delete1.png")

        result = cv2.matchTemplate(input, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)  # min_val, max_val, min_loc, max_loc

        if max_val > 0.90:
            click_center(template, max_loc)
            sleep(stop_x, stop_y)

        else:
            template = cv2.imread("./delete2.png")

            result = cv2.matchTemplate(input, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)  # min_val, max_val, min_loc, max_loc

            if max_val > 0.90:
                click_center(template, max_loc)
                sleep(stop_x, stop_y)

            else:
                template = cv2.imread("./delete3.png")

                result = cv2.matchTemplate(input, template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(result)  # min_val, max_val, min_loc, max_loc

                if max_val > 0.90:
                    click_center(template, max_loc)
                    sleep(stop_x, stop_y)

                else:
                    template = cv2.imread("./dot.png")

                    result = cv2.matchTemplate(input, template, cv2.TM_CCOEFF_NORMED)
                    _, max_val, _, max_loc = cv2.minMaxLoc(result)  # min_val, max_val, min_loc, max_loc

                    if max_val > 0.90:
                        click_center(template, max_loc)
                        sleep(stop_x, stop_y)


if __name__ == '__main__':
    main()
