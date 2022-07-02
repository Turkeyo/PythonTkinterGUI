from cgitb import text
from email import header
from itertools import count
import tkinter as tk
import math
#============觸發事件==============
#處理事件
def countBMI():
    #取得輸入區塊的數字
    height = float(height_type.get())
    weight = float(weight_type.get())
    bmi_value = round(weight / math.pow(height, 2), 2)
    result = 'Your BMI Is: {} {}'.format(bmi_value,result_yourbody(bmi_value))
    showBMI.configure(text=result)
def result_yourbody(bmi_value):
    if bmi_value < 18.5:
        return '體重過輕'
    elif bmi_value >= 18.5:
        return '體重適中'
    elif bmi_value >= 24:
        return '體重過重'
#============視窗==============
#生成GUI
window = tk.Tk()
#設定GUI標題
window.title('BMI App')
#設定視窗大小
window.geometry('800x600')
#設定視窗背景      設定背景顏色:白
window.configure(background='white')

#在window建立一個表格  w在window視窗建立 內容字:BMI 計算機
header_label = tk.Label(window, text='BMI 計算機')
#佈署表格
header_label.pack()


#=======height輸入區塊=======
#在window建立區塊
height_frame = tk.Frame(window)
#佈署區塊
height_frame.pack()

#在height_frame內建立表格
height_label = tk.Label(height_frame,text='身高(m)')
#佈署表格           放置在左側
height_label.pack(side=tk.LEFT)

#在height_frame內建立可輸入的表格
height_type = tk.Entry(height_frame)
#佈署表格
height_type.pack()

#=======weight輸入區塊=======
#在window建立區塊
weight_frame = tk.Frame(window)
#佈署區塊
weight_frame.pack()

#在weight_frame內建立表格
weight_label = tk.Label(weight_frame,text='體重(kg)')
#佈署表格
weight_label.pack(side=tk.LEFT)

#在weight_frame內建立可輸入表格
weight_type = tk.Entry(weight_frame)
#佈署表格
weight_type.pack()

#在window建立表格
showBMI = tk.Label(window)
#佈署表格
showBMI.pack()

#=======計算按鈕=======
#在window建立按鈕
window_buttom = tk.Button(window,text="計算BMI",command=countBMI)
#佈署按鈕
window_buttom.pack()
#迴圈執行視窗
window.mainloop()


