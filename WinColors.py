import os
from tkinter import *
from tkinter import colorchooser

class setting():
    pass

def colorchoosers(defaultcolor):
    clr = colorchooser.askcolor(title="Select color")
    if clr == (None, None):
        print(f"{defaultcolor} -> {defaultcolor}")
        return defaultcolor
    print(f"{defaultcolor} -> {clr}")
    return clr

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   

setting.ActiveBorder="180 180 180"
setting.ActiveTitle="153 180 209"
setting.AppWorkspace="171 171 171"
setting.Background="0 0 0"
setting.ButtonAlternateFace="0 0 0"
setting.ButtonDkShadow="105 105 105"
setting.ButtonFace="240 240 240"
setting.ButtonHilight="255 255 255"
setting.ButtonLight="227 227 227"
setting.ButtonShadow="160 160 160"
setting.ButtonText="0 0 0"
setting.GradientActiveTitle="185 209 234"
setting.GradientInactiveTitle="215 228 242"
setting.GrayText="109 109 109"
setting.Hilight="051 153 255"
setting.HilightText="255 255 255"
setting.HotTrackingColor="000 102 204"
setting.InactiveBorder="244 247 252"
setting.InactiveTitle="191 205 219"
setting.InactiveTitleText="0 0 0"
setting.InfoText="0 0 0"
setting.InfoWindow="255 255 225"
setting.Menu="240 240 240"
setting.MenuBar="240 240 240"
setting.MenuHilight="051 153 255"
setting.MenuText="0 0 0"
setting.Scrollbar="200 200 200"
setting.TitleText="0 0 0"
setting.Window="255 255 255"
setting.WindowFrame="100 100 100"
setting.WindowText="0 0 0"

windows = Tk()
    
windows.title("WIN10 COLOR")
windows.geometry('270x420')

def ActiveBorderdef():
    ActiveBorder['bg'] = setting.ActiveBorder = colorchoosers(setting.ActiveBorder)
ActiveBorder=Button(windows, text="     ", bg=f"#{setting.ActiveBorder.replace(' ', '')}", command = ActiveBorderdef)
ActiveBorder.grid(column=1, row=0)
ActiveBorderlbl=Label(windows, text="ActiveBorder")
ActiveBorderlbl.grid(column=2, row=0)

def ActiveTitledef():
    ActiveTitle['bg'] = setting.ActiveTitle = colorchoosers(setting.ActiveTitle)
ActiveTitle=Button(windows, text="     ", bg=f"#{setting.ActiveTitle.replace(' ', '')}", command = ActiveTitledef)
ActiveTitle.grid(column=1, row=1)
ActiveTitlelbl=Label(windows, text="ActiveTitle")
ActiveTitlelbl.grid(column=2, row=1)

def AppWorkspacedef():
    AppWorkspace['bg'] = setting.AppWorkspace = colorchoosers(setting.AppWorkspace)
AppWorkspace=Button(windows, text="     ", bg=f"#{setting.AppWorkspace.replace(' ', '')}", command = AppWorkspacedef)
AppWorkspace.grid(column=1, row=2)
AppWorkspacelbl=Label(windows, text="AppWorkspace")
AppWorkspacelbl.grid(column=2, row=2)

def Backgrounddef():
    Background['bg'] = setting.Background = colorchoosers(setting.Background)
Background=Button(windows, text="     ", bg=f"#{setting.Background.replace(' ', '')}", command = Backgrounddef)
Background.grid(column=1, row=3)
Backgroundlbl=Label(windows, text="Background")
Backgroundlbl.grid(column=2, row=3)

def ButtonAlternateFacedef():
    ButtonAlternateFace['bg'] = setting.ButtonAlternateFace = colorchoosers(setting.ButtonAlternateFace)
ButtonAlternateFace=Button(windows, text="     ", bg=f"#{setting.ButtonAlternateFace.replace(' ', '')}", command = ButtonAlternateFacedef)
ButtonAlternateFace.grid(column=1, row=4)
ButtonAlternateFacelbl=Label(windows, text="ButtonAlternateFace")
ButtonAlternateFacelbl.grid(column=2, row=4)

def ButtonDkShadowdef():
    ButtonDkShadow['bg'] = setting.ButtonDkShadow = colorchoosers(setting.ButtonDkShadow)
ButtonDkShadow=Button(windows, text="     ", bg=f"#{setting.ButtonDkShadow.replace(' ', '')}", command = ButtonDkShadowdef)
ButtonDkShadow.grid(column=1, row=5)
ButtonDkShadowlbl=Label(windows, text="ButtonDkShadow")
ButtonDkShadowlbl.grid(column=2, row=5)

def ButtonFacedef():
    ButtonFace['bg'] = setting.ButtonFace = colorchoosers(setting.ButtonFace)
ButtonFace=Button(windows, text="     ", bg=f"#{setting.ButtonFace.replace(' ', '')}", command = ButtonFacedef)
ButtonFace.grid(column=1, row=6)
ButtonFacelbl=Label(windows, text="ButtonFace")
ButtonFacelbl.grid(column=2, row=6)

