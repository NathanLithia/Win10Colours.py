import os
from tkinter import *
from tkinter import colorchooser

class setting():
    pass

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

ActiveBorder=Button(windows, text="     ", bg=f"#{setting.ActiveBorder.replace(' ', '')}", fg="red")
ActiveBorder.grid(column=1, row=0)
ActiveBorderlbl=Label(windows, text="ActiveBorder")
ActiveBorderlbl.grid(column=2, row=0)

ActiveTitle=Button(windows, text="     ", bg=f"#{setting.ActiveTitle.replace(' ', '')}", fg="red")
ActiveTitle.grid(column=1, row=1)
ActiveTitlelbl=Label(windows, text="ActiveTitle")
ActiveTitlelbl.grid(column=2, row=1)

AppWorkspace=Button(windows, text="     ", bg=f"#{setting.AppWorkspace.replace(' ', '')}", fg="red")
AppWorkspace.grid(column=1, row=2)
AppWorkspacelbl=Label(windows, text="AppWorkspace")
AppWorkspacelbl.grid(column=2, row=2)

Background=Button(windows, text="     ", bg=f"#{setting.Background.replace(' ', '')}", fg="red")
Background.grid(column=1, row=3)
Backgroundlbl=Label(windows, text="Background")
Backgroundlbl.grid(column=2, row=3)

ButtonAlternateFace=Button(windows, text="     ", bg=f"#{setting.ButtonAlternateFace.replace(' ', '')}", fg="red")
ButtonAlternateFace.grid(column=1, row=4)
ButtonAlternateFacelbl=Label(windows, text="ButtonAlternateFace")
ButtonAlternateFacelbl.grid(column=2, row=4)

ButtonDkShadow=Button(windows, text="     ", bg=f"#{setting.ButtonDkShadow.replace(' ', '')}", fg="red")
ButtonDkShadow.grid(column=1, row=5)
ButtonDkShadowlbl=Label(windows, text="ButtonDkShadow")
ButtonDkShadowlbl.grid(column=2, row=5)

ButtonFace=Button(windows, text="     ", bg=f"#{setting.ButtonFace.replace(' ', '')}", fg="red")
ButtonFace.grid(column=1, row=6)
ButtonFacelbl=Label(windows, text="ButtonFace")
ButtonFacelbl.grid(column=2, row=6)

ButtonHilight=Button(windows, text="     ", bg=f"#{setting.ButtonHilight.replace(' ', '')}", fg="red")
ButtonHilight.grid(column=1, row=7)
ButtonHilightlbl=Label(windows, text="ButtonHilight")
ButtonHilightlbl.grid(column=2, row=7)

ButtonLight=Button(windows, text="     ", bg=f"#{setting.ButtonLight.replace(' ', '')}", fg="red")
ButtonLight.grid(column=1, row=8)
ButtonLightlbl=Label(windows, text="ButtonLight")
ButtonLightlbl.grid(column=2, row=8)

ButtonShadow=Button(windows, text="     ", bg=f"#{setting.ButtonShadow.replace(' ', '')}", fg="red")
ButtonShadow.grid(column=1, row=9)
ButtonShadowlbl=Label(windows, text="ButtonShadow")
ButtonShadowlbl.grid(column=2, row=9)

ButtonText=Button(windows, text="     ", bg=f"#{setting.ButtonText.replace(' ', '')}", fg="red")
ButtonText.grid(column=1, row=10)
ButtonTextlbl=Label(windows, text="ButtonText")
ButtonTextlbl.grid(column=2, row=10)

GradientActiveTitle=Button(windows, text="     ", bg=f"#{setting.GradientActiveTitle.replace(' ', '')}", fg="red")
GradientActiveTitle.grid(column=1, row=11)
GradientActiveTitlelbl=Label(windows, text="GradientActiveTitle")
GradientActiveTitlelbl.grid(column=2, row=11)

GradientInactiveTitle=Button(windows, text="     ", bg=f"#{setting.GradientInactiveTitle.replace(' ', '')}", fg="red")
GradientInactiveTitle.grid(column=1, row=12)
GradientInactiveTitlelbl=Label(windows, text="GradientInactiveTitle")
GradientInactiveTitlelbl.grid(column=2, row=12)

GrayText=Button(windows, text="     ", bg=f"#{setting.GrayText.replace(' ', '')}", fg="red")
GrayText.grid(column=1, row=13)
GrayTextlbl=Label(windows, text="GrayText")
GrayTextlbl.grid(column=2, row=13)

Hilight=Button(windows, text="     ", bg=f"#{setting.Hilight.replace(' ', '')}", fg="red")
Hilight.grid(column=1, row=14)
Hilightlbl=Label(windows, text="Hilight")
Hilightlbl.grid(column=2, row=14)

