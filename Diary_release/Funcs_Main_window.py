import time

color_violet = "#805491"
color_green = "#008000"
color_red = "#c92118"
color_grey = "#9b9e9b"
color_black = "#000000"
color_yellow = "#edcf24"
color_blue = "#338eb5"

bad_1, good_1, bad_2, good_2, bad_3, good_3, bad_4, good_4, bad_5, good_5 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

file = open('info_Main.txt', 'r')
info_data_Main_window = file.readlines()
for i in range(len(info_data_Main_window) - 1):
    info_data_Main_window[i] = info_data_Main_window[i][:-1]
for i in range(len(info_data_Main_window)):
    info_data_Main_window[i] = info_data_Main_window[i].split(" ")
file.close()

for k in range(len(info_data_Main_window)):
    if int(info_data_Main_window[k][4]) == -1: bad_1 += 1
    if int(info_data_Main_window[k][4]) == 1: good_1 += 1
    if int(info_data_Main_window[k][5]) == -1: bad_2 += 1
    if int(info_data_Main_window[k][5]) == 1: good_2 += 1
    if int(info_data_Main_window[k][6]) == -1: bad_3 += 1
    if int(info_data_Main_window[k][6]) == 1: good_3 += 1
    if int(info_data_Main_window[k][7]) == -1: bad_4 += 1
    if int(info_data_Main_window[k][7]) == 1: good_4 += 1
    if int(info_data_Main_window[k][8]) == -1: bad_5 += 1
    if int(info_data_Main_window[k][8]) == 1: good_5 += 1

now = time.localtime()

if i == len(info_data_Main_window) - 1 and str(info_data_Main_window[i][3]) < str(now[7]) or i == len(info_data_Main_window) - 1 and str(info_data_Main_window[i][2]) < str(now[0]):
    info_data_Main_window.append([str(now[2]), str(now[1]), str(now[0]), str(now[7]), "-2", "-2", "-2", "-2", "-2"])

def Alcogol():
    Main_func([-1, -2, -2, -2, -2])

def Training():
    Main_func([1, -2, -2, -2, -2])

def Nicotine():
    Main_func([-2, -1, -2, -2, -2])

def Active_Style():
    Main_func([-2, 1, -2, -2, -2])

def Games():
    Main_func([-2, -2, -1, -2, -2])

def Study():
    Main_func([-2, -2, 1, -2, -2])

def News_and_Shorts():
    Main_func([-2, -2, -2, -1, -2])

def Literature():
    Main_func([-2, -2, -2, 1, -2])

def Poor_Nutrition():
    Main_func([-2, -2, -2, -2, -1])

def Proper_Nutrition():
    Main_func([-2, -2, -2, -2, 1])

def Exit_from():
    quit()

def Main_func(params= [-2, -2, -2, -2, -2]):

    global info_data_Main_window
    global bad_1
    global good_1
    global bad_2
    global good_2
    global bad_3
    global good_3
    global bad_4
    global good_4
    global bad_5
    global good_5

    now = time.localtime()

    for i in range(len(info_data_Main_window)):
        if str(info_data_Main_window[i][2]) == str(now[0]) and str(info_data_Main_window[i][3]) == str(now[7]):
            for j in range(len(params)):
                if params[j] == 1 and int(info_data_Main_window[i][4 + j]) != -1:
                    info_data_Main_window[i][4 + j] = 1
                elif params[j] == -1:
                    info_data_Main_window[i][4 + j] = -1
                else: pass
        else:
            if i == len(info_data_Main_window) - 1 and str(info_data_Main_window[i][3]) < str(now[7]) or i == len(info_data_Main_window) - 1 and str(info_data_Main_window[i][2]) < str(now[0]):
                for j in range(len(params)):
                    if params[j] == 1 and int(info_data_Main_window[i + 1][4 + j]) != -1:
                        info_data_Main_window[i + 1][4 + j] = 1
                    elif params[j] == -1:
                        info_data_Main_window[i + 1][4 + j] = -1
                    else: pass
            else: pass
            
    bad_1, good_1, bad_2, good_2, bad_3, good_3, bad_4, good_4, bad_5, good_5 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for k in range(len(info_data_Main_window)):
        if int(info_data_Main_window[k][4]) == -1: bad_1 += 1
        if int(info_data_Main_window[k][4]) == 1: good_1 += 1
        if int(info_data_Main_window[k][5]) == -1: bad_2 += 1
        if int(info_data_Main_window[k][5]) == 1: good_2 += 1
        if int(info_data_Main_window[k][6]) == -1: bad_3 += 1
        if int(info_data_Main_window[k][6]) == 1: good_3 += 1
        if int(info_data_Main_window[k][7]) == -1: bad_4 += 1
        if int(info_data_Main_window[k][7]) == 1: good_4 += 1
        if int(info_data_Main_window[k][8]) == -1: bad_5 += 1
        if int(info_data_Main_window[k][8]) == 1: good_5 += 1

    file = open('info_Main.txt', 'w')
    for i in range(len(info_data_Main_window)):
        x = " ".join(str(el) for el in info_data_Main_window[i])
        if i == len(info_data_Main_window) - 1:
            file.write(x)
        else:
            file.write(x + '\n')
    file.close()

def Bad_or_Good(bad, good):
    if good > bad and good > (good + bad) * 0.9: return [">>>>>", color_green]
    elif good > bad and good > (good + bad) * 0.8: return [">>>>", color_green]
    elif good > bad and good > (good + bad) * 0.7: return [">>>", color_green]
    elif good > bad and good > (good + bad) * 0.6: return [">>", color_green]
    elif good > bad and good > (good + bad) * 0.5: return [">", color_green]
    elif bad > good and bad > (good + bad) * 0.9: return ["<<<<<", color_red]
    elif bad > good and bad > (good + bad) * 0.8: return ["<<<<", color_red]
    elif bad > good and bad > (good + bad) * 0.7: return ["<<<", color_red]
    elif bad > good and bad > (good + bad) * 0.6: return ["<<", color_red]
    elif bad > good and bad > (good + bad) * 0.5: return ["<", color_red]
    else: return ["---", color_yellow]

def get_percent():

    global bad_1
    global good_1
    global bad_2
    global good_2
    global bad_3
    global good_3
    global bad_4
    global good_4
    global bad_5
    global good_5

    Sum_goods_and_bads = bad_1*3 + good_1*3 + bad_2*2 + good_2*2 + bad_3*3 + good_3*3 + bad_4 + good_4 + bad_5 + good_5
    return str(round(100 * (good_1*3 + good_2*2 + good_3*3 + good_4 + good_5) / Sum_goods_and_bads, 1)) + "%"

def get_color_precent():
    if float(get_percent()[:-1]) >= 70: return color_violet
    elif float(get_percent()[:-1]) >= 60: return color_blue
    elif float(get_percent()[:-1]) >= 50: return color_green
    elif float(get_percent()[:-1]) >= 40: return color_yellow
    else: return color_red

def get_color_button(param= [-2, -2, -2, -2, -2]):
    a = 0
    for i in range(len(param)):
        if param[i] != -2:
            a = i
    if int(info_data_Main_window[-1][4 + a]) == -1 and param[a] == -1: return [color_red, color_black]
    elif int(info_data_Main_window[-1][4 + a]) == 1 and param[a] == 1: return [color_green, color_black]
    elif param[a] == -1: return [color_grey, color_red]
    else: return [color_grey, color_green]