def ButtonHilightdef():
    ButtonHilight['bg'] = setting.ButtonHilight = colorchoosers(setting.ButtonHilight)
ButtonHilight=Button(windows, text="     ", bg=f"#{setting.ButtonHilight.replace(' ', '')}", command = ButtonHilightdef)
ButtonHilight.grid(column=1, row=7)
ButtonHilightlbl=Label(windows, text="ButtonHilight")
ButtonHilightlbl.grid(column=2, row=7)

def ButtonLightdef():
    ButtonLight['bg'] = setting.ButtonLight = colorchoosers(setting.ButtonLight)
ButtonLight=Button(windows, text="     ", bg=f"#{setting.ButtonLight.replace(' ', '')}", command = ButtonLightdef)
ButtonLight.grid(column=1, row=8)
ButtonLightlbl=Label(windows, text="ButtonLight")
ButtonLightlbl.grid(column=2, row=8)

def ButtonShadowdef():
    ButtonShadow['bg'] = setting.ButtonShadow = colorchoosers(setting.ButtonShadow)
ButtonShadow=Button(windows, text="     ", bg=f"#{setting.ButtonShadow.replace(' ', '')}", command = ButtonShadowdef)
ButtonShadow.grid(column=1, row=9)
ButtonShadowlbl=Label(windows, text="ButtonShadow")
ButtonShadowlbl.grid(column=2, row=9)

def ButtonTextdef():
    ButtonText['bg'] = setting.ButtonText = colorchoosers(setting.ButtonText)
ButtonText=Button(windows, text="     ", bg=f"#{setting.ButtonText.replace(' ', '')}", command = ButtonTextdef)
ButtonText.grid(column=1, row=10)
ButtonTextlbl=Label(windows, text="ButtonText")
ButtonTextlbl.grid(column=2, row=10)

def GradientActiveTitledef():
    GradientActiveTitle['bg'] = setting.GradientActiveTitle = colorchoosers(setting.GradientActiveTitle)
GradientActiveTitle=Button(windows, text="     ", bg=f"#{setting.GradientActiveTitle.replace(' ', '')}", command = GradientActiveTitledef)
GradientActiveTitle.grid(column=1, row=11)
GradientActiveTitlelbl=Label(windows, text="GradientActiveTitle")
GradientActiveTitlelbl.grid(column=2, row=11)

def GradientInactiveTitledef():
    GradientInactiveTitle['bg'] = setting.GradientInactiveTitle = colorchoosers(setting.GradientInactiveTitle)
GradientInactiveTitle=Button(windows, text="     ", bg=f"#{setting.GradientInactiveTitle.replace(' ', '')}", command = GradientInactiveTitledef)
GradientInactiveTitle.grid(column=1, row=12)
GradientInactiveTitlelbl=Label(windows, text="GradientInactiveTitle")
GradientInactiveTitlelbl.grid(column=2, row=12)

def GrayTextdef():
    GrayText['bg'] = setting.GrayText = colorchoosers(setting.GrayText)
GrayText=Button(windows, text="     ", bg=f"#{setting.GrayText.replace(' ', '')}", command = GrayTextdef)
GrayText.grid(column=1, row=13)
GrayTextlbl=Label(windows, text="GrayText")
GrayTextlbl.grid(column=2, row=13)

def Hilightdef():
    Hilight['bg'] = setting.Hilight = colorchoosers(setting.Hilight)
Hilight=Button(windows, text="     ", bg=f"#{setting.Hilight.replace(' ', '')}", command = Hilightdef)
Hilight.grid(column=1, row=14)
Hilightlbl=Label(windows, text="Hilight")
Hilightlbl.grid(column=2, row=14)

def HilightTextdef():
    HilightText['bg'] = setting.HilightText = colorchoosers(setting.HilightText)
HilightText=Button(windows, text="     ", bg=f"#{setting.HilightText.replace(' ', '')}", command = HilightTextdef)
HilightText.grid(column=3, row=0)
HilightTextlbl=Label(windows, text="HilightText")
HilightTextlbl.grid(column=4, row=0)

def HotTrackingColordef():
    HotTrackingColor['bg'] = setting.HotTrackingColor = colorchoosers(setting.HotTrackingColor)
HotTrackingColor=Button(windows, text="     ", bg=f"#{setting.HotTrackingColor.replace(' ', '')}", command = HotTrackingColordef)
HotTrackingColor.grid(column=3, row=1)
HotTrackingColorlbl=Label(windows, text="HotTrackingColor")
HotTrackingColorlbl.grid(column=4, row=1)

def InactiveBorderdef():
    InactiveBorder['bg'] = setting.InactiveBorder = colorchoosers(setting.InactiveBorder)
InactiveBorder=Button(windows, text="     ", bg=f"#{setting.InactiveBorder.replace(' ', '')}", command = InactiveBorderdef)
InactiveBorder.grid(column=3, row=2)
InactiveBorderlbl=Label(windows, text="InactiveBorder")
InactiveBorderlbl.grid(column=4, row=2)

def InactiveTitledef():
    InactiveTitle['bg'] = setting.InactiveTitle = colorchoosers(setting.InactiveTitle)
