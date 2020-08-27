from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import askquestion, showerror
from PIL.ImageTk import PhotoImage
from PIL import Image, ImageTk, ImageFilter
from math import cos, pi, tan


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
        self.lin_resol = 0.5
        self.vbscript = ""
        self.root = Tk()
        root=self.root
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Открыть", command=self.open_file)
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=self.quit)
        menubar.add_cascade(label="Изображение", menu=filemenu)

        progmenu = Menu(menubar, tearoff=0)
        progmenu.add_command(label="Создать bpp файл", command=self.create_files)
        menubar.add_cascade(label="Программа", menu=progmenu)
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
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Выбрать файл",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        if self.filename != "": 
            self.root.title(self.filename)
            load = Image.open(self.filename)
            img = ImageTk.PhotoImage(load)
            self.canvas.create_image(2, 2, anchor=NW, image = img)
            self.canvas.image = img

    def param_panel(self):
        filewin = Frame(self.root)
        lab = Label(filewin,text="Данные заготовки :")
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
        lab1 = Label(filewin,text = "Данные гравировки :")
        lab1.pack()
        rowlx = Frame(filewin)
        lablx = Label(rowlx,width=10, text="длина: ")
        entlx= Entry(rowlx)
        entlx.insert(0, str(self.lx))
        self.entlx = entlx
        rowlx.pack(side=TOP, fill=X)
        lablx.pack(side=LEFT)
        entlx.pack(side=RIGHT, expand=YES, fill=X)
        rowly = Frame(filewin)
        lably = Label(rowly,width=10, text="высота: ")
        ently= Entry(rowly)
        ently.insert(0, str(self.ly))
        self.ently = ently
        rowly.pack(side=TOP, fill=X)
        lably.pack(side=LEFT)
        ently.pack(side=RIGHT, expand=YES, fill=X)
        lab2 =Label(filewin,text = "Данные обработки :")
        lab2.pack()
        toolname_row = Frame(filewin)
        toolname_lab = Label(toolname_row,width=25, text="код инструмента : ")
        toolname_ent= Entry(toolname_row)
        toolname_ent.insert(0, self.toolname)
        self.toolname_ent = toolname_ent
        toolname_row.pack(side=TOP, fill=X)
        toolname_lab.pack(side=LEFT, expand=YES, fill=X)
        toolname_ent.pack(side=RIGHT, expand=YES, fill=X)
        work_speed_row = Frame(filewin)
        work_speed_lab = Label(work_speed_row,width=25, text="подача : ")
        work_speed_ent= Entry(work_speed_row)
        work_speed_ent.insert(0, str(self.work_speed))
        self.work_speed_ent = work_speed_ent
        work_speed_row.pack(side=TOP, fill=X)
        work_speed_lab.pack(side=LEFT, expand=YES, fill=X)
        work_speed_ent.pack(side=RIGHT, expand=YES, fill=X)
        v_bit_angle_row = Frame(filewin)
        v_bit_angle_lab = Label(v_bit_angle_row,width=25, text="V-угол фрезы : ")
        v_bit_angle_ent= Entry(v_bit_angle_row)
        v_bit_angle_ent.insert(0, str(self.v_bit_angle))
        self.v_bit_angle_ent = v_bit_angle_ent
        v_bit_angle_row.pack(side=TOP, fill=X)
        v_bit_angle_lab.pack(side=LEFT, expand=YES, fill=X)
        v_bit_angle_ent.pack(side=RIGHT, expand=YES, fill=X)
        lin_resol_row = Frame(filewin)
        lin_resol_lab = Label(lin_resol_row,width=25, text="шаг вдоль линии : ")
        lin_resol_ent= Entry(lin_resol_row)
        lin_resol_ent.insert(0, str(self.lin_resol))
        self.lin_resol_ent = lin_resol_ent
        lin_resol_row.pack(side=TOP, fill=X)
        lin_resol_lab.pack(side=LEFT, expand=YES, fill=X)
        lin_resol_ent.pack(side=RIGHT, expand=YES, fill=X)
        use_blur_row = Frame(filewin)
        use_blur_cb = Checkbutton(use_blur_row, text = "использовать фильтр Гаусса", variable= self.use_blur)
        use_blur_row.pack(side=TOP, fill=X)
        use_blur_cb.pack(side=LEFT, expand=YES, fill=X)
        rowd = Frame(filewin)
        labd = Label(rowd,width=5, text="глубина : ")
        entd= Entry(rowd)
        entd.insert(0, str(self.depth))
        self.entd = entd
        rowd.pack(side=TOP, fill=X)
        labd.pack(side=LEFT, expand=YES, fill=X)
        entd.pack(side=RIGHT, expand=YES, fill=X)
        rowst = Frame(filewin)
        labst = Label(rowst,width=25, text="увеличение шага,%: ")
        entst= Entry(rowst)
        entst.insert(0, str(self.stepover))
        self.entst = entst
        rowst.pack(side=TOP, fill=X)
        labst.pack(side=LEFT,fill=X, expand=YES)
        entst.pack(side=RIGHT, expand=YES, fill=X)
        labp = Label(filewin, text = "Данные программы :")
        labp.pack()
        rown = Frame(filewin)
        labn = Label(rown,width=10, text="имя : ")
        entn= Entry(rown)
        entn.insert(0, self.prgname)
        self.entn = entn
        rown.pack(side=TOP, fill=X)
        labn.pack(side=LEFT)
        entn.pack(side=RIGHT, expand=YES, fill=X)
        rowml = Frame(filewin)
        labml = Label(rowml,width=25, text=" max  число строк: ")
        entml= Entry(rowml)
        entml.insert(0, self.maxlines)
        self.entml = entml
        rowml.pack(side=TOP, fill=X)
        labml.pack(side=LEFT, expand=YES, fill=X )
        entml.pack(side=RIGHT, expand=YES, fill=X)
        button = Button(filewin, text="Применить", command = self.set_param)
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

    
            
    def header(self):
        return "[HEADER]\nTYPE=BPP\nVER=130\n\n[DESCRIPTION]\n\n"

    def variables(self):
        strin = """[VARIABLES]
PAN=LPX|{0:3.3f}||4|
PAN=LPY|{1:3.3f}||4|
PAN=LPZ|{2:3.3f}||4|
PAN=ORLST|"1"||0|
PAN=SIMMETRY|1||0|
PAN=TLCHK|0||0|
PAN=TOOLING|""||0|
PAN=CUSTSTR|""||0|
PAN=FCN|1.000000||0|
PAN=XCUT|0||4|
PAN=YCUT|0||4|
PAN=JIGTH|0||4|
PAN=CKOP|0||0|
PAN=UNIQUE|0||0|
PAN=MATERIAL|"wood"||0|
PAN=PUTLST|""||0|
PAN=OPPWKRS|0||0|
PAN=UNICLAMP|0||0|
PAN=CHKCOLL|0||0|
PAN=WTPIANI|0||0|
PAN=COLLTOOL|0||0|
PAN=CALCEDTH|0||0|
PAN=ENABLELABEL|0||0|
\n""".format(self.lpx, self.lpy, self.lpz)
        return strin

    def programstart(self):
        dx = (self.lpx - self.lx)/2
        dy = (self.lpy - self.ly)/2
        strin ='[PROGRAM]\n@ SHIFT, "", "", 249689336, "" : {0:3.3f}, {1:3.3f}\n'.format(dx, dy)
        strin = strin + '@ ROUT, "TDCODE1", "", 43308176, "" : "P1001", 0, "1", 0, 0, "", 1, 11, -1, 0, 0, 32, 32, 50, 0, 45, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0\n'
        return strin

    
    def startpoint(self,x, y):
        return "  @ START_POINT, "", "", 43303376, "" : {0:3.3f}, {1:3.3f}, 0\n".format(x,y)

    def vb_startpoint(self,x, y):
        return 'Call ProgBuilder.AddPoint(65, 43303376, ""    , ({0:3.3f})*FCN, ({1:3.3f})*FCN, (0)*FCN)\n'.format(x,y)

    def vbscript_start(self):
        dx = (self.lpx - self.lx)/2
        dy = (self.lpy - self.ly)/2
        strin = """[VBSCRIPT]
Option Explicit
Dim mm: mm = 1.000000000000000000
Dim inc: inc = 25.399999999999999000
Dim SIDE: SIDE = -1
Dim LPX: LPX = {0:3.3f}
Dim LPY: LPY = {1:3.3f}
Dim LPZ: LPZ = {2:3.3f}
Dim ORLST: ORLST = "1"
Dim SIMMETRY: SIMMETRY = 1
Dim TLCHK: TLCHK = 0
Dim TOOLING: TOOLING = ""
Dim CUSTSTR: CUSTSTR = ""
Dim FCN: FCN = 1.000000
Dim XCUT: XCUT = 0
Dim YCUT: YCUT = 0
Dim JIGTH: JIGTH = 0
Dim CKOP: CKOP = 0
Dim UNIQUE: UNIQUE = 0
Dim MATERIAL: MATERIAL = "wood"
Dim PUTLST: PUTLST = ""
Dim OPPWKRS: OPPWKRS = 0
Dim UNICLAMP: UNICLAMP = 0
Dim CHKCOLL: CHKCOLL = 0
Dim WTPIANI: WTPIANI = 0
Dim COLLTOOL: COLLTOOL = 0
Dim CALCEDTH: CALCEDTH = 0
Dim ENABLELABEL: ENABLELABEL = 0
Sub Main()Call ProgBuilder.SetPanel(LPX*FCN, LPY*FCN, LPZ*FCN, ORLST, SIMMETRY, TLCHK, TOOLING, CUSTSTR, \
FCN, XCUT*FCN, YCUT*FCN, JIGTH*FCN, CKOP, UNIQUE, MATERIAL, PUTLST, OPPWKRS, UNICLAMP, CHKCOLL, WTPIANI, COLLTOOL, CALCEDTH, ENABLELABEL)
Call ProgBuilder.AddShift(0, 249689336, ""    , ({3:3.3f})*FCN, ({4:3.3f})*FCN)
SIDE = 0: Call ProgBuilder.StartRout(0, 43308176, "TDCODE0"    , "P1001", 0, "1", (0)*FCN, (2)*FCN, "", YES, (11)*FCN, rpNO, (0)*FCN, \
(0)*FCN, (32)*FCN, (32)*FCN, (50)*FCN, 0, 45, YES, 0, 0, 0, (0)*FCN, (0)*FCN, azrNO, NO, NO, NO, 0, (0)*FCN, YES, NO, (0)*FCN, 0, NO, 0,\
(0)*FCN, 0, (0)*FCN, NO, (0)*FCN, YES, 0, -1, (0)*FCN)\n""".format(self.lpx, self.lpy, self.lpz,dx,dy)
        return strin

    def prog_end(self):
        strin ='  @ ENDPATH, "", "", 43307792, "" :\n\n' + self.vbscript_start()+self.vbscript+self.vb_end()
        strin = strin + '[MACRODATA]\n\n[TDCODES]\nVER=1\nCONVF=1.000000\nBUGFLAGS=3\n'
        strin = strin + '(MST)<LN=1,NJ=TDCODE1,TYW=2,NT=1,>\n(GEN)<WT=2,DL=0,>\n'
        strin = strin + '(TOO)<DI=11.0000,SP=11.0000,CL=1,COD={0},RO=-1,TY=100,ACT=0,NCT=,DCT=5.000000,TCT=0.000000,DICT=20.000000,DFCT=80.000000,PCT=60.000000,>\n'.format(self.toolname)
        strin = strin + '(IO)<AI=0.000,AO=0.000,DA=0.000,DT=0.000,DD=0.000,IFD=0.00,OFD=0.00,IN=0,OUT=0,PR=0,ETCI=0,ITI=0,TLI=0.00,THI=0.00,ETCO=0,ITO=0,TLO=0.00,THO=0.00,PDI=0.00,PDO=0.00,>\n'
        strin = strin + '(WRK)<OP=1,CO=0,HH=0.000,DR=0,PV=0,PT=0,TC=0,DP=5,SM=0,TT=0,RC=0,BD=0,SW=0,IC="",IM="",IA="",PC=0,BL=0,PU=0,EA=0,EEA=0,SP=0,AP=0,ESB=0,>\n'
        strin = strin + '(SPD)<AF=0.00,CF=0.000,DS=0.00,FE=8000,RT=0.00,OF=0.00,>\n'
        strin = strin + '(MOR)<PE=0.000000,TG=0.000000,TL=0.000000,WH=0.000000,>\n\n[PCF]\n\n[TOOLING]\n'
        return strin

    def vb_end(self):
        return 'Call ProgBuilder.EndPath(64, 43307792, ""    ): SIDE = -1\nEnd Sub\n\n'

    def prog_line(self,x,y,z):
        return "  @ LINC_EP, "", "", 43306064, "" : {0:3.3f}, {1:3.3f}, 0, {2:3.3f}, 0, 0, 0, 0\n".format(x,y,z)

    def vb_line(self,x,y,z):
        return 'Call ProgBuilder.AddLineIncEP(93, 43306064, ""    , ({0:3.3f})*FCN, ({1:3.3f})*FCN, (0)*FCN, ({2:3.3f})*FCN, scOFF, (0)*FCN, 0, 0)\n'.format(x,y,z)


    def create_files(self):
        if self.filename=="":
            showerror('Error!',"Open a image")
            return
        prg = self.header()
        prg = prg + self.variables()
        prg = prg + self.programstart()
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
            self.vbscript = self.vbscript + self.vb_startpoint(xi,yi)
            xo = xi
            yo = yi
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
                dx = xi - xo
                dy = yi - yo
                prg = prg + self.prog_line(dx, dy, dz)
                self.vbscript = self.vbscript + self.vb_line(dx, dy, dz)
                ni = ni + 2
                xo = xi
                yo = yi
                xi = xi - step_xy
                yi = yi + step_xy
            if ni > self.maxlines :
                ni = 0
                prg = prg + self.prog_end()
                fo = open(out_f, "w")
                fo.write(prg)
                fo.close()
                fi = fi + 1
                out_f = self.prgname + str(fi) +".bpp"
                prg = self.header()
                prg = prg + self.variables()
                prg = prg + self.programstart()
                self.vbscript = ""
        prg = prg + self.prog_end()
        fo = open(out_f, "w")
        fo.write(prg)
        fo.close()
        return prg

if __name__ == '__main__' :
    app=App()
