class Notification:
    def get_notification(self):
        pass
class Instagram(Notification):

    def get_notification(self):
        print("Vainika has send a request")

class Facebook(Notification):

    def get_notification(self):
        print("Facebook notification")

ob=Instagram()
ob.get_notification()
ob1=Facebook()
ob1.get_notification()
