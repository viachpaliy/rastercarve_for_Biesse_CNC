from tkinter import *
from tkinter import filedialog, ttk
from tkinter.messagebox import askquestion, showerror
from PIL.ImageTk import PhotoImage
from PIL import Image, ImageTk, ImageFilter
from math import cos, pi, tan, sqrt, sin


class App:
   
    def __init__(self):
        self.filename =""
        self.lpx = 800.0
        self.lpy = 500.0
        self.lpz = 19.3
        self.lx = 800.0
        self.ly = 500.0
        self.toolname = "UGOL90"
        self.work_speed = 8000
        self.v_bit_angle = 90
        self.depth = 2.0
        self.prgname = "prog"
        self.maxlines = 100000
        self.stepover = 100
        self.strategy = 'angle45'
        self.lin_resol = 0.5
        self.root = Tk()
        root=self.root
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="Image", menu=filemenu)

        progmenu = Menu(menubar, tearoff=0)
        progmenu.add_command(label="Parameters", command=self.piece_dialog)
        progmenu.add_command(label="Create bpp files", command=self.create_files)
        menubar.add_cascade(label="Programme", menu=progmenu)
        self.use_blur = BooleanVar()
        self.param_panel=self.param_panel()
        self.param_panel.pack(side=LEFT)
        self.canvas = Canvas(root, width = 1200, height = 800)
        self.canvas.pack(fill=BOTH)
        root.config(menu=menubar)
        root.mainloop()

    def quit(self):
        sys.exit()
        self.root.quit()

    def open_file(self):
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.root.title(self.filename)
        load = Image.open(self.filename)
        img = ImageTk.PhotoImage(load)
        self.canvas.create_image(2, 2, anchor=NW, image = img)
        self.canvas.image = img

    def param_panel(self):
        filewin = Frame(self.root)
        lab = Label(filewin,text="Piece data :")
        lab.pack()
        rowx = Frame(filewin)
        labx = Label(rowx,width=10, text="LPX: ")
        entx= Entry(rowx)
        entx.insert(0, str(self.lpx))
        self.entx = entx
        rowx.pack(side=TOP, fill=X)
        labx.pack(side=LEFT)
        entx.pack(side=RIGHT, expand=YES, fill=X)
        rowy = Frame(filewin)
        laby = Label(rowy,width=10, text="LPY: ")
        enty= Entry(rowy)
        enty.insert(0,str(self.lpy))
        self.enty = enty
        rowy.pack(side=TOP, fill=X)
        laby.pack(side=LEFT)
        enty.pack(side=RIGHT, expand=YES, fill=X)
        rowz = Frame(filewin)
        labz = Label(rowz,width=10, text="LPZ: ")
        entz= Entry(rowz)
        entz.insert(0,str(self.lpz))
        self.entz = entz
        rowz.pack(side=TOP, fill=X)
        labz.pack(side=LEFT)
        entz.pack(side=RIGHT, expand=YES, fill=X)
        lab1 = Label(filewin,text = "Image data :")
        lab1.pack()
        rowlx = Frame(filewin)
        lablx = Label(rowlx,width=10, text="lenght: ")
        entlx= Entry(rowlx)
        entlx.insert(0, str(self.lx))
        self.entlx = entlx
        rowlx.pack(side=TOP, fill=X)
        lablx.pack(side=LEFT)
        entlx.pack(side=RIGHT, expand=YES, fill=X)
        rowly = Frame(filewin)
        lably = Label(rowly,width=10, text="height: ")
        ently= Entry(rowly)
        ently.insert(0, str(self.ly))
        self.ently = ently
        rowly.pack(side=TOP, fill=X)
        lably.pack(side=LEFT)
        ently.pack(side=RIGHT, expand=YES, fill=X)
        lab2 =Label(filewin,text = "Milling data :")
        lab2.pack()
        toolname_row = Frame(filewin)
        toolname_lab = Label(toolname_row,width=10, text="tool name : ")
        toolname_ent= Entry(toolname_row)
        toolname_ent.insert(0, self.toolname)
        self.toolname_ent = toolname_ent
        toolname_row.pack(side=TOP, fill=X)
        toolname_lab.pack(side=LEFT, expand=YES, fill=X)
        toolname_ent.pack(side=RIGHT, expand=YES, fill=X)
        work_speed_row = Frame(filewin)
        work_speed_lab = Label(work_speed_row,width=10, text="work speed : ")
        work_speed_ent= Entry(work_speed_row)
        work_speed_ent.insert(0, str(self.work_speed))
        self.work_speed_ent = work_speed_ent
        work_speed_row.pack(side=TOP, fill=X)
        work_speed_lab.pack(side=LEFT, expand=YES, fill=X)
        work_speed_ent.pack(side=RIGHT, expand=YES, fill=X)
        v_bit_angle_row = Frame(filewin)
        v_bit_angle_lab = Label(v_bit_angle_row,width=10, text="V-bit angle : ")
        v_bit_angle_ent= Entry(v_bit_angle_row)
        v_bit_angle_ent.insert(0, str(self.v_bit_angle))
        self.v_bit_angle_ent = v_bit_angle_ent
        v_bit_angle_row.pack(side=TOP, fill=X)
        v_bit_angle_lab.pack(side=LEFT, expand=YES, fill=X)
        v_bit_angle_ent.pack(side=RIGHT, expand=YES, fill=X)
        lin_resol_row = Frame(filewin)
        lin_resol_lab = Label(lin_resol_row,width=20, text="linear resolution : ")
        lin_resol_ent= Entry(lin_resol_row)
        lin_resol_ent.insert(0, str(self.lin_resol))
        self.lin_resol_ent = lin_resol_ent
        lin_resol_row.pack(side=TOP, fill=X)
        lin_resol_lab.pack(side=LEFT, expand=YES, fill=X)
        lin_resol_ent.pack(side=RIGHT, expand=YES, fill=X)
        use_blur_row = Frame(filewin)
        use_blur_cb = Checkbutton(use_blur_row, text = "use Gaussian blur filter", variable= self.use_blur)
        use_blur_row.pack(side=TOP, fill=X)
        use_blur_cb.pack(side=LEFT, expand=YES, fill=X)
        rowd = Frame(filewin)
        labd = Label(rowd,width=5, text="depth: ")
        entd= Entry(rowd)
        entd.insert(0, str(self.depth))
        self.entd = entd
        rowd.pack(side=TOP, fill=X)
        labd.pack(side=LEFT, expand=YES, fill=X)
        entd.pack(side=RIGHT, expand=YES, fill=X)
        rowst = Frame(filewin)
        labst = Label(rowst,width=10, text="stepover,%: ")
        entst= Entry(rowst)
        entst.insert(0, str(self.stepover))
        self.entst = entst
        rowst.pack(side=TOP, fill=X)
        labst.pack(side=LEFT,fill=X, expand=YES)
        entst.pack(side=RIGHT, expand=YES, fill=X)
        rowstrat = Frame(filewin)
        labstrat = Label(rowstrat,width=10, text="strategy : ")
        combostrat = ttk.Combobox(rowstrat,values=['angle45','circle','spiral'])
        combostrat.current(0)
        self.combostrat = combostrat
        rowstrat.pack(side=TOP, fill=X)
        labstrat.pack(side=LEFT,fill=X, expand=YES)
        combostrat.pack(side=RIGHT, expand=YES, fill=X)
        labp = Label(filewin, text = "Programme data :")
        labp.pack()
        rown = Frame(filewin)
        labn = Label(rown,width=10, text="name: ")
        entn= Entry(rown)
        entn.insert(0, self.prgname)
        self.entn = entn
        rown.pack(side=TOP, fill=X)
        labn.pack(side=LEFT)
        entn.pack(side=RIGHT, expand=YES, fill=X)
        rowml = Frame(filewin)
        labml = Label(rowml,width=12, text=" max num lines: ")
        entml= Entry(rowml)
        entml.insert(0, self.maxlines)
        self.entml = entml
        rowml.pack(side=TOP, fill=X)
        labml.pack(side=LEFT, expand=YES, fill=X )
        entml.pack(side=RIGHT, expand=YES, fill=X)
        button = Button(filewin, text="OK", command = self.set_param)
        button.pack()
        return filewin

    def set_param(self):
        self.lpx = float(self.entx.get())
        self.lpy = float(self.enty.get())
        self.lpz = float(self.entz.get())
        self.lx = float(self.entlx.get())
        self.ly = float(self.ently.get())
        self.depth = float(self.entd.get())
        self.prgname = self.entn.get()
        self.maxlines = int(self.entml.get())
        self.stepover = float(self.entst.get())
        self.toolname = self.toolname_ent.get()
        self.work_speed = float(self.work_speed_ent.get())
        self.v_bit_angle = float(self.v_bit_angle_ent.get())
        self.lin_resol =  float(self.lin_resol_ent.get())
        self.strategy = self.combostrat.get()

    def piece_dialog(self):
        filewin = Toplevel(self.root)
        lab = Label(filewin,text="Piece data :")
        lab.pack()
        rowx = Frame(filewin)
        labx = Label(rowx,width=5, text="LPX: ")
        entx= Entry(rowx)
        entx.insert(0, str(self.lpx))
        rowx.pack(side=TOP, fill=X)
        labx.pack(side=LEFT)
        entx.pack(side=RIGHT, expand=YES, fill=X)
        rowy = Frame(filewin)
        laby = Label(rowy,width=5, text="LPY: ")
        enty= Entry(rowy)
        enty.insert(0,str(self.lpy))
        rowy.pack(side=TOP, fill=X)
        laby.pack(side=LEFT)
        enty.pack(side=RIGHT, expand=YES, fill=X)
        rowz = Frame(filewin)
        labz = Label(rowz,width=5, text="LPZ: ")
        entz= Entry(rowz)
        entz.insert(0,str(self.lpz))
        rowz.pack(side=TOP, fill=X)
        labz.pack(side=LEFT)
        entz.pack(side=RIGHT, expand=YES, fill=X)
        lab1 = Label(filewin,text = "Image data :")
        lab1.pack()
        rowlx = Frame(filewin)
        lablx = Label(rowlx,width=5, text="lenght: ")
        entlx= Entry(rowlx)
        entlx.insert(0, str(self.lx))            
        rowlx.pack(side=TOP, fill=X)
        lablx.pack(side=LEFT)
        entlx.pack(side=RIGHT, expand=YES, fill=X)
        rowly = Frame(filewin)
        lably = Label(rowly,width=15, text="height: ")
        ently= Entry(rowly)
        ently.insert(0, str(self.ly))            
        rowly.pack(side=TOP, fill=X)
        lably.pack(side=LEFT)
        ently.pack(side=RIGHT, expand=YES, fill=X)
        lab2 =Label(filewin,text = "Milling data :")
        lab2.pack()
        rowd = Frame(filewin)
        labd = Label(rowd,width=5, text="Depth: ")
        entd= Entry(rowd)
        entd.insert(0, str(self.depth))            
        rowd.pack(side=TOP, fill=X)
        labd.pack(side=LEFT)
        entd.pack(side=RIGHT, expand=YES, fill=X)
        labp = Label(filewin, text = "Programme data :")
        labp.pack()
        rown = Frame(filewin)
        labn = Label(rown,width=5, text="name: ")
        entn= Entry(rown)
        entn.insert(0, self.prgname)            
        rown.pack(side=TOP, fill=X)
        labn.pack(side=LEFT)
        entn.pack(side=RIGHT, expand=YES, fill=X)
        rowml = Frame(filewin)
        labml = Label(rowml,width=5, text=" max num lines: ")
        entml= Entry(rowml)
        entml.insert(0, self.maxlines)            
        rowml.pack(side=TOP, fill=X)
        labml.pack(side=LEFT, expand=YES, fill=X )
        entml.pack(side=RIGHT, expand=YES, fill=X)
        button = Button(filewin, text="OK", command = filewin.destroy)
        button.pack()
            
    def header(self):
        return "[HEADER]\nTYPE=BPP\nVER=150\n\n[DESCRIPTION]\n\n"

    def variables(self):
        strin = """[VARIABLES]
PAN=LPX|{0:3.3f}||4|
PAN=LPY|{1:3.3f}||4|
PAN=LPZ|{2:3.3f}||4|
PAN=ORLST|"5"||3|
PAN=SIMMETRY|1||1|
PAN=TLCHK|0||1|
PAN=TOOLING|""||3|
PAN=CUSTSTR|$B$KBsExportToNcRvA.XncExtraPanelData$V""||3|
PAN=FCN|1.000000||2|
PAN=XCUT|0||4|
PAN=YCUT|0||4|
PAN=JIGTH|0||4|
PAN=CKOP|0||1|
PAN=UNIQUE|0||1|
PAN=MATERIAL|"wood"||3|
PAN=PUTLST|""||3|
PAN=OPPWKRS|0||1|
PAN=UNICLAMP|0||1|
PAN=CHKCOLL|0||1|
PAN=WTPIANI|0||1|
PAN=COLLTOOL|0||1|
PAN=CALCEDTH|0||1|
PAN=ENABLELABEL|0||1|
PAN=LOCKWASTE|0||1|
PAN=LOADEDGEOPT|0||1|
PAN=ITLTYPE|0||1|
PAN=RUNPAV|0||1|
PAN=FLIPEND|0||1|
PAN=ENABLEMACHLINKS|0||1|
PAN=ENABLEPURSUITS|0||1|
PAN=ENABLEFASTVERTBORINGS|0||1|
PAN=FASTVERTBORINGSVALUE|0||4|
\n""".format(self.lpx, self.lpy, self.lpz)
        return strin

    def programstart2(self):
        dx = (self.lpx - self.lx)/2
        dy = (self.lpy - self.ly)/2
        strin = """[PROGRAM]
    @ SHIFT, "", "", 374974684, "", 0 : {0:3.3f}, {1:3.3f}
    @ ROUT, "", "", 95893420, "", 0 : "P1001", 0, "1", 0, 0, "", 1, 1.6, -1, 0, 0, 32, 32, 50, 0, 45, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 8000, "UGOL90", 100, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 5, 0, 20, 80, 60, 0, "", "", "ROUT", 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 99, 0\n""".format(dx, dy)
        return strin

    def programstart(self):
        dx = (self.lpx - self.lx)/2
        dy = (self.lpy - self.ly)/2
        strin = '[PROGRAM]\n    @ SHIFT, "", "", 374974684, "", 0 : {0:3.3f}, {1:3.3f}\n'.format(dx, dy)
        strin = strin + '    @ ROUT, "", "", 95893420, "", 0 : "P1001", 0, "1", 0, 0, "", 1, 1.6, -1, 0, 0, 32, 32, 50, 0, 45, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0,'
        strin = strin + '{0:4.0f},"{1:s}", 100, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 5, 0, 20, 80, 60,'.format(self.work_speed,self.toolname)
        strin = strin + ', 0, "", "", "ROUT", 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 99, 0\n'
        return strin
    
    def startpoint(self,x, y):
        return "  @ START_POINT, "", "", 95893036, "", 0 : {0:3.3f}, {1:3.3f}, 0\n".format(x,y)

    def prog_end(self):
        return "  @ ENDPATH, "", "", 95894508, "", 0 :\n\n[VBSCRIPT]\n\n[MACRODATA]\n\n[TDCODES]\n\n[PCF]\n\n[TOOLING]\n\n[SUBPROGS]\n\n"

    def prog_line(self,x,y,z):
        return "  @ LINE_EP, "", "", 95894956, "", 0 : {0:3.3f}, {1:3.3f}, 0, {2:3.3f}, 0, 0, 0, 0, 0\n".format(x,y,z)

    def create_files(self):
        print('strategy : {}'.format(self.strategy))
        if self.strategy=='angle45':
            self.angle45_strategy()
        if self.strategy=='circle':
            self.circle_strategy()

    def circle_strategy(self):
        if self.filename=="":
            showerror('Error!',"Open a image")
            return
        prg = self.header()
        prg = prg + self.variables()
        prg = prg + self.programstart()
        print(prg)
        im=Image.open(self.filename)
        if self.use_blur.get():
            im=im.filter(ImageFilter.GaussianBlur(radius=2))
        depth = self.depth
        step = 2 * depth *tan(self.v_bit_angle * pi/360) * self.stepover / 100 
        n = int(sqrt(self.lx**2 +self.ly**2)/(2*step))
        ni = 0
        fi = 0
        out_f = self.prgname + ".bpp"
        for ki in range(1,n):
            ri = step * ki
            alfa_step = pi * self.lin_resol / ri
            alfa = 0
            zi = 0.0
            start_flag = True
            while alfa <= (2 * pi + alfa_step) :
                
                zo = zi
                xi = self.lx/2 + ri * cos(alfa)
                yi = self.ly/2 + ri * sin(alfa)
                if ((xi < self.lx) & (xi >0) & (yi < self.ly) & (yi > 0)):
                    if start_flag:
                        start_flag = False
                        zi = 0.0
                        prg = prg + self.startpoint(xi, yi)
                    i = int (round(xi * im.size[0] / self.lx))
                    j = int (round(yi * im.size[1] / self.ly))
                    if i<0:
                        i=0
                    if i>im.size[0]-1:
                        i=im.size[0]-1
                    if j<0:
                        j=0
                    if j>im.size[1]-1:
                        j=im.size[1]-1
                    gray = 0.299 * im.getpixel((i,j))[0] + 0.587 * im.getpixel((i,j))[1] + 0.114 * im.getpixel((i,j))[2]
                    gray = 256 - gray
                    zi = depth * gray /255
                    dz = zi - zo         
                    prg = prg + self.prog_line(xi, yi, dz)
                    print(self.prog_line(xi, yi, dz))
                    ni = ni +1
                else:
                    start_flag = True
                alfa += alfa_step
            if ni > self.maxlines :
                ni = 0
                prg = prg + self.prog_end()
                print(self.prog_end())
                fo = open(out_f, "w")
                fo.write(prg)
                fo.close()
                fi = fi + 1
                out_f = self.prgname + str(fi) +".bpp"
                prg = self.header()
                prg = prg + self.variables()
                prg = prg + self.programstart()
        prg = prg + self.prog_end()
        print(self.prog_end())
        fo = open(out_f, "w")
        fo.write(prg)
        fo.close()
        return prg
    
    def angle45_strategy(self):
        if self.filename=="":
            showerror('Error!',"Open a image")
            return
        prg = self.header()
        prg = prg + self.variables()
        prg = prg + self.programstart()
        print(prg)
        im=Image.open(self.filename)
        if self.use_blur.get():
            im=im.filter(ImageFilter.GaussianBlur(radius=2))
        depth = self.depth
        step = 2 * depth *tan(self.v_bit_angle * pi/360) * self.stepover / (100 * cos(pi/4) )
        step_xy = self.lin_resol * cos(pi/4)
        n = int((self.lx + self.ly)/step)
        ni = 0
        fi = 0
        out_f = self.prgname + ".bpp"
        for ki in range(1,n):
            xi =  step * ki
            yi = 0.0
            zi = 0.0
            if xi > self.lx :
                yi = xi - self.lx
                xi = self.lx
            prg = prg + self.startpoint(xi, yi)
            print(self.startpoint(xi, yi))
            while ((xi > 0.0) & (yi < self.ly)):
                zo = zi
                i = int (round(xi * im.size[0] / self.lx))
                j = int (round(yi * im.size[1] / self.ly))
                if i<0:
                    i=0
                if i>im.size[0]-1:
                    i=im.size[0]-1
                if j<0:
                    j=0
                if j>im.size[1]-1:
                    j=im.size[1]-1
                gray = 0.299 * im.getpixel((i,j))[0] + 0.587 * im.getpixel((i,j))[1] + 0.114 * im.getpixel((i,j))[2]
                gray = 256 - gray
                zi = depth * gray /255
                dz = zi - zo         
                prg = prg + self.prog_line(xi, yi, dz)
                print(self.prog_line(xi, yi, dz))
                ni = ni +1
                xi = xi - step_xy
                yi = yi + step_xy
            if ni > self.maxlines :
                ni = 0
                prg = prg + self.prog_end()
                print(self.prog_end())
                fo = open(out_f, "w")
                fo.write(prg)
                fo.close()
                fi = fi + 1
                out_f = self.prgname + str(fi) +".bpp"
                prg = self.header()
                prg = prg + self.variables()
                prg = prg + self.programstart()
        prg = prg + self.prog_end()
        print(self.prog_end())
        fo = open(out_f, "w")
        fo.write(prg)
        fo.close()
        return prg

if __name__ == '__main__' :
    app=App()
