class  mobile:
    def __init__(self):
        pass

    def call(self):
        print('Invoking call function')

    def sms(self):
        print('Invoking sms method')

    def games(self):
        print('Invoking game method')

class Realme(mobile):
    def cam(self):
        print("invoking cam method")

    def music(self):
        print("invoking music method")

    def video_call(self):
        print("invoking video call method")

real=Realme()
real.call()
real.music()