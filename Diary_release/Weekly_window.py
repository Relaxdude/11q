from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
import time
from functools import partial
import Settings

day = ""
task = ""
priority = ""
deadline = ""
color_violet = "#805491"
color_green = "#008000"
color_red = "#b32727"
color_grey = "#9b9e9b"
color_light_gray = "#bfbdbd"
color_black = "#000000"
color_yellow = "#edcf24"
color_blue = "#338eb5"
color_orange = "#d67222"
color_background = "#bab1cc"
color_dark_gray = "#454443"
days_1 = ["Понедельник (Актуальная неделя)", "Вторник (Актуальная неделя)", "Среда (Актуальная неделя)", "Четверг (Актуальная неделя)", "Пятница (Актуальная неделя)", "Суббота (Актуальная неделя)", "Воскресенье (Актуальная неделя)", "Понедельник (Следующая неделя)", "Вторник (Следующая неделя)", "Среда (Следующая неделя)", "Четверг (Следующая неделя)", "Пятница (Следующая неделя)", "Суббота (Следующая неделя)", "Воскресенье (Следующая неделя)"]
prioritys = ["Неважный", "Низкий", "Средний", "Высокий"]
Buttons_Everyday_isactive= [False, False, False, False, False, False, False]
which_week = 1
arr_days_for_everyday = []
count_tasks_today = 0
flag_for_last_day = False

file = open('info_Weekly.txt', 'r', encoding='utf-8')
info_data_Weekly_window = file.readlines()
for i in range(len(info_data_Weekly_window) - 1):
	info_data_Weekly_window[i] = info_data_Weekly_window[i][:-1]
for i in range(len(info_data_Weekly_window)):
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

def write_data():

	global info_data_Weekly_window

	file = open('info_Weekly.txt', 'w', encoding='utf-8')
	for i in range(len(info_data_Weekly_window)):
		x = " ".join(str(el) for el in info_data_Weekly_window[i])
		if i == len(info_data_Weekly_window) - 1:
			file.write(x)
		else:
			file.write(x + '\n')
	file.close()

def get_true_day(data):
	now = time.localtime()
	if int(data[1]) == 1:
		if int(data[0]) < now[6]:
			return now[7] - (now[6] - int(data[0])) + 7
		else:
			return now[7] + (int(data[0]) - now[6]) + 7
	else:
		if int(data[0]) < now[6]:
			return now[7] - (now[6] - int(data[0]))
		else:
			return now[7] + (int(data[0]) - now[6])

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

def get_weekly_tasks_count():

	global info_data_Weekly_window

	count_tasks_today = 0
	for i in range(len(info_data_Weekly_window)):
		if int(info_data_Weekly_window[i][0]) == time.localtime()[7] and int(info_data_Weekly_window[i][5]) != 1:
			count_tasks_today += 1
	return "Осталось выполнить заданий: " + str(count_tasks_today)

def get_color_tasks(data_string):
	if int(data_string[5]) == 1:
		return "#269617"
	elif int(data_string[5]) == 0 or (int(data_string[5]) == 2 and time.localtime()[7] <= int(data_string[0])):
		return "#e06f24"
	elif int(data_string[5]) == -1 or (int(data_string[5]) == 2 and time.localtime()[7] > int(data_string[0])):
		return color_grey
	elif int(data_string[5]) == -2:
		return "#b32727"

def which_week_day(day):
	if int(day[1]) == 0:
		if int(day[3]) == 0:
			return 1
		else:
			return 2
	else:
		now = time.localtime()
		if now[6] >= int(day[2]) and now[7] < int(day[0]) or now[6] < int(day[2]) and now[7] < int(day[0]) and int(day[0]) - now[7] > 6:
			return 2
		else:
			return 1

def get_deadline(day_info):
	if time.localtime()[7] - int(day_info[0]) > 0 or int(day_info[5]) == 1 or int(day_info[5]) == 2:
		return ""
	else:
		return "\n\nДней осталось: " + str(int(day_info[3]) - time.localtime()[7])
	
def update_last_day(window):
	
	global flag_for_last_day

	if Settings.flag_for_windows == 3:
		pass
	else:
		Settings.where_flag_for_windows = 0
		if flag_for_last_day:
			flag_for_last_day = False
			window.destroy()
		else:
			flag_for_last_day = True
			window.destroy()

def state_or_normal(status_task):

	global flag_for_last_day

	if flag_for_last_day:
		if int(status_task[5]) == -1 or int(status_task[5]) == 2 and (time.localtime()[6] != 0 and Settings.flag_for_windows == 2 and time.localtime()[7] - int(status_task[0]) == 1):
			return 'normal'
		else:
			return 'disabled'
	else:
		if int(status_task[5]) == -2 or int(status_task[5]) == -1 or int(status_task[5]) == 1 or (int(status_task[5]) == 2 and time.localtime()[7] > int(status_task[0])):
			return 'disabled'
		else:
			return 'normal'

