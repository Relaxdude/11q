from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
import time
from functools import partial
from tkinter import font
import Settings

day = ""
task = ""
priority = ""
deadline = ""
color_violet = "#805491"
color_green = "#008000"
color_red = "#c92118"
color_grey = "#9b9e9b"
color_light_gray = "#bfbdbd"
color_black = "#000000"
color_yellow = "#edcf24"
color_blue = "#338eb5"
color_background = "#bab1cc"
days_1 = ["Понедельник (Актуальная неделя)", "Вторник (Актуальная неделя)", "Среда (Актуальная неделя)", "Четверг (Актуальная неделя)", "Пятница (Актуальная неделя)", "Суббота (Актуальная неделя)", "Воскресенье (Актуальная неделя)", "Понедельник (Следующая неделя)", "Вторник (Следующая неделя)", "Среда (Следующая неделя)", "Четверг (Следующая неделя)", "Пятница (Следующая неделя)", "Суббота (Следующая неделя)", "Воскресенье (Следующая неделя)"]
prioritys = ["Неважный", "Низкий", "Средний", "Высокий"]
which_week = 1

file = open('info_Weekly.txt', 'r', encoding='utf-8')
info_data_Weekly_window = file.readlines()
for i in range(len(info_data_Weekly_window) - 1):
	info_data_Weekly_window[i] = info_data_Weekly_window[i][:-1]
for i in range(len(info_data_Weekly_window)):
	# for j in range(6):
	info_data_Weekly_window[i] = info_data_Weekly_window[i].split(" ")
	string = ""
	for j in range(6,len(info_data_Weekly_window[i])):
		if j == len(info_data_Weekly_window[i]) - 1:
			string += info_data_Weekly_window[i][j]
		else:
			string += info_data_Weekly_window[i][j] + " "
	info_data_Weekly_window[i][6] = string
	if len(info_data_Weekly_window[i]) > 7:
		for j in range(7,len(info_data_Weekly_window[i])):
			info_data_Weekly_window[i].pop(7)

file.close()

def Exit_from():
    quit()

def what_day_week(number):
	if number < 7:
		return number
	else:
		return number - 7

def eliminating_spaces(string):
	for i in range(len(string)):
		if string[-1] == " ":
			string = string[:-1]
	return string

def window_add_task():

	global days_1
	global prioritys

	def get_message():

		global day
		global task
		global priority
		global deadline
		global info_data_Weekly_window
		global days_1
		global prioritys

		if combobox_day.get() != "" and combobox_deadline.get() != "" and combobox_priority.get() != "" and entry_task.get():
			now = time.localtime()
			if days_1.index(combobox_day.get()) - now[6] + now[7] <= days_1.index(combobox_deadline.get()) - now[6] + now[7]:
				info_data_Weekly_window.append([days_1.index(combobox_day.get()) - now[6] + now[7], now[0], what_day_week(days_1.index(combobox_day.get())), days_1.index(combobox_deadline.get()) - now[6] + now[7], prioritys.index(combobox_priority.get()), 0, eliminating_spaces(entry_task.get())])
				window_add.destroy()
			else:
				mb.showerror("Ошибка", "Дедлайн не может быть раньше чем день задачи")
		else:
			mb.showerror("Ошибка", "Все поля должны быть заполнены")
		
	window_add = Tk()
	window_add.title('Добавить запись')
	window_add.geometry("1240x370+200+165")
	frame = Frame(window_add, highlightbackground= color_black, highlightthickness= 10, height= 100)
	frame.pack(fill=BOTH, expand=1)
	now = time.localtime()

	Label(frame, text="Введи название задачи", font="Arial 20 bold", height= 2).grid(row= 0, column= 1, columnspan= 4, padx= 10)
	Label(frame, text="").grid(row= 0, column= 0)
	Label(frame, text="").grid(row= 0, column= 4)

	entry_task = ttk.Entry(frame, width=100, font=("Arial", 16))
	entry_task.grid(row= 1, column= 1, columnspan= 3)

	Label(frame, text="На какой день назначить задачу", font="Arial 14 bold", height= 2).grid(row= 2, column= 1)
	Label(frame, text="На какой день назначить дедлайн задачи", font="Arial 14 bold", height= 2).grid(row= 2, column= 2)
	Label(frame, text="Приоритет задачи", font="Arial 14 bold", height= 2).grid(row= 2, column= 3)

	# Выбор дня для задачи
	days_2 = []
	for i in range(len(days_1) - now[6]):
		days_2.append(days_1[i + now[6]])
	combobox_day = ttk.Combobox(frame, values= days_2, font=("Arial", 16), width=27, state= "readonly")
	combobox_day.grid(row= 3, column= 1, ipadx= 40)

 	# Выбор дедлайна задачи
	deadlines = []
	for i in range(len(days_1) - now[6]):
		deadlines.append(days_1[i + now[6]])
	combobox_deadline = ttk.Combobox(frame, values= deadlines, font=("Arial", 16), width=27, state= "readonly")
	combobox_deadline.grid(row= 3, column=2, ipadx= 40)

	# Выбор приоритета задачи
	combobox_priority = ttk.Combobox(frame, values= prioritys, font=("Arial", 16), width=27, state= "readonly")
	combobox_priority.grid(row= 3, column= 3)

	def on_enter_for_Button_Save(e):
		Button_Save.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_Save(e):
		Button_Save.config(background= color_grey, foreground= color_black)
	Button_Save = Button(frame, text= 'Добавить', font= "Arial 18 bold", bg= color_grey, height= 3, width= 30, command= get_message)	
	Button_Save.grid(row=4, column= 1, pady= 20, columnspan= 4)
	Button_Save.bind('<Enter>', on_enter_for_Button_Save)
	Button_Save.bind('<Leave>', on_leave_for_Button_Save)

	window_add.mainloop()

