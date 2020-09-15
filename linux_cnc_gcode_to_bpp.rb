module BPP

class Header
  
  def to_s
    %{[HEADER]\nTYPE=BPP\nVER=150\n\n[DESCRIPTION]\n\n}
  end 
 
end

class Variables

  def initialize(x,y,z)
    @x=x.to_f.to_s
    @y=y.to_f.to_s
    @z=z.to_f.to_s
  end
  
  def to_s
%{[VARIABLES]
PAN=LPX|#{@x}||4|
PAN=LPY|#{@y}||4|
PAN=LPZ|#{@z}||4|
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
GLB=LX|LPX||0|
GLB=LY|LPY||0|\n\n}
  end  

end

class ProgramStart

  def initialize(x,y,z,d)
    @x=x.to_f.to_s
    @y=(-y.to_f).to_s
    @z=(-z.to_f).to_s
    @d=d.to_f.to_s
  end

  def to_s
%{[PROGRAM]
@ SHIFT, "", "", 374974684, "", 0 : LX/2, LY/2
@ ROUT, "", "", 95893420, "", 0 : "P1001", 0, "1", #{@d}, 0, "", 1, 1.6, -1, 0, 0, 32, 32, 50, 0, 45, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, "CARVING", 100, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 5, 0, 20, 80, 60, 0, "", "", "ROUT", 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 99, 0
  @ START_POINT, "", "", 95893036, "", 0 : #{@x}, #{@y}, 0
  @ LINE_EP, "", "", 95894956, "", 0 : #{@x}, #{@y}, 0, #{@z}, 0, 0, 0, 0, 0\n}
  end
end

class ProgramEnd
  
  def to_s
    %{  @ ENDPATH, "", "", 95894508, "", 0 :\n\n[VBSCRIPT]\n\n[MACRODATA]\n\n[TDCODES]\n\n[PCF]\n\n[TOOLING]\n\n[SUBPROGS]\n\n}
  end

end

class Movement
  attr_accessor :x, :y, :z

end 

class Converter

  def convert(filename:, lpx:, lpy:, lpz:, z0:)
    nmaxline=64000
    m = filename.match /(?<name>\w+)\.\w+/
    ofname = m[:name]
    arr = IO.readlines(filename)
    _num_file = 0
    _n_str = 0  
    _Xprev=0.0
    _Yprev=0.0
    _Zprev=0.0 
    _fname=ofname + ".bpp" 
    _file = File.new(_fname,"w")
    arr.each do |lin|
      if _n_str==0
        h = Header.new
        _file.syswrite h
        v = Variables.new lpx, lpy, lpz
        _file.syswrite v
        s = ProgramStart.new _Xprev, _Yprev, _Zprev, z0
         _file.syswrite s
      end
      _Xi=_Xprev
      _Yi=_Yprev
      _Zi=_Zprev
      smx = lin.match /.*X(?<x>(\+|-)?\d{,3}(\.\d{,3})?).*/
      smy = lin.match /.*Y(?<y>(\+|-)?\d{,3}(\.\d{,3})?).*/
      smz = lin.match /.*Z(?<z>(\+|-)?\d{,3}(\.\d{,3})?).*/
      _n_str+=1
      _Xi= smx[:x] if smx
      _Yi = smy[:y] if smy
      _Zi = smz[:z] if smz
      ostr='  @ LINE_EP, "", "", ' + + _n_str.to_s + ', "", 0 :' + _Xi.to_s + ",  " +(-1 * _Yi.to_f).to_s + ", 0, " + (_Zprev.to_f - _Zi.to_f).to_s + ", 0, 0, 0, 0, 0\n"
      _file.syswrite ostr
      _Xprev = _Xi
      _Yprev = _Yi
      _Zprev = _Zi
      if _n_str > nmaxline
        pe = ProgramEnd.new
        _file.syswrite pe
        _file.close
        _n_str=0
        _num_file+=1
        _fname=ofname + _num_file.to_s + ".bpp"
        _file = File.new(_fname,"w")
      end
    end
    pe = ProgramEnd.new
    _file.syswrite pe
    _file.close  
  end

end

end

c = BPP::Converter.new
lx = 570.0
lx = ARGV[1].to_f if ARGV.length >= 2
ly = 350.0 
ly = ARGV[2].to_f if ARGV.length >= 3
lz = 19.3
lz = ARGV[3].to_f if ARGV.length >= 4
z = 0.0
z = ARGV[4].to_f if ARGV.length >= 5
c.convert(filename: ARGV[0], lpx: lx, lpy: ly, lpz: lz, z0: z)