InactiveTitle=Button(windows, text="     ", bg=f"#{setting.InactiveTitle.replace(' ', '')}", command = InactiveTitledef)
InactiveTitle.grid(column=3, row=3)
InactiveTitlelbl=Label(windows, text="InactiveTitle")
InactiveTitlelbl.grid(column=4, row=3)

def InactiveTitleTextdef():
    InactiveTitleText['bg'] = setting.InactiveTitleText = colorchoosers(setting.InactiveTitleText)
InactiveTitleText=Button(windows, text="     ", bg=f"#{setting.InactiveTitleText.replace(' ', '')}", command = InactiveTitleTextdef)
InactiveTitleText.grid(column=3, row=4)
InactiveTitleTextlbl=Label(windows, text="InactiveTitleText")
InactiveTitleTextlbl.grid(column=4, row=4)

def InfoTextdef():
    InfoText['bg'] = setting.InfoText = colorchoosers(setting.InfoText)
InfoText=Button(windows, text="     ", bg=f"#{setting.InfoText.replace(' ', '')}", command = InfoTextdef)
InfoText.grid(column=3, row=5)
InfoTextlbl=Label(windows, text="InfoText")
InfoTextlbl.grid(column=4, row=5)

def Buttondef():
    Menu['bg'] = setting.Button = colorchoosers(setting.Button)
Menu=Button(windows, text="     ", bg=f"#{setting.Menu.replace(' ', '')}", command = Buttondef)
Menu.grid(column=3, row=6)
Menulbl=Label(windows, text="Menu")
Menulbl.grid(column=4, row=6)

def MenuBardef():
    MenuBar['bg'] = setting.MenuBar = colorchoosers(setting.MenuBar)
MenuBar=Button(windows, text="     ", bg=f"#{setting.MenuBar.replace(' ', '')}", command = MenuBardef)
MenuBar.grid(column=3, row=7)
MenuBarlbl=Label(windows, text="MenuBar")
MenuBarlbl.grid(column=4, row=7)

def MenuHilightdef():
    MenuHilight['bg'] = setting.MenuHilight = colorchoosers(setting.MenuHilight)
MenuHilight=Button(windows, text="     ", bg=f"#{setting.MenuHilight.replace(' ', '')}", command = MenuHilightdef)
MenuHilight.grid(column=3, row=8)
MenuHilightlbl=Label(windows, text="MenuHilight")
MenuHilightlbl.grid(column=4, row=8)

def MenuTextdef():
    MenuText['bg'] = setting.MenuText = colorchoosers(setting.MenuText)
MenuText=Button(windows, text="     ", bg=f"#{setting.MenuText.replace(' ', '')}", command = MenuTextdef)
MenuText.grid(column=3, row=9)
MenuTextlbl=Label(windows, text="MenuText")
MenuTextlbl.grid(column=4, row=9)

def Scrollbardef():
    Scrollbar['bg'] = setting.Scrollbar = colorchoosers(setting.Scrollbar)
Scrollbar=Button(windows, text="     ", bg=f"#{setting.Scrollbar.replace(' ', '')}", command = Scrollbardef)
Scrollbar.grid(column=3, row=10)
Scrollbarlbl=Label(windows, text="Scrollbar")
Scrollbarlbl.grid(column=4, row=10)

def TitleTextdef():
    TitleText['bg'] = setting.TitleText = colorchoosers(setting.TitleText)
TitleText=Button(windows, text="     ", bg=f"#{setting.TitleText.replace(' ', '')}", command = TitleTextdef)
TitleText.grid(column=3, row=11)
TitleTextlbl=Label(windows, text="TitleText")
TitleTextlbl.grid(column=4, row=11)

def Windowdef():
    Window['bg'] = setting.Window = colorchoosers(setting.Window)
Window=Button(windows, text="     ", bg=f"#{setting.Window.replace(' ', '')}", command = Windowdef)
Window.grid(column=3, row=12)
Windowlbl=Label(windows, text="Window")
Windowlbl.grid(column=4, row=12)

def WindowFramedef():
    WindowFrame['bg'] = setting.WindowFrame = colorchoosers(setting.WindowFrame)
WindowFrame=Button(windows, text="     ", bg=f"#{setting.WindowFrame.replace(' ', '')}", command = WindowFramedef)
WindowFrame.grid(column=3, row=13)
lbl=Label(windows, text="WindowFrame")
lbl.grid(column=4, row=13)

def WindowTextdef():
    WindowText['bg'] = setting.WindowText = colorchoosers(setting.WindowText)
WindowText=Button(windows, text="     ", bg=f"#{setting.WindowText.replace(' ', '')}", command = WindowTextdef)
WindowText.grid(column=3, row=14)
lbl=Label(windows, text="WindowText")
lbl.grid(column=4, row=14)

def Closedef():
    exit()
Close=Button(windows, text="Close", command = Closedef)
Close.grid(column=2, row=15)

Create=Button(windows, text="Create")
Create.grid(column=4, row=15)


print(setting.WindowText)
#windows.configure(background='black')
windows.mainloop()