def get_color_tasks(index_status):
	if index_status == 1:
		return "#269617"
	elif index_status == 0:
		return "#e06f24"
	elif index_status == -1:
		return color_grey
	elif index_status == -2:
		return "#b32727"

def which_week_day(day):
	now = time.localtime()
	if now[6] >= int(day[2]) and now[7] < int(day[0]) or now[6] < int(day[2]) and now[7] < int(day[0]) and int(day[0]) - now[7] > 6:
		return 2
	else:
		return 1

def get_deadline(day_info):
	if time.localtime()[7] - int(day_info[0]) > 0 or int(day_info[5]) == 1:
		return ""
	else:
		return "\n\nДней осталось: " + str(int(day_info[3]) - time.localtime()[7])

def delete_or_complete_task(data):

	def complete(data_complete):

		data_complete[5] = str(1)
		window_compl_del.destroy()
	
	def delete(data_delete):

		global info_data_Weekly_window

		for i in range(len(info_data_Weekly_window)):
			flag = True
			for j in range(7):
				if info_data_Weekly_window[i][j] != data_delete[j]:
					flag = False
					break
			if flag:
				info_data_Weekly_window.pop(i)
				break
		window_compl_del.destroy()


	window_compl_del = Tk()
	window_compl_del.title('Подтвердите действие')
	window_compl_del.geometry("477x335+835+415")
	frame = Frame(window_compl_del, highlightbackground= "#000000", highlightthickness= 10, height= 50)
	frame.pack(fill=BOTH, expand=1)
	font_1 = font.Font(family= "Arial", size=22, weight="bold")

	Label(frame, text="Удалить задачу\n или отметить что оно выполнено ?", font="Arial 18 bold", height= 7).grid(row= 0, column= 0, columnspan= 4)
	Label(frame, text="").grid(row= 1, column= 0)

	def on_enter_for_Button_Complete(e):
		Button_Complete.config(background= color_green, foreground= color_black)
	def on_leave_for_Button_Complete(e):
		Button_Complete.config(background= color_grey, foreground= color_black)
	Button_Complete = Button(frame, text="Выполнено", height= 3, width= 15, font=("Arial", 18), bg= color_grey, command= partial(complete, data))
	Button_Complete.grid(row= 1, column= 1)
	Button_Complete.bind('<Enter>', on_enter_for_Button_Complete)
	Button_Complete.bind('<Leave>', on_leave_for_Button_Complete)

	Label(frame, text="").grid(row= 1, column= 2)

	def on_enter_for_Button_Delete(e):
		Button_Delete.config(background= color_red, foreground= color_black)
	def on_leave_for_Button_Delete(e):
		Button_Delete.config(background= color_grey, foreground= color_black)
	Button_Delete = Button(frame, text="Удалить", height= 3, width= 15, font=("Arial", 18), bg= color_grey, command= partial(delete, data))
	Button_Delete.grid(row= 1, column= 3)
	Button_Delete.bind('<Enter>', on_enter_for_Button_Delete)
	Button_Delete.bind('<Leave>', on_leave_for_Button_Delete)

	window_compl_del.mainloop()

