import tkinter as tk
import random

answer = random.randint(1, 10)

def check():
    user = int(entry.get())

    if user == answer:
        result.config(text="정답!")
    elif user > answer:
        result.config(text="너무 큼!")
    else:
        result.config(text="너무 작음!")

window = tk.Tk()
window.title("숫자게임")
window.geometry("300x200")

label = tk.Label(window, text="1~10 숫자 입력")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="확인", command=check)
button.pack()

result = tk.Label(window, text="")
result.pack()

window.mainloop()
