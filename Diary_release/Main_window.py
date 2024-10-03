from tkinter import *
import time
import Settings

bad_1, good_1, bad_2, good_2, bad_3, good_3, bad_4, good_4, bad_5, good_5 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
info_data_Main_window = []

def main_window():

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
    global info_data_Main_window

    color_violet = "#805491"
    color_green = "#008000"
    color_red = "#c92118"
    color_grey = "#9b9e9b"
    color_black = "#000000"
    color_yellow = "#edcf24"
    color_blue = "#338eb5"

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

    if len(info_data_Main_window) == 0 or int(info_data_Main_window[i][3]) < now[7] or int(info_data_Main_window[i][2]) < now[0]:
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
        if len(info_data_Main_window) == 1 and Sum_goods_and_bads == 0:
            return "0 %"
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

    window = Tk()
    window.title("Мой день")
    window.geometry(str(window.winfo_screenwidth() - 75) + "x" + str(window.winfo_screenheight()))
    window.columnconfigure(index=0, weight=2)
    window.rowconfigure(index=0, weight=2)
    frame = Frame(window, highlightbackground= color_violet, highlightthickness= 10, padx= 100, pady= 10)  
    frame.pack(expand=True)

    day = str(time.localtime()[2])
    if len(day) == 1: day = "0" + day

    month = str(time.localtime()[1])
    if len(month) == 1: month = "0" + month

    label_data = Label(frame, text="Дата " + day + "." + month + "." + str(time.localtime()[0]), font=("Arial", 40))
    label_data.grid(row=0, column=0, columnspan=3, ipadx= 300)

    label_productivity = Label(frame, text="Общая продуктивность: ", font=("Arial", 40))
    label_productivity.grid(row=1, column=0, columnspan=2, ipadx= 30)
    label_percent = Label(frame, text= get_percent(), font=("Arial", 50), foreground=get_color_precent())
    label_percent.grid(row=1, column=2, ipadx= 50)

    def on_enter_for_Choice_left1(e):
        if int(info_data_Main_window[-1][4]) != -1:
            Choice_left1.config(background=color_red, foreground= color_black)
    def on_leave_for_Choice_left1(e):
        if int(info_data_Main_window[-1][4]) != -1:
            Choice_left1.config(background= color_grey, foreground= color_red)
    Choice_left1 = Button(frame, text='Алкоголь', fg=get_color_button([-1, -2, -2, -2, -2])[1], bg=get_color_button([-1, -2, -2, -2, -2])[0], font=("Arial", 14), activebackground='red', command=Alcogol)
    Choice_left1.grid(row=2, column=0, ipadx= 116, ipady= 20, pady= 5)
    Choice_left1.bind('<Enter>', on_enter_for_Choice_left1)
    Choice_left1.bind('<Leave>', on_leave_for_Choice_left1)

    label1 = Label(frame, text=Bad_or_Good(bad_1, good_1)[0], font=("Arial", 34), foreground=Bad_or_Good(bad_1, good_1)[1])
    label1.grid(row=2, column=1, ipadx= 100)

    def on_enter_for_Choice_right1(e):
        if int(info_data_Main_window[-1][4]) != 1 and int(info_data_Main_window[-1][4]) != -1:
            Choice_right1.config(background=color_green, foreground= color_black)
        elif int(info_data_Main_window[-1][4]) == -1: 
            Choice_right1.config(background= color_grey, foreground= color_red)
    def on_leave_for_Choice_right1(e):
        if int(info_data_Main_window[-1][4]) != 1:
            Choice_right1.config(background= color_grey, foreground= color_green)
    Choice_right1 = Button(frame, text='Тренировка', fg=get_color_button([1, -2, -2, -2, -2])[1], bg=get_color_button([1, -2, -2, -2, -2])[0], font=("Arial", 14), activebackground='green', command=Training)
    Choice_right1.grid(row=2, column=2, ipadx= 86, ipady= 20, pady= 5)
    Choice_right1.bind('<Enter>', on_enter_for_Choice_right1)
    Choice_right1.bind('<Leave>', on_leave_for_Choice_right1)

    def on_enter_for_Choice_left2(e):
        if int(info_data_Main_window[-1][5]) != -1:
            Choice_left2.config(background= color_red, foreground= color_black)
    def on_leave_for_Choice_left2(e):
        if int(info_data_Main_window[-1][5]) != -1:
            Choice_left2.config(background= color_grey, foreground= color_red)
    Choice_left2 = Button(frame, text='Никотин', fg=get_color_button([-2, -1, -2, -2, -2])[1], bg=get_color_button([-2, -1, -2, -2, -2])[0], font=("Arial", 14), activebackground='red', command=Nicotine)
    Choice_left2.grid(row=3, column=0, ipadx= 122, ipady= 20, pady= 5)
    Choice_left2.bind('<Enter>', on_enter_for_Choice_left2)
    Choice_left2.bind('<Leave>', on_leave_for_Choice_left2)

    label2 = Label(frame, text=Bad_or_Good(bad_2, good_2)[0], font=("Arial", 34), foreground=Bad_or_Good(bad_2, good_2)[1])
    label2.grid(row=3, column=1, ipadx= 100)

    def on_enter_for_Choice_right2(e):
        if int(info_data_Main_window[-1][5]) != 1 and int(info_data_Main_window[-1][5]) != -1:
            Choice_right2.config(background=color_green, foreground= color_black)
        elif int(info_data_Main_window[-1][5]) == -1: 
            Choice_right2.config(background= color_grey, foreground= color_red)
    def on_leave_for_Choice_right2(e):
        if int(info_data_Main_window[-1][5]) != 1:
            Choice_right2.config(background= color_grey, foreground= color_green)
    Choice_right2 = Button(frame, text='Активность', fg=get_color_button([-2, 1, -2, -2, -2])[1], bg=get_color_button([-2, 1, -2, -2, -2])[0], font=("Arial", 14), activebackground='green', command=Active_Style)
    Choice_right2.grid(row=3, column=2, ipadx= 88, ipady= 20, pady= 5)
    Choice_right2.bind('<Enter>', on_enter_for_Choice_right2)
    Choice_right2.bind('<Leave>', on_leave_for_Choice_right2)

    def on_enter_for_Choice_left3(e):
        if int(info_data_Main_window[-1][6]) != -1:
            Choice_left3.config(background= color_red, foreground= color_black)
    def on_leave_for_Choice_left3(e):
        if int(info_data_Main_window[-1][6]) != -1:
            Choice_left3.config(background= color_grey, foreground= color_red)
    Choice_left3 = Button(frame, text='Игры', font=("Arial", 14), fg=get_color_button([-2, -2, -1, -2, -2])[1], bg=get_color_button([-2, -2, -1, -2, -2])[0], activebackground='red', command=Games)
    Choice_left3.grid(row=4, column=0, ipadx= 134, ipady= 20, pady= 5)
    Choice_left3.bind('<Enter>', on_enter_for_Choice_left3)
    Choice_left3.bind('<Leave>', on_leave_for_Choice_left3)

    label3 = Label(frame, text=Bad_or_Good(bad_3, good_3)[0], font=("Arial", 34), foreground=Bad_or_Good(bad_3, good_3)[1])
    label3.grid(row=4, column=1, ipadx= 100)

    def on_enter_for_Choice_right3(e):
        if int(info_data_Main_window[-1][6]) != 1 and int(info_data_Main_window[-1][6]) != -1:
            Choice_right3.config(background=color_green, foreground= color_black)
        elif int(info_data_Main_window[-1][6]) == -1: 
            Choice_right3.config(background= color_grey, foreground= color_red)
    def on_leave_for_Choice_right3(e):
        if int(info_data_Main_window[-1][6]) != 1:
            Choice_right3.config(background= color_grey, foreground= color_green)
    Choice_right3 = Button(frame, text='Учёба',font=("Arial", 14), fg=get_color_button([-2, -2, 1, -2, -2])[1], bg=get_color_button([-2, -2, 1, -2, -2])[0], activebackground='green', command=Study)
    Choice_right3.grid(row=4, column=2, ipadx= 111, ipady= 20, pady= 5)
    Choice_right3.bind('<Enter>', on_enter_for_Choice_right3)
    Choice_right3.bind('<Leave>', on_leave_for_Choice_right3)

    def on_enter_for_Choice_left4(e):
        if int(info_data_Main_window[-1][7]) != -1:
            Choice_left4.config(background=color_red, foreground= color_black)
    def on_leave_for_Choice_left4(e):
        if int(info_data_Main_window[-1][7]) != -1:
            Choice_left4.config(background= color_grey, foreground= color_red)
    Choice_left4 = Button(frame, text='Потребительский контент', font=("Arial", 14), fg=get_color_button([-2, -2, -2, -1, -2])[1], bg=get_color_button([-2, -2, -2, -1, -2])[0], activebackground='red', command=News_and_Shorts)
    Choice_left4.grid(row=5, column=0, ipadx= 45, ipady= 20, pady= 5)
    Choice_left4.bind('<Enter>', on_enter_for_Choice_left4)
    Choice_left4.bind('<Leave>', on_leave_for_Choice_left4)

    label4 = Label(frame, text=Bad_or_Good(bad_4, good_4)[0], font=("Arial", 34), foreground=Bad_or_Good(bad_4, good_4)[1])
    label4.grid(row=5, column=1, ipadx= 100)

    def on_enter_for_Choice_right4(e):
        if int(info_data_Main_window[-1][7]) != 1 and int(info_data_Main_window[-1][7]) != -1:
            Choice_right4.config(background=color_green, foreground= color_black)
        elif int(info_data_Main_window[-1][7]) == -1: 
            Choice_right4.config(background= color_grey, foreground= color_red)
    def on_leave_for_Choice_right4(e):
        if int(info_data_Main_window[-1][7]) != 1:
            Choice_right4.config(background= color_grey, foreground= color_green)
    Choice_right4 = Button(frame, text='Познавательный контент',font=("Arial", 14), fg=get_color_button([-2, -2, -2, 1, -2])[1], bg=get_color_button([-2, -2, -2, 1, -2])[0], activebackground='green', command=Literature)
    Choice_right4.grid(row=5, column=2, ipadx= 29, ipady= 20, pady= 5)
    Choice_right4.bind('<Enter>', on_enter_for_Choice_right4)
    Choice_right4.bind('<Leave>', on_leave_for_Choice_right4)

    def on_enter_for_Choice_left5(e):
        if int(info_data_Main_window[-1][8]) != -1:
            Choice_left5.config(background=color_red, foreground= color_black)
    def on_leave_for_Choice_left5(e):
        if int(info_data_Main_window[-1][8]) != -1:
            Choice_left5.config(background= color_grey, foreground= color_red)
    Choice_left5 = Button(frame, text='Неправильное питание', font=("Arial", 14), fg=get_color_button([-2, -2, -2, -2, -1])[1], bg=get_color_button([-2, -2, -2, -2, -1])[0], activebackground='red', command=Poor_Nutrition)
    Choice_left5.grid(row=6, column=0, ipadx= 57, ipady= 20, pady= 5)
    Choice_left5.bind('<Enter>', on_enter_for_Choice_left5)
    Choice_left5.bind('<Leave>', on_leave_for_Choice_left5)

    label5 = Label(frame, text=Bad_or_Good(bad_5, good_5)[0], font=("Arial", 34), foreground=Bad_or_Good(bad_5, good_5)[1])
    label5.grid(row=6, column=1, ipadx= 100)

    def on_enter_for_Choice_right5(e):
        if int(info_data_Main_window[-1][8]) != 1 and int(info_data_Main_window[-1][8]) != -1:
            Choice_right5.config(background=color_green, foreground= color_black)
        elif int(info_data_Main_window[-1][8]) == -1: 
            Choice_right5.config(background= color_grey, foreground= color_red)
    def on_leave_for_Choice_right5(e):
        if int(info_data_Main_window[-1][8]) != 1:
            Choice_right5.config(background= color_grey, foreground= color_green)
    Choice_right5 = Button(frame, text='Правильное питание', font=("Arial", 14), fg=get_color_button([-2, -2, -2, -2, 1])[1], bg=get_color_button([-2, -2, -2, -2, 1])[0], activebackground='green', command=Proper_Nutrition)
    Choice_right5.grid(row=6, column=2, ipadx= 48, ipady= 20, pady= 5)
    Choice_right5.bind('<Enter>', on_enter_for_Choice_right5)
    Choice_right5.bind('<Leave>', on_leave_for_Choice_right5)

    def destroy_window():
        Settings.flag_for_windows = 2
        window.destroy()
    def on_enter_for_cal_btn1(e):
        cal_btn1.config(background="#bfbdbd", foreground= color_violet)
    def on_leave_for_cal_btn1(e):
        cal_btn1.config(background= color_grey, foreground= color_black)
    cal_btn1 = Button(frame, text='Ежедневник', bg= color_grey, activebackground= color_violet, font=("Arial", 14), command=destroy_window)
    cal_btn1.grid(row=7, column=0, ipadx= 104, ipady= 25, pady= 10)
    cal_btn1.bind('<Enter>', on_enter_for_cal_btn1)
    cal_btn1.bind('<Leave>', on_leave_for_cal_btn1)

    def on_enter_for_cal_btn2(e):
        cal_btn2.config(background="#bfbdbd", foreground= color_black)
    def on_leave_for_cal_btn2(e):
        cal_btn2.config(background= color_grey, foreground= color_black)
    cal_btn2 = Button(frame, text='Обновить', bg= color_grey, activebackground= color_grey, font=("Arial", 14), command=window.destroy)
    cal_btn2.grid(row=7, column=1, ipadx= 110, ipady= 25, pady= 10)
    cal_btn2.bind('<Enter>', on_enter_for_cal_btn2)
    cal_btn2.bind('<Leave>', on_leave_for_cal_btn2)

    def on_enter_for_cal_btn3(e):
        cal_btn3.config(background="#bfbdbd", foreground= color_black)
    def on_leave_for_cal_btn3(e):
        cal_btn3.config(background= color_grey, foreground= color_black)
    cal_btn3 = Button(frame, text='Закрыть', font=("Arial", 14), bg= color_grey, activebackground= color_grey, command=Exit_from)
    cal_btn3.grid(row=7, column=2, ipadx= 101, ipady= 25, pady= 10)
    cal_btn3.bind('<Enter>', on_enter_for_cal_btn3)
    cal_btn3.bind('<Leave>', on_leave_for_cal_btn3)

    label_space = Label(frame, text="")
    label_space.grid(row=8, column=0, columnspan=3, ipadx= 100)
    label_for_you = Label(frame, text="Я это сделал ради Тебя ♡", font=("Comic Sans MS", 28), foreground=color_violet)
    label_for_you.grid(row=9, column=0, columnspan=3, ipadx= 100)

    mainloop()