import npyscreen
import time

def myFunction(*args):
    F = npyscreen.Form(name='My Test Application')
    F.add(npyscreen.TitleText, name="First Widget")
    F.edit()

if __name__ == '__main__':
    npyscreen.wrapper_basic(myFunction)