HilightText=Button(windows, text="     ", bg=f"#{setting.HilightText.replace(' ', '')}", fg="red")
HilightText.grid(column=3, row=0)
HilightTextlbl=Label(windows, text="HilightText")
HilightTextlbl.grid(column=4, row=0)

HotTrackingColor=Button(windows, text="     ", bg=f"#{setting.HotTrackingColor.replace(' ', '')}", fg="red")
HotTrackingColor.grid(column=3, row=1)
HotTrackingColorlbl=Label(windows, text="HotTrackingColor")
HotTrackingColorlbl.grid(column=4, row=1)

InactiveBorder=Button(windows, text="     ", bg=f"#{setting.InactiveBorder.replace(' ', '')}", fg="red")
InactiveBorder.grid(column=3, row=2)
InactiveBorderlbl=Label(windows, text="InactiveBorder")
InactiveBorderlbl.grid(column=4, row=2)

InactiveTitle=Button(windows, text="     ", bg=f"#{setting.InactiveTitle.replace(' ', '')}", fg="red")
InactiveTitle.grid(column=3, row=3)
InactiveTitlelbl=Label(windows, text="InactiveTitle")
InactiveTitlelbl.grid(column=4, row=3)

InactiveTitleText=Button(windows, text="     ", bg=f"#{setting.InactiveTitleText.replace(' ', '')}", fg="red")
InactiveTitleText.grid(column=3, row=4)
InactiveTitleTextlbl=Label(windows, text="InactiveTitleText")
InactiveTitleTextlbl.grid(column=4, row=4)

InfoText=Button(windows, text="     ", bg=f"#{setting.InfoText.replace(' ', '')}", fg="red")
InfoText.grid(column=3, row=5)
InfoTextlbl=Label(windows, text="InfoText")
InfoTextlbl.grid(column=4, row=5)

Menu=Button(windows, text="     ", bg=f"#{setting.Menu.replace(' ', '')}", fg="red")
Menu.grid(column=3, row=6)
Menulbl=Label(windows, text="Menu")
Menulbl.grid(column=4, row=6)

MenuBar=Button(windows, text="     ", bg=f"#{setting.MenuBar.replace(' ', '')}", fg="red")
MenuBar.grid(column=3, row=7)
MenuBarlbl=Label(windows, text="MenuBar")
MenuBarlbl.grid(column=4, row=7)

MenuHilight=Button(windows, text="     ", bg=f"#{setting.MenuHilight.replace(' ', '')}", fg="red")
MenuHilight.grid(column=3, row=8)
MenuHilightlbl=Label(windows, text="MenuHilight")
MenuHilightlbl.grid(column=4, row=8)

MenuText=Button(windows, text="     ", bg=f"#{setting.MenuText.replace(' ', '')}", fg="red")
MenuText.grid(column=3, row=9)
MenuTextlbl=Label(windows, text="MenuText")
MenuTextlbl.grid(column=4, row=9)

Scrollbar=Button(windows, text="     ", bg=f"#{setting.Scrollbar.replace(' ', '')}", fg="red")
Scrollbar.grid(column=3, row=10)
Scrollbarlbl=Label(windows, text="Scrollbar")
Scrollbarlbl.grid(column=4, row=10)

TitleText=Button(windows, text="     ", bg=f"#{setting.TitleText.replace(' ', '')}", fg="red")
TitleText.grid(column=3, row=11)
TitleTextlbl=Label(windows, text="TitleText")
TitleTextlbl.grid(column=4, row=11)

Window=Button(windows, text="     ", bg=f"#{setting.Window.replace(' ', '')}", fg="red")
Window.grid(column=3, row=12)
Windowlbl=Label(windows, text="Window")
Windowlbl.grid(column=4, row=12)

WindowFrame=Button(windows, text="     ", bg=f"#{setting.WindowFrame.replace(' ', '')}", fg="red")
WindowFrame.grid(column=3, row=13)
lbl=Label(windows, text="WindowFrame")
lbl.grid(column=4, row=13)

WindowText=Button(windows, text="     ", bg=f"#{setting.WindowText.replace(' ', '')}", fg="red")
WindowText.grid(column=3, row=14)
lbl=Label(windows, text="WindowText")
lbl.grid(column=4, row=14)

Close=Button(windows, text="Close")
Close.grid(column=2, row=15)

Create=Button(windows, text="Create")
Create.grid(column=4, row=15)


print(setting.WindowText)
#windows.configure(background='black')
windows.mainloop()

def colorchoosers(inputs):
    clr = colorchooser.askcolor(title="Select color")
    print(clr)
    return clr