def state_or_normal(status_task):
	if int(status_task[5]) == -2 or int(status_task[5]) == -1 or (int(status_task[5]) == 1 and int(status_task[0]) < time.localtime()[7]):
		return 'disabled'
	else:
		return 'normal'

def get_max_tasks_on_day(which_week):

	global info_data_Weekly_window
	Max = 0
	if Settings.flag_for_windows == 2:
		for i in range(7):
			local_Max = 0
			for j in range(len(info_data_Weekly_window)):
				if which_week_day(info_data_Weekly_window[j]) == 1 and int(info_data_Weekly_window[j][2]) == i:
					local_Max += 1
					if local_Max > Max:
						Max += 1
	elif Settings.flag_for_windows == 2:
		for i in range(7):
			local_Max = 0
			for j in range(len(info_data_Weekly_window)):
				if which_week_day(info_data_Weekly_window[j]) == 2 and info_data_Weekly_window[j][2] == i:
					local_Max += 1
					if local_Max > Max:
						Max += 1
	return Max

def set_enters(text):
	if len(text) > 20:
		arr_text = text.split(" ")
		print(arr_text)
		text = ""
		len_str = ""
		for i in range(len(arr_text)):
			if len(len_str + arr_text[i]) < 25:
				len_str += arr_text[i] + " "
				if i == len(arr_text) - 1:
					len_str = len_str[:-1]
					text += len_str
			else:
				if len_str == "":
					text += arr_text[i] + "\n"
				else:
					len_str = len_str[:-1] + "\n"
					text += len_str
					len_str = ""
					if i == len(arr_text) - 1:
						text += arr_text[i]
					else:
						len_str += arr_text[i] + " "
	return text