def get_max_tasks_on_day():

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


# У каждой задачи должны быть: день[0], год[1], день недели[2], дедлайн[3], приоритет[4],
#  статус выполнено ли[5] (-2(дедлайн прошел), -1(день прошел), 0(ожидание), 1(выполнено), 2(ежедневка не выполнена), 3(ежедневка выполнена)), текст[6]
def weekly_window():

	Settings.where_flag_for_windows = 1

	def window_add_task(data = []):

		global days_1
		global prioritys

		def get_message(data):

			global day
			global task
			global priority
			global deadline
			global info_data_Weekly_window
			global days_1
			global prioritys

			if combobox_day.get() != "" and combobox_deadline.get() != "" and combobox_priority.get() != "" and entry_task.get() != "":
					now = time.localtime()
					if days_1.index(combobox_day.get()) - now[6] + now[7] <= days_1.index(combobox_deadline.get()) - now[6] + now[7]:
						if len(data) == 0:
							info_data_Weekly_window.append([str(days_1.index(combobox_day.get()) - now[6] + now[7]), str(now[0]), str(what_day_week(days_1.index(combobox_day.get()))), str(days_1.index(combobox_deadline.get()) - now[6] + now[7]), str(prioritys.index(combobox_priority.get())), str(0), str(eliminating_spaces(entry_task.get()))])
							write_data()
							window_add.grab_release()
							window_add.destroy()
							main_window.destroy()
						else:
							data[0] = str(days_1.index(combobox_day.get()) - now[6] + now[7])
							data[2] = str(what_day_week(days_1.index(combobox_day.get())))
							data[3] = str(days_1.index(combobox_deadline.get()) - now[6] + now[7])
							data[4] = str(prioritys.index(combobox_priority.get()))
							data[6] = str(eliminating_spaces(entry_task.get()))
							write_data()
							window_add.grab_release()
							window_add.destroy()
							main_window.destroy()
					else:
						mb.showerror("Ошибка", "Дедлайн не может быть раньше чем день задачи")
			else:
				mb.showerror("Ошибка", "Все поля должны быть заполнены")
		
		window_add = Toplevel()
		window_add.title('Данные задания')
		window_add.geometry("1240x370+309+340")
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
		Button_Save = Button(frame, text= 'Добавить', font= "Arial 18 bold", bg= color_grey, height= 3, width= 30, command= lambda: get_message(data))	
		Button_Save.grid(row=4, column= 1, pady= 20, columnspan= 4)
		Button_Save.bind('<Enter>', on_enter_for_Button_Save)
		Button_Save.bind('<Leave>', on_leave_for_Button_Save)

		window_add.grab_set()
	
	def window_add_task_everyday(data = []):

		global days_1
		global prioritys
		global arr_days_for_everyday
		global Buttons_Everyday_isactive

		def get_message(data = []):
			
			global day
			global task
			global priority
			global deadline
			global info_data_Weekly_window
			global days_1
			global prioritys
			global arr_days_for_everyday
			global Buttons_Everyday_isactive
			# У каждой ежедневной задачи должны быть: день[0], год[1], день недели[2], номер недели[3], приоритет[4],
			#  статус выполнено ли[5] (-2(дедлайн прошел), -1(день прошел), 0(ожидание), 1(выполнено), 2(ежедневка не выполнена)), текст[6]
			if len(arr_days_for_everyday) != 0 and combobox_priority.get() != "" and entry_task.get() != "":
				if len(data) != 0:
					for i in reversed(range(len(info_data_Weekly_window))):
						if int(info_data_Weekly_window[i][1]) == 0 and int(info_data_Weekly_window[i][4]) == int(data[4]) and info_data_Weekly_window[i][6] == data[6]:
							info_data_Weekly_window.pop(i)
				for i in range(len(arr_days_for_everyday)):
						info_data_Weekly_window.append([str(get_true_day([arr_days_for_everyday[i], 0])), str(0), str(arr_days_for_everyday[i]), str(0), str(prioritys.index(combobox_priority.get())), str(2), str(eliminating_spaces(entry_task.get()))])
						info_data_Weekly_window.append([str(get_true_day([arr_days_for_everyday[i], 1])), str(0), str(arr_days_for_everyday[i]), str(1), str(prioritys.index(combobox_priority.get())), str(2), str(eliminating_spaces(entry_task.get()))])

				write_data()
				window_add_everyday.grab_release()
				window_add_everyday.destroy()
				main_window.destroy()
			else:
				mb.showerror("Ошибка", "Все поля должны быть заполнены")
		
		def set_day_everyday(day):

			global arr_days_for_everyday
			global Buttons_Everyday_isactive

			if Buttons_Everyday_isactive[day] == False: 
				Buttons_Everyday_isactive[day] = True

			flag = True
			for i in range(len(arr_days_for_everyday)):
				if arr_days_for_everyday[i] == day:
					Buttons_Everyday_isactive[day] = False
					flag = False
					arr_days_for_everyday.remove(arr_days_for_everyday[i])
					break
			if flag:
				arr_days_for_everyday.append(day)
			else:
				pass
			write_data()
		
		window_add_everyday = Toplevel()
		window_add_everyday.title('Добавить ежедневное задание')
		window_add_everyday.geometry("1240x650+309+200")
		frame = Frame(window_add_everyday, highlightbackground= color_black, highlightthickness= 10, height= 100)
		frame.pack(fill=BOTH, expand=1)		
		Buttons_Everyday_isactive= [False, False, False, False, False, False, False]
		arr_days_for_everyday = []									

		Label(frame, text="Введи название задачи", font="Arial 20 bold", height= 2).grid(row= 0, column= 1, columnspan= 4, padx= 10)
		Label(frame, text="").grid(row= 0, column= 0)
		Label(frame, text="").grid(row= 0, column= 4)

		entry_task = ttk.Entry(frame, width=100, font=("Arial", 16))
		entry_task.grid(row= 1, column= 1, columnspan= 3)

		Label(frame, text="На какой день назначить задачу", font="Arial 16 bold", height= 2).grid(row= 2, column= 1)
		Label(frame, text="Приоритет задачи", font="Arial 14 bold", height= 2).grid(row= 2, column= 2)

		# Выбор дня для ежедневной задачи
		def on_enter_for_Button_Monday(e):
			if Buttons_Everyday_isactive[0]:
				Button_Monday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Monday.config(background= color_grey, foreground= color_black)
		def on_leave_for_Button_Monday(e):
			if Buttons_Everyday_isactive[0]:
				Button_Monday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Monday.config(background= color_grey, foreground= color_black)
		Button_Monday = Button(frame, text= "Понедельник", background= color_grey, activebackground= color_dark_gray, font=("Arial", 16), height= 2, width= 20, command= lambda: set_day_everyday(0))
		Button_Monday.grid(row= 3, column= 1)
		Button_Monday.bind('<Enter>', on_enter_for_Button_Monday)
		Button_Monday.bind('<Leave>', on_leave_for_Button_Monday)

		def on_enter_for_Button_Tuesday(e):
			if Buttons_Everyday_isactive[1]:
				Button_Tuesday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Tuesday.config(background= color_grey, foreground= color_black)
		def on_leave_for_Button_Tuesday(e):
			if Buttons_Everyday_isactive[1]:
				Button_Tuesday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Tuesday.config(background= color_grey, foreground= color_black)
		Button_Tuesday = Button(frame, text= "Вторник", background= color_grey, activebackground= color_dark_gray, font=("Arial", 16), height= 2, width= 20, command= lambda: set_day_everyday(1))
		Button_Tuesday.grid(row= 4, column= 1)
		Button_Tuesday.bind('<Enter>', on_enter_for_Button_Tuesday)
		Button_Tuesday.bind('<Leave>', on_leave_for_Button_Tuesday)

		def on_enter_for_Button_Wednesday(e):
			if Buttons_Everyday_isactive[2]:
				Button_Wednesday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Wednesday.config(background= color_grey, foreground= color_black)
		def on_leave_for_Button_Wednesday(e):
			if Buttons_Everyday_isactive[2]:
				Button_Wednesday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Wednesday.config(background= color_grey, foreground= color_black)
		Button_Wednesday = Button(frame, text= "Среда", background= color_grey, activebackground= color_dark_gray, font=("Arial", 16), height= 2, width= 20, command= lambda: set_day_everyday(2))
		Button_Wednesday.grid(row= 5, column= 1)
		Button_Wednesday.bind('<Enter>', on_enter_for_Button_Wednesday)
		Button_Wednesday.bind('<Leave>', on_leave_for_Button_Wednesday)

		def on_enter_for_Button_Thursday(e):
			if Buttons_Everyday_isactive[3]:
				Button_Thursday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Thursday.config(background= color_grey, foreground= color_black)
		def on_leave_for_Button_Thursday(e):
			if Buttons_Everyday_isactive[3]:
				Button_Thursday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Thursday.config(background= color_grey, foreground= color_black)
		Button_Thursday = Button(frame, text= "Четверг", background= color_grey, activebackground= color_dark_gray, font=("Arial", 16), height= 2, width= 20, command= lambda: set_day_everyday(3))
		Button_Thursday.grid(row= 6, column= 1)
		Button_Thursday.bind('<Enter>', on_enter_for_Button_Thursday)
		Button_Thursday.bind('<Leave>', on_leave_for_Button_Thursday)

		def on_enter_for_Button_Friday(e):
			if Buttons_Everyday_isactive[4]:
				Button_Friday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Friday.config(background= color_grey, foreground= color_black)
		def on_leave_for_Button_Friday(e):
			if Buttons_Everyday_isactive[4]:
				Button_Friday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Friday.config(background= color_grey, foreground= color_black)
		Button_Friday = Button(frame, text= "Пятница", background= color_grey, activebackground= color_dark_gray, font=("Arial", 16), height= 2, width= 20, command= lambda: set_day_everyday(4))
		Button_Friday.grid(row= 7, column= 1)
		Button_Friday.bind('<Enter>', on_enter_for_Button_Friday)
		Button_Friday.bind('<Leave>', on_leave_for_Button_Friday)

		def on_enter_for_Button_Saturday(e):
			if Buttons_Everyday_isactive[5]:
				Button_Saturday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Saturday.config(background= color_grey, foreground= color_black)
		def on_leave_for_Button_Saturday(e):
			if Buttons_Everyday_isactive[5]:
				Button_Saturday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Saturday.config(background= color_grey, foreground= color_black)
		Button_Saturday = Button(frame, text= "Суббота", background= color_grey, activebackground= color_dark_gray, font=("Arial", 16), height= 2, width= 20, command= lambda: set_day_everyday(5))
		Button_Saturday.grid(row= 8, column= 1)
		Button_Saturday.bind('<Enter>', on_enter_for_Button_Saturday)
		Button_Saturday.bind('<Leave>', on_leave_for_Button_Saturday)

		def on_enter_for_Button_Sunday(e):
			if Buttons_Everyday_isactive[6]:
				Button_Sunday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Sunday.config(background= color_grey, foreground= color_black)
		def on_leave_for_Button_Sunday(e):
			if Buttons_Everyday_isactive[6]:
				Button_Sunday.config(background= color_dark_gray, foreground= color_black)
			else:
				Button_Sunday.config(background= color_grey, foreground= color_black)
		Button_Sunday = Button(frame, text= "Воскресенье", background= color_grey, activebackground= color_dark_gray, font=("Arial", 16), height= 2, width= 20, command= lambda: set_day_everyday(6))
		Button_Sunday.grid(row= 9, column= 1)
		Button_Sunday.bind('<Enter>', on_enter_for_Button_Sunday)
		Button_Sunday.bind('<Leave>', on_leave_for_Button_Sunday)

		# Выбор приоритета задачи
		combobox_priority = ttk.Combobox(frame, values= prioritys, font=("Arial", 16), width=27, state= "readonly")
		combobox_priority.grid(row= 3, column= 2)

		def on_enter_for_Button_Save(e):
			Button_Save.config(background= color_light_gray, foreground= color_black)
		def on_leave_for_Button_Save(e):
			Button_Save.config(background= color_grey, foreground= color_black)
		Button_Save = Button(frame, text= 'Добавить', font= "Arial 18 bold", bg= color_grey, height= 3, width= 30, command= lambda: get_message(data))	
		Button_Save.grid(row=2, column= 3, pady= 20, rowspan= 8)
		Button_Save.bind('<Enter>', on_enter_for_Button_Save)
		Button_Save.bind('<Leave>', on_leave_for_Button_Save)

		window_add_everyday.grab_set()

	def delete_or_complete_task(data):

		def update(data):

			global info_data_Weekly_window

			if flag_for_last_day:
				mb.showerror("Ошибка", "Нельзя изменить задание прошлого дня")
				window_compl_del.grab_release() 
				window_compl_del.destroy()
			else:
				window_compl_del.grab_release() 
				window_compl_del.destroy()
				if int(data[1]) == 0:			
					window_add_task_everyday(data)
				else:
					window_add_task(data)

		def complete(data_complete):
			
			if int(data_complete[1]) == 0 and int(data_complete[0]) != time.localtime()[7] and flag_for_last_day == False:
				mb.showerror("Ошибка", "Ежедневное задание должно выполнятся в свой же день")
				window_compl_del.grab_release() 
				window_compl_del.destroy()
			else:
				data_complete[5] = str(1)
				write_data()
				window_compl_del.grab_release() 
				window_compl_del.destroy()
				main_window.destroy()
					
		def delete(data_delete):

			global info_data_Weekly_window

			if flag_for_last_day:
				mb.showerror("Ошибка", "Нельзя удалить задание прошлого дня")
				window_compl_del.grab_release() 
				window_compl_del.destroy()
			else:
				if int(data_delete[1]) == 0:
					arr_index_for_delete_everyday = []
					for i in range(len(info_data_Weekly_window)):
						if int(info_data_Weekly_window[i][1]) == 0:
							if info_data_Weekly_window[i][6] == data_delete[6]:
								arr_index_for_delete_everyday.append(info_data_Weekly_window[i])
					for i in arr_index_for_delete_everyday:
						info_data_Weekly_window.remove(i)
				else:
					info_data_Weekly_window.remove(data_delete)
				write_data()
				window_compl_del.grab_release() 
				window_compl_del.destroy()
				main_window.destroy()

		window_compl_del = Toplevel()
		window_compl_del.title('Подтвердите действие')
		window_compl_del.geometry("478x445+724+357")
		frame = Frame(window_compl_del, highlightbackground= "#000000", highlightthickness= 10, height= 50)
		frame.pack(fill=BOTH, expand=1)

		Label(frame, text="Удалить задачу, изменить,\n или отметить что оно выполнено ?", font="Arial 18 bold", height= 7).grid(row= 0, column= 0, columnspan= 4)
		Label(frame, text="").grid(row= 1, column= 0)

		def on_enter_for_Button_Update(e):
			Button_Update.config(background= color_light_gray, foreground= color_black)
		def on_leave_for_Button_Update(e):
			Button_Update.config(background= color_grey, foreground= color_black)
		Button_Update = Button(frame, text="Изменить", height= 3, width= 31, font=("Arial", 18), bg= color_grey, command= partial(update, data))
		Button_Update.grid(row= 1, column= 1, columnspan= 3)
		Button_Update.bind('<Enter>', on_enter_for_Button_Update)
		Button_Update.bind('<Leave>', on_leave_for_Button_Update)

		def on_enter_for_Button_Complete(e):
			Button_Complete.config(background= color_green, foreground= color_black)
		def on_leave_for_Button_Complete(e):
			Button_Complete.config(background= color_grey, foreground= color_black)
		Button_Complete = Button(frame, text="Выполнено", height= 3, width= 15, font=("Arial", 18), bg= color_grey, command= partial(complete, data))
		Button_Complete.grid(row= 2, column= 1, pady= 5)
		Button_Complete.bind('<Enter>', on_enter_for_Button_Complete)
		Button_Complete.bind('<Leave>', on_leave_for_Button_Complete)

		Label(frame, text="").grid(row= 2, column= 2)

		def on_enter_for_Button_Delete(e):
			Button_Delete.config(background= color_red, foreground= color_black)
		def on_leave_for_Button_Delete(e):
			Button_Delete.config(background= color_grey, foreground= color_black)
		Button_Delete = Button(frame, text="Удалить", height= 3, width= 15, font=("Arial", 18), bg= color_grey, command= partial(delete, data))
		Button_Delete.grid(row= 2, column= 3)
		Button_Delete.bind('<Enter>', on_enter_for_Button_Delete)
		Button_Delete.bind('<Leave>', on_leave_for_Button_Delete)

		window_compl_del.grab_set()

	global info_data_Weekly_window

	main_window = Tk()
	main_window.title('Еженедельник')
	main_window.geometry(str(main_window.winfo_screenwidth() - 65) + "x" + str(main_window.winfo_screenheight()))
	main_window.attributes('-fullscreen',True)

	frame_up = Frame(main_window, height= 60)
	frame_up.pack(fill=BOTH,side=TOP)

	main_frame = Frame(main_window)
	main_frame.pack()
	
	my_canvas = Canvas(main_window, highlightthickness= 0)
	my_canvas.pack(expand=1, fill= "both")

	second_frame = Frame(my_canvas, background= color_background)

	my_canvas.create_window((0,0), window=second_frame)

	Label(frame_up, text="", background= color_background).place(x=0, y=0, height=60, width= 1920)
	Label(frame_up, text="Понедельник", font=("Arial", 16), bg= color_grey).place(x=55, y=10, height=40, width= 235)
	Label(frame_up, text="Вторник", font=("Arial", 16), bg= color_grey).place(x=317, y=10, height=40, width= 235)
	Label(frame_up, text="Среда", font=("Arial", 16), bg= color_grey).place(x=579, y=10, height=40, width= 235)
	Label(frame_up, text="Четверг", font=("Arial", 16), bg= color_grey).place(x=841, y=10, height=40, width= 235)
	Label(frame_up, text="Пятница", font=("Arial", 16), bg= color_grey).place(x=1103, y=10, height=40, width= 235)
	Label(frame_up, text="Суббота", font=("Arial", 16), bg= color_grey).place(x=1365, y=10, height=40, width= 235)
	Label(frame_up, text="Воскресенье", font=("Arial", 16), bg= color_grey).place(x=1627, y=10, height=40, width= 235)

	n_row_monday, n_row_tuesday, n_row_wednesday, n_row_thursday, n_row_friday, n_row_saturday, n_row_sunday = 0, 0, 0, 0, 0, 0, 0
				
	now = time.localtime()

	arr_for_delete = []
	arr_for_double = []
	# Находим инфу, прошлой недели (ненужной)
	for i in range(len(info_data_Weekly_window)):
		# Находим что неделя прошлая от актуальной, то есть ненужная. Нужны актуальная и следующая
		if (int(info_data_Weekly_window[i][2]) > now[6] and int(info_data_Weekly_window[i][0]) < now[7]) or (int(info_data_Weekly_window[i][2]) <= now[6] and int(info_data_Weekly_window[i][0]) < now[7] and now[7] - int(info_data_Weekly_window[i][0]) > 6):
			if int(info_data_Weekly_window[i][1]) == 0:
				info_data_Weekly_window[i][0] = str(int(info_data_Weekly_window[i][0]) + 7)
				info_data_Weekly_window[i][5] = str(2)
				for j in range(len(info_data_Weekly_window)):
					if int(info_data_Weekly_window[i][1]) == 0 and info_data_Weekly_window[i][0] == info_data_Weekly_window[j][0] and info_data_Weekly_window[i][6] == info_data_Weekly_window[j][6] and info_data_Weekly_window[j][3] == "1":
						info_data_Weekly_window[j][0] = str(int(info_data_Weekly_window[j][0]) + 7)
			elif (int(info_data_Weekly_window[i][5]) == 0 or int(info_data_Weekly_window[i][5]) == -1) and now[7] <= int(info_data_Weekly_window[i][3]):
				flag = False
				for j in arr_for_double:
					if info_data_Weekly_window[i][3] == j[3] and info_data_Weekly_window[i][4] == j[4] and info_data_Weekly_window[i][6] == j[6]:
						flag = True
				if flag:
					arr_for_delete.append(info_data_Weekly_window[i])
				else:
					arr_for_double.append(info_data_Weekly_window[i])
					arr_for_delete.append(info_data_Weekly_window[i])
					info_data_Weekly_window.append([now[7],  now[0], now[6], info_data_Weekly_window[i][3], info_data_Weekly_window[i][4], 0, info_data_Weekly_window[i][6]])
			elif (int(info_data_Weekly_window[i][5]) == -2 and now[7] > int(info_data_Weekly_window[i][3])) or (int(info_data_Weekly_window[i][5]) == 1) or (now[6] == 0 and now[7] > int(info_data_Weekly_window[i][3]) and int(info_data_Weekly_window[i][5]) == -1):
				arr_for_delete.append(info_data_Weekly_window[i])
	for i in arr_for_delete:
		info_data_Weekly_window.remove(i)
	
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
	
	#Удаляем задания которые были выполнены в прошлый день
	arr_for_update_last_days, arr_for_delete = [], []
	for i in range(len(info_data_Weekly_window)):
		if i == 24:
			pass
		if int(info_data_Weekly_window[i][5]) == 1 and int(info_data_Weekly_window[i][1]) != 0:
			arr_for_update_last_days.append(info_data_Weekly_window[i])
	for i in range(len(info_data_Weekly_window)):
		for j in arr_for_update_last_days:
			if info_data_Weekly_window[i][3] == j[3] and info_data_Weekly_window[i][4] == j[4] and int(info_data_Weekly_window[i][5]) == 0 and info_data_Weekly_window[i][6] == j[6]:
				arr_for_delete.append(info_data_Weekly_window[i])
	for i in arr_for_delete:
		info_data_Weekly_window.remove(i)
	
	# Сортируем строки задач по приоритету
	arr_data_complete = []
	info_data_copy = []
	for i in range(4):
		for j in range(len(info_data_Weekly_window)):
			if int(info_data_Weekly_window[j][4]) == 3 and i == 0 and int(info_data_Weekly_window[j][5]) != 1:
				info_data_copy.append(info_data_Weekly_window[j])
			elif int(info_data_Weekly_window[j][4]) == 2 and i == 1 and int(info_data_Weekly_window[j][5]) != 1:
				info_data_copy.append(info_data_Weekly_window[j])
			elif int(info_data_Weekly_window[j][4]) == 1 and i == 2 and int(info_data_Weekly_window[j][5]) != 1:
				info_data_copy.append(info_data_Weekly_window[j])
			elif int(info_data_Weekly_window[j][4]) == 0 and i == 3 and int(info_data_Weekly_window[j][5]) != 1:
				info_data_copy.append(info_data_Weekly_window[j])
	for i in range(len(info_data_Weekly_window)):
		if int(info_data_Weekly_window[i][5]) == 1:
				arr_data_complete.append(info_data_Weekly_window[i])
	info_data_Weekly_window = info_data_copy
	arr_data_complete.reverse()
	for i in range(len(arr_data_complete)):
		info_data_Weekly_window.append(arr_data_complete[i])
	write_data()

	for i in range(7):
		Label(second_frame, text= "", width = 32, height= 0, background= color_background).grid(row= 0, column= i + 1, padx= 16)
	if get_max_tasks_on_day() < 6:
		for i in range(1, 8):
			Label(second_frame, text= "", width = 2, height= 6, background= color_background).grid(row= i, column= 0, pady= 26, padx= 12)
	else:
		for i in range(1, get_max_tasks_on_day() + 3):
			Label(second_frame, text= "", width = 2, height= 6, background= color_background).grid(row= i, column= 0, pady= 26, padx= 12)
	Label(second_frame, text= "", width = 2, height= 6, background= color_background).grid(row= 1, column= 8, pady= 26, padx= 12)

	if Settings.flag_for_windows == 2:
		for i in range(len(info_data_Weekly_window)):
			if int(info_data_Weekly_window[i][2]) == 0 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_monday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_monday, column=1)
			elif int(info_data_Weekly_window[i][2]) == 1 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_tuesday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_tuesday, column=2)
			elif int(info_data_Weekly_window[i][2]) == 2 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_wednesday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_wednesday, column=3)
			elif int(info_data_Weekly_window[i][2]) == 3 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_thursday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_thursday, column=4)
			elif int(info_data_Weekly_window[i][2]) == 4 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_friday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_friday, column=5)
			elif int(info_data_Weekly_window[i][2]) == 5 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_saturday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_saturday, column=6)
			elif int(info_data_Weekly_window[i][2]) == 6 and which_week_day(info_data_Weekly_window[i]) == 1:
				n_row_sunday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_sunday, column=7)
	elif Settings.flag_for_windows == 3:
		for i in range(len(info_data_Weekly_window)):
			if int(info_data_Weekly_window[i][2]) == 0 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_monday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_monday, column=1)
			elif int(info_data_Weekly_window[i][2]) == 1 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_tuesday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_tuesday, column=2)
			elif int(info_data_Weekly_window[i][2]) == 2 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_wednesday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_wednesday, column=3)
			elif int(info_data_Weekly_window[i][2]) == 3 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_thursday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_thursday, column=4)
			elif int(info_data_Weekly_window[i][2]) == 4 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_friday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_friday, column=5)
			elif int(info_data_Weekly_window[i][2]) == 5 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_saturday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_saturday, column=6)
			elif int(info_data_Weekly_window[i][2]) == 6 and which_week_day(info_data_Weekly_window[i]) == 2:
				n_row_sunday += 1
				Button(second_frame, text= set_enters(info_data_Weekly_window[i][6]) + get_deadline(info_data_Weekly_window[i]), font=("Arial", 12), width = 25, height= 6, state=state_or_normal(info_data_Weekly_window[i]), background=get_color_tasks(info_data_Weekly_window[i]), command=partial(delete_or_complete_task, info_data_Weekly_window[i])).grid(row=n_row_sunday, column=7)
	
	frame_bottom = Frame(main_window, bg=color_red)
	frame_bottom.place(x=0,y=930, height= 150, width= 1920)

	Label(frame_bottom, text="", bg= color_black).place(x=0, y=0, height=150, width= 1920)

	def bottom_button_get_state():
		if flag_for_last_day:
			return 'disabled'
		else:
			return 'normal'
		
	def go_to_main_window():
		Settings.flag_for_windows = 1
		main_window.destroy()
		
	def on_enter_for_Button_to_Main(e):
		if flag_for_last_day:
			pass
		else:
			Button_to_Main.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_to_Main(e):
		Button_to_Main.config(background= color_grey, foreground= color_black)
	Button_to_Main = Button(frame_bottom, text='Главная', state= bottom_button_get_state(), font=("Arial", 16), bg= color_grey, command= go_to_main_window)
	Button_to_Main.place(x=55, y= 25, height= 100, width= 235)
	Button_to_Main.bind('<Enter>', on_enter_for_Button_to_Main)
	Button_to_Main.bind('<Leave>', on_leave_for_Button_to_Main)

	def on_enter_for_Button_Add(e):
		if flag_for_last_day:
			pass
		else:
			Button_Add.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_Add(e):
		Button_Add.config(background= color_grey, foreground= color_black)
	Button_Add = Button(frame_bottom, text='Добавить задачу', state= bottom_button_get_state(), font=("Arial", 16), bg= color_grey, command= window_add_task)
	Button_Add.place(x=317, y= 25, height= 100, width= 235)
	Button_Add.bind('<Enter>', on_enter_for_Button_Add)
	Button_Add.bind('<Leave>', on_leave_for_Button_Add)

	def on_enter_for_Button_Add_everyday(e):
		if flag_for_last_day:
			pass
		else:
			Button_Add_everyday.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_Add_everyday(e):
		Button_Add_everyday.config(background= color_grey, foreground= color_black)
	Button_Add_everyday = Button(frame_bottom, text='Добавить ежедневку', state= bottom_button_get_state(), font=("Arial", 16), bg= color_grey, command= window_add_task_everyday)
	Button_Add_everyday.place(x=579, y= 25, height= 100, width= 235)
	Button_Add_everyday.bind('<Enter>', on_enter_for_Button_Add_everyday)
	Button_Add_everyday.bind('<Leave>', on_leave_for_Button_Add_everyday)

	def get_text_for_last_day():
		global flag_for_last_day

		if flag_for_last_day:
			return ["Обычный режим", "Arial 18 bold"]
		else:
			return ["Изменить\nпрошлый день", ("Arial", 16)]

	def on_enter_for_Button_Update_last_day(e):
		Button_Update_last_day.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_Update_last_day(e):
		Button_Update_last_day.config(background= color_grey, foreground= color_black)
	Button_Update_last_day = Button(frame_bottom, text= get_text_for_last_day()[0], font= get_text_for_last_day()[1], bg= color_grey, fg= color_black, command= lambda: update_last_day(main_window))
	Button_Update_last_day.place(x=841, y=25, height=100, width= 235)
	Button_Update_last_day.bind('<Enter>', on_enter_for_Button_Update_last_day)
	Button_Update_last_day.bind('<Leave>', on_leave_for_Button_Update_last_day)
		
	def go_to_window_week_1():
		if Settings.flag_for_windows == 2:
			pass
		else:
			Settings.where_flag_for_windows = 3
			Settings.flag_for_windows = 2
			main_window.destroy()

	def on_enter_for_Button_week_1(e):
		if flag_for_last_day:
			pass
		else:
			Button_week_1.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_week_1(e):
		Button_week_1.config(background= color_grey, foreground= color_black)
	Button_week_1 = Button(frame_bottom, text='1 неделя', font=("Arial", 16), state= bottom_button_get_state(), bg= color_grey, command= go_to_window_week_1)
	Button_week_1.place(x=1103, y= 25, height= 100, width= 235)
	Button_week_1.bind('<Enter>', on_enter_for_Button_week_1)
	Button_week_1.bind('<Leave>', on_leave_for_Button_week_1)

	def go_to_window_week_2():
		if Settings.flag_for_windows == 3:
			pass
		else:
			Settings.where_flag_for_windows = 2
			Settings.flag_for_windows = 3
			main_window.destroy()
		
	def on_enter_for_Button_week_2(e):
		if flag_for_last_day:
			pass
		else:
			Button_week_2.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_week_2(e):
		Button_week_2.config(background= color_grey, foreground= color_black)
	Button_week_2 = Button(frame_bottom, text='2 неделя', font=("Arial", 16), state= bottom_button_get_state(), bg= color_grey, command= go_to_window_week_2)
	Button_week_2.place(x=1365, y= 25, height= 100, width= 235)
	Button_week_2.bind('<Enter>', on_enter_for_Button_week_2)
	Button_week_2.bind('<Leave>', on_leave_for_Button_week_2)

	def on_enter_for_Button_close(e):
		Button_close.config(background= color_light_gray, foreground= color_black)
	def on_leave_for_Button_close(e):
		Button_close.config(background= color_grey, foreground= color_black)
	Button_close = Button(frame_bottom, text='Закрыть', font=("Arial", 16), bg= color_grey, command= Exit_from)
	Button_close.place(x=1627, y= 25, height= 100, width= 235)
	Button_close.bind('<Enter>', on_enter_for_Button_close)
	Button_close.bind('<Leave>', on_leave_for_Button_close)

	def _on_mousewheel(event: Event):
		my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
	my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
	my_canvas.bind_all("<MouseWheel>", _on_mousewheel)

	Label(main_window, text= "beta\n1.13", background= color_background, font=("Arial", 10)).place(x= 1870, y= 5)
	main_window.mainloop()
