import tkinter as tk

#============觸發事件==============
#處理事件
def echo_hello():
    print('hello')

#============視窗==============
#生成GUI
window = tk.Tk()
#建立區塊
top_frame = tk.Frame(window)
#佈署區塊
top_frame.pack()

#建立按鈕區塊
bottom_frame = tk.Frame(window)
#佈署按鈕區塊
bottom_frame.pack(side=tk.BOTTOM)

#============按鈕==============
#在top_frame建立按鈕區塊
left_button = tk.Button(top_frame, text="Red",fg='red')
#佈署按鈕
left_button.pack(side=tk.LEFT)

#在top_frame建立按鈕區塊
middle_button = tk.Button(top_frame, text="Green",fg='green')
#佈署按鈕
middle_button.pack(side=tk.LEFT)

#在top_frame建立按鈕區塊
right_button = tk.Button(top_frame, text="Blue",fg='blue')
#佈署按鈕
right_button.pack(side=tk.LEFT)

#在top_frame建立按鈕區塊 使用方法內的指令
bottom_button = tk.Button(bottom_frame, text='Black', fg='black', command=echo_hello)
#佈署按鈕
bottom_button.pack(side=tk.BOTTOM)

#迴圈執行視窗
window.mainloop()