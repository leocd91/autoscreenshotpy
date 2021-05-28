import tkinter as tk
from PIL import ImageGrab, ImageTk, Image, ImageChops, ImageDraw, ImageFont, ImageStat
import os
import time
from datetime import date
import cv2
import ctypes 


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.attributes('-fullscreen', True)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both",expand=True)

        image = ImageGrab.grab(include_layered_windows=False, all_screens=False)
        image2 = image
        width, height = image.size
        
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 25)
        font2 = ImageFont.truetype("arial.ttf", 20)
        draw.text((width/3, height/2),"SELECT AREA TO SCREENSHOT",(255,0,0), font=font)
        draw.text((width/3+90, height/2+30),"(Area which will be saved)",(255,0,0), font=font2)

        self.image = ImageTk.PhotoImage(image)
        self.photo = self.canvas.create_image(0,0,image=self.image,anchor="nw")
        
        self.x, self.y = 0, 0
        self.rect, self.start_x, self.start_y = None, None, None

        self.x2, self.y2 = 0, 0
        self.rect2, self.start_x2, self.start_y2 = None, None, None

        self.deiconify()

        self.canvas.tag_bind(self.photo,"<ButtonPress-1>", self.on_button_press2)
        self.canvas.tag_bind(self.photo,"<B1-Motion>", self.on_move_press2)
        self.canvas.tag_bind(self.photo,"<ButtonRelease-1>", self.on_button_release2)
        self.deiconify()


    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='green')

    def on_button_press2(self, event):
        self.start_x2 = event.x
        self.start_y2 = event.y
        self.rect2 = self.canvas.create_rectangle(self.x2, self.y2, 1, 1, outline='red')

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_move_press2(self, event):
        curX2, curY2 = (event.x, event.y)
        self.canvas.coords(self.rect2, self.start_x2, self.start_y2, curX2, curY2)

    def on_button_release2(self, event):
        self.withdraw()
        image2 = ImageGrab.grab(include_layered_windows=False, all_screens=False)
        width, height = image2.size
        draw2 = ImageDraw.Draw(image2)
        font = ImageFont.truetype("arial.ttf", 25)
        font2 = ImageFont.truetype("arial.ttf", 20)
        draw2.text((width/3, height/2),"SELECT AREA TO FOCUS",(255,100,0), font=font)
        draw2.text((width/4+50, height/2+30),"(Area that if changes, will save the screenshot.)",(255,100,0), font=font2)
        draw2.text((width/4-20, height/2+60),"(Avoid selecting area that constantly changes, like presenter face-cam.)",(255,100,0), font=font2)
        
        self.image = ImageTk.PhotoImage(image2)
        self.photo = self.canvas.create_image(0,0,image=self.image,anchor="nw")
        self.canvas.tag_bind(self.photo,"<ButtonPress-1>", self.on_button_press)
        self.canvas.tag_bind(self.photo,"<B1-Motion>", self.on_move_press)
        self.canvas.tag_bind(self.photo,"<ButtonRelease-1>", self.on_button_release)
        self.deiconify()

    def on_button_release(self, event):
        helloCallBack(self)


def helloCallBack(self):
    ctypes.windll.user32.MessageBoxW(0, "Auto Screenshot starting! \nTo stop, just close the minimized terminal below.", "AutoScreenshotPy by leocd91", 0)
    bbox = self.canvas.bbox(self.rect2)
    bbox2 = self.canvas.bbox(self.rect)
    print('Recording started!')
    print('target:',bbox)
    print('focus:',bbox2)
    self.withdraw()
    self.old_image_f = ImageGrab.grab(bbox2)
    
    today = date.today()
    starttime = time.time()
    dirr = r'./screenshot'
    if not os.path.exists(dirr):
        os.mkdir('screenshot')
    print('detecting new slide..')
    i=0
    while True:
        fldrdir = dirr+r'/'+str(today).replace('-','_')    
        if not os.path.exists(fldrdir):
            os.mkdir(fldrdir)
        flname = fldrdir+r'/'+time.strftime("%Y%m%d%H%M%S")+'.png'
        self.new_image_f = ImageGrab.grab(bbox2)
        
        diff = ImageChops.difference(self.old_image_f, self.new_image_f)
        stat = ImageStat.Stat(diff)
        diff_ratio = ( sum(stat.mean) / (len(stat.mean) * 255) )*100
        
        if diff_ratio > 10.0:
            i=i+1
            print('found new slides! (',i,')')
            self.new_image = ImageGrab.grab(bbox)
            self.new_image.save(flname,"PNG")
            self.old_image_f = self.new_image_f 
            
        time.sleep(5 - time.time() % 5)
root = GUI()

root.mainloop()
