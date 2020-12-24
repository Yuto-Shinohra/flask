import rumps
import tkinter
import subprocess
import sys


class main(rumps.App):
    @rumps.clicked("Test")
    def test(self,_):
        a()


def a():
    root = Tkinter.Tk()
    root.title(u"Software Title")
    root.geometry("400x300")
    root.mainloop()


if __name__=='__main__':
    launch=main("a")
    launch.run()
