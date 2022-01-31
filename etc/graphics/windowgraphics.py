from cgitb import text
from multiprocessing.sharedctypes import Value
import tkinter
import tkinter.ttk
import etc.stringManager
import json
import sys
languageclass = etc.stringManager.stringman("en")
lanman = lambda stringcaller: languageclass.get(stringcaller)
global images
images = {
            "running": "etc/graphics/gfx/running.png",
            "alarm": "etc/graphics/gfx/alarm.png",
            "off": "etc/graphics/gfx/off.png",
            "sleeping": "etc/graphics/gfx/sleeping.png",
            "splash": "etc/graphics/gfx/splash.png"
        }
class window:
    global images
    def __init__(self):
        self.window = tkinter.Tk()
        self.returnitem = None
        self.looping = True
        self.engine = []
        self.c, self.r = 0,0
    def clearwidgets(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.update()
        self.window.update_idletasks()
    def profile_selector(self):
        """
        in a combobox list all profiles
        add a button named start
        return the profile name
        """
        self.clearwidgets()
        self.window.title(lanman("profile_selector"))
        self.window.geometry("300x300")
        self.window.resizable(False, False)
        self.window.configure(background="white")
        comboboxitems=[]
        try:
            with open ("etc/settings.json", "r+") as f:
                try:
                    settings=json.load(f)
                except Exception as e:
                    print("An error occured while loading settings.json", e)
                    settings = {}
                    
        except:
            print("settings.json dosyası bulunamadı. ayarlar açılıyor.")
            settings = {}
        for item in settings.keys():
            comboboxitems.append(settings[item]["profile_name"])
        if settings == {}:
            tkinter.Label(self.window, text=lanman("settings_empty")).pack()
        else:
            self.combobox = tkinter.ttk.Combobox(self.window, values=comboboxitems)
            self.combobox.pack()
            self.combobox.current(0)
            self.combobox.bind("<<ComboboxSelected>>", self.profile_selected)
            self.startbutton = tkinter.Button(self.window, text=lanman("start"), command=self.start)
            self.startbutton.pack()
            self.settingsbutton = tkinter.Button(self.window, text=lanman("settings"), command=self.settings)
            self.settingsbutton.pack()
        while self.looping:
            self.window.update()
            self.window.update_idletasks()
    def settings(self):
        pass
    def profile_selected(self, event):
        print(self.combobox.get())
    def start(self):
        self.returnitem = self.combobox.get()
        self.looping = False
    def runningwindow(self, profile):
        self.window.title(lanman("running_window"))
        self.window.geometry("300x300")
        self.window.resizable(False, False)
        self.window.configure(background="white")
        self.clearwidgets()
        tkinter.Label(self.window, text=lanman("profile_selected")+" : "+profile["profile_name"]).grid(row=self.r, column=0)
        self.r+=1
        """
        add a console that will show the stdout
        on the bottom of the window
        in a black box
        """
        bottomframe = tkinter.Frame(self.window)
        bottomframe.config(background="black")
        bottomframe.config(height=100, width=100)
        bottomframe.grid(row=30, column=0, columnspan=4)
        bottomframe.grid_propagate(False)
        bottomframe.grid_rowconfigure(0, weight=1)
        bottomframe.grid_columnconfigure(0, weight=1)
        self.consoleoutput = ""
        self.console = tkinter.Text(bottomframe, height=10, width=100, state="disabled", bg="black", fg="white", font="Arial 10")
        self.console.grid(row=0, column=0, sticky="nsew")
    def returnlast(self):
        returnitem = self.returnitem
        self.returnitem = None
        return returnitem
    def update(self):
        self.window.update()
        self.window.update_idletasks()
        self.console.insert(tkinter.END, self.consoleoutput)
    def register_engine(self, engine, status = "off"):
        self.engine.append([engine,
            status, # status
            False, # is it drawed?
            None, # label
            None, # image
            None, # buttons
        ])
        self.draw_engine_status()
    def engine_update(self, engine, status):
        self.engine[engine][1] = status
    def engine_status(self, engine):
        return self.engine[engine][1]
    def engine_status_all(self):
        return self.engine
    def draw_engine_status(self):
        for engine in self.engine:
            if engine[2] == False:
                label = tkinter.Label(self.window, text=engine[0].name)
                label.grid(row=self.r, column=0)
                photo = tkinter.PhotoImage(file=images[engine[1]])
                image = tkinter.Label(self.window, image=photo)
                image.image = photo
                image.grid(row=self.r, column=1)
                startbutton = tkinter.Button(self.window, text=lanman("start"), command=lambda **x: self.startmodule(engine[0]))
                stopbutton = tkinter.Button(self.window, text=lanman("stop"), command=lambda **x: self.stopmodule(engine[0]))
                startbutton.grid(row=self.r, column=2)
                stopbutton.grid(row=self.r, column=3)
                self.r+=1
                engine[2] = True
    
if __name__ == "__main__":
    exit()