# У каждой задачи должны быть: день[0], год[1], день недели[2], дедлайн[3], приоритет[4], статус выполнено ли[5] (-2(дедлайн прошел), -1(день прошел), 0(ожидание), 1(выполнено)), текст[6]
def weekly_window():

	global info_data_Weekly_window

	main_window = Tk()
	main_window.title('Еженедельник')
	main_window.geometry(str(main_window.winfo_screenwidth() - 65) + "x" + str(main_window.winfo_screenheight()))

	frame_up = Frame(main_window, height= 40)
	frame_up.pack(fill=BOTH,side=TOP)

	main_frame = Frame(main_window)
	main_frame.pack()
	
	my_canvas = Canvas(main_window, highlightthickness= 0)
	my_canvas.pack(expand=1, fill= "both")

	second_frame = Frame(my_canvas, background= color_background)

	my_canvas.create_window((0,0), window=second_frame)

	Label(frame_up, text="", background= color_background).place(x=0, y=0, height=40, width= 1858)
	Label(frame_up, text="Понедельник", font=("Arial", 16), bg= color_grey).place(x=38, y=0, height=40, width= 234)
	Label(frame_up, text="Вторник", font=("Arial", 16), bg= color_grey).place(x=300, y=0, height=40, width= 234)
	Label(frame_up, text="Среда", font=("Arial", 16), bg= color_grey).place(x=562, y=0, height=40, width= 234)
	Label(frame_up, text="Четверг", font=("Arial", 16), bg= color_grey).place(x=824, y=0, height=40, width= 234)
	Label(frame_up, text="Пятница", font=("Arial", 16), bg= color_grey).place(x=1086, y=0, height=40, width= 234)
	Label(frame_up, text="Суббота", font=("Arial", 16), bg= color_grey).place(x=1348, y=0, height=40, width= 234)
	Label(frame_up, text="Воскресенье", font=("Arial", 16), bg= color_grey).place(x=1610, y=0, height=40, width= 234)

	n_row_monday, n_row_tuesday, n_row_wednesday, n_row_thursday, n_row_friday, n_row_saturday, n_row_sunday = 0, 0, 0, 0, 0, 0, 0

	# Сортируем строки задач по приоритету
	info_data_copy = []
	for i in range(4):
		for j in range(len(info_data_Weekly_window)):
			if int(info_data_Weekly_window[j][4]) == 3 and i == 0:
				info_data_copy.append(info_data_Weekly_window[j])
			elif int(info_data_Weekly_window[j][4]) == 2 and i == 1:
				info_data_copy.append(info_data_Weekly_window[j])
			elif int(info_data_Weekly_window[j][4]) == 1 and i == 2:
				info_data_copy.append(info_data_Weekly_window[j])
			elif int(info_data_Weekly_window[j][4]) == 0 and i == 3:
				info_data_copy.append(info_data_Weekly_window[j])
	
	info_data_Weekly_window = info_data_copy
			
	now = time.localtime()

	for i in range(len(info_data_Weekly_window)):
		# Если день прошел и задание не было выполнено
		if (int(info_data_Weekly_window[i][0]) < now[7] and int(info_data_Weekly_window[i][1]) == now[0] or int(info_data_Weekly_window[i][1]) < now[0]) and int(info_data_Weekly_window[i][5]) == 0:
			#Если дедлайн прошел
			if int(info_data_Weekly_window[i][3]) < now[7]:
				info_data_Weekly_window[i][5] = -2
			# Дедлайн ещё не прошел, и день уже закончился
			else:
				info_data_Weekly_window.append([now[7],  now[0], now[6], info_data_Weekly_window[i][3], info_data_Weekly_window[i][4], 0, info_data_Weekly_window[i][6]])
				info_data_Weekly_window[i][5] = -1
	
	now = time.localtime()

	arr_for_delete = []
	# Находим инфу, прошлой недели (ненужной)
	for i in range(len(info_data_Weekly_window)):
		# Находим что неделя прошлая от актуальной, то есть ненужная. Нужны актуальная и следующая
		if int(info_data_Weekly_window[i][2]) > now[6] and int(info_data_Weekly_window[i][0]) < now[7] or int(info_data_Weekly_window[i][2]) <= now[6] and int(info_data_Weekly_window[i][0]) < now[7] and now[7] - int(info_data_Weekly_window[i][0]) > 6:
			if (int(info_data_Weekly_window[i][5]) == 0 or int(info_data_Weekly_window[i][5]) == -1) and now[7] <= int(info_data_Weekly_window[i][3]):
				info_data_Weekly_window.append([now[7],  now[0], now[6], info_data_Weekly_window[i][3], info_data_Weekly_window[i][4], 0, info_data_Weekly_window[i][6]])
				info_data_Weekly_window.pop(i)
			elif int(info_data_Weekly_window[i][5]) == -2 and now[7] > int(info_data_Weekly_window[i][3]):
				arr_for_delete.append(i)
	for i in arr_for_delete:
		info_data_Weekly_window.pop(i)

	file = open('info_Weekly.txt', 'w', encoding='utf-8')
	for i in range(len(info_data_Weekly_window)):
		x = " ".join(str(el) for el in info_data_Weekly_window[i])
		if i == len(info_data_Weekly_window) - 1:
			file.write(x)
		else:
			file.write(x + '\n')
	file.close()

	for i in range(7):
		if i == 6:
			Label(second_frame, text= "", width = 32, height=0, background= color_background).grid(row= 0, column= i + 1, padx= 16)
		else:
			Label(second_frame, text= "", width = 32, height=0, background= color_background).grid(row= 0, column= i + 1, padx= 16)
	if get_max_tasks_on_day(which_week) < 6:
		for i in range(1, 8):
			Label(second_frame, text= "", width = 0, height=6, background= color_background).grid(row= i, column= 0, pady= 26, padx= 10)
	else:
		for i in range(1, get_max_tasks_on_day(which_week) + 3):
			Label(second_frame, text= "", width = 0, height=6, background= color_background).grid(row= i, column= 0, pady= 26, padx= 10)

	if Settings.flag_for_windows == 2:
		for i in range(len(info_data_Weekly_window)):
			if int(info_data_Weekly_window[i][2]) == 0 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_monday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_monday, column=1)
			elif int(info_data_Weekly_window[i][2]) == 1 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_tuesday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_tuesday, column=2)
			elif int(info_data_Weekly_window[i][2]) == 2 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_wednesday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_wednesday, column=3)
			elif int(info_data_Weekly_window[i][2]) == 3 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_thursday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_thursday, column=4)
			elif int(info_data_Weekly_window[i][2]) == 4 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_friday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_friday, column=5)
			elif int(info_data_Weekly_window[i][2]) == 5 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_saturday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_saturday, column=6)
			elif int(info_data_Weekly_window[i][2]) == 6 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_sunday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_sunday, column=7)
	elif Settings.flag_for_windows == 3:
		for i in range(len(info_data_Weekly_window)):
			if int(info_data_Weekly_window[i][2]) == 0 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_monday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_monday, column=1)
			elif int(info_data_Weekly_window[i][2]) == 1 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_tuesday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_tuesday, column=2)
			elif int(info_data_Weekly_window[i][2]) == 2 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_wednesday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_wednesday, column=3)
			elif int(info_data_Weekly_window[i][2]) == 3 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_thursday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_thursday, column=4)
			elif int(info_data_Weekly_window[i][2]) == 4 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_friday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_friday, column=5)
			elif int(info_data_Weekly_window[i][2]) == 5 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_saturday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_saturday, column=6)
			elif int(info_data_Weekly_window[i][2]) == 6 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_sunday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(int(info_data_Weekly_window[i][5])), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_sunday, column=7)
	
	frame_bottom = Frame(main_window, bg=color_red)
	frame_bottom.place(x=0,y=930, height= 127, width= 1858)

	Label(frame_bottom, text="", bg= color_black).place(x=0, y=0, height=127, width= 1858)

	def go_to_main_window():
		Settings.flag_for_windows = 1
		main_window.destroy()
		
	def on_enter_for_Button_to_Main(e):
		Button_to_Main.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_to_Main(e):
		Button_to_Main.config(background= color_grey, foreground= color_black)
	Button_to_Main = Button(frame_bottom, text='Главная', font=("Arial", 16), bg= color_grey, command= go_to_main_window)
	Button_to_Main.place(x=20, y=20, height=80, width= 286)
	Button_to_Main.bind('<Enter>', on_enter_for_Button_to_Main)
	Button_to_Main.bind('<Leave>', on_leave_for_Button_to_Main)

	def on_enter_for_Button_Add(e):
		Button_Add.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_Add(e):
		Button_Add.config(background= color_grey, foreground= color_black)
	Button_Add = Button(frame_bottom, text='Добавить', font=("Arial", 16), bg= color_grey, command= window_add_task)
	Button_Add.place(x=326, y=20, height=80, width= 286)
	Button_Add.bind('<Enter>', on_enter_for_Button_Add)
	Button_Add.bind('<Leave>', on_leave_for_Button_Add)

	def on_enter_for_Button_Update(e):
		Button_Update.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_Update(e):
		Button_Update.config(background= color_grey, foreground= color_black)
	Button_Update = Button(frame_bottom, text='Обновить', font=("Arial", 16), bg= color_grey, command= main_window.destroy)
	Button_Update.place(x=632, y=20, height=80, width= 286)
	Button_Update.bind('<Enter>', on_enter_for_Button_Update)
	Button_Update.bind('<Leave>', on_leave_for_Button_Update)

	def on_enter_for_Button_close(e):
		Button_close.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_close(e):
		Button_close.config(background= color_grey, foreground= color_black)
	Button_close = Button(frame_bottom, text='Закрыть', font=("Arial", 16), bg= color_grey, command= Exit_from)
	Button_close.place(x=938, y=20, height=80, width= 286)
	Button_close.bind('<Enter>', on_enter_for_Button_close)
	Button_close.bind('<Leave>', on_leave_for_Button_close)
		
	def go_to_window_week_1():
		if Settings.flag_for_windows == 2:
			pass
		else:
			Settings.flag_for_windows = 2
			main_window.destroy()

	def on_enter_for_Button_week_1(e):
		Button_week_1.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_week_1(e):
		Button_week_1.config(background= color_grey, foreground= color_black)
	Button_week_1 = Button(frame_bottom, text='1 неделя', font=("Arial", 16), bg= color_grey, command= go_to_window_week_1)
	Button_week_1.place(x=1244, y=20, height=80, width= 286)
	Button_week_1.bind('<Enter>', on_enter_for_Button_week_1)
	Button_week_1.bind('<Leave>', on_leave_for_Button_week_1)

	def go_to_window_week_2():
		if Settings.flag_for_windows == 3:
			pass
		else:
			Settings.flag_for_windows = 3
			main_window.destroy()
		
	def on_enter_for_Button_week_2(e):
		Button_week_2.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_week_2(e):
		Button_week_2.config(background= color_grey, foreground= color_black)
	Button_week_2 = Button(frame_bottom, text='2 неделя', font=("Arial", 16), bg= color_grey, command= go_to_window_week_2)
	Button_week_2.place(x=1550, y=20, height=80, width= 286)
	Button_week_2.bind('<Enter>', on_enter_for_Button_week_2)
	Button_week_2.bind('<Leave>', on_leave_for_Button_week_2)

	def _on_mousewheel(event: Event):
		my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
	my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
	my_canvas.bind_all("<MouseWheel>", _on_mousewheel)

	main_window.mainloop()