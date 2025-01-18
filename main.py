import tkinter as tk
from tkinter import messagebox

def request_apology():
    # Показать сообщение с просьбой извиниться
    apology_label.pack()
    apology_entry.pack()
    submit_button.pack()

def check_apology():
    # Проверить введенное извинение
    if apology_entry.get().strip().lower() == "извини":
        messagebox.showinfo("Ответ", "Красава Дон")
    else:
        messagebox.showwarning("Ошибка", "Пожалуйста, напишите 'извини'.")

# Создаем главное окно
root = tk.Tk()
root.title("Программа извинений")

# Создаем элементы интерфейса
request_button = tk.Button(root, text="чотам", command=request_apology)
apology_label = tk.Label(root, text="Напишите извинение:")
apology_entry = tk.Entry(root)
submit_button = tk.Button(root, text="Отправить", command=check_apology)

# Размещаем кнопку на главном окне
request_button.pack(pady=20)

# Запускаем главный цикл
