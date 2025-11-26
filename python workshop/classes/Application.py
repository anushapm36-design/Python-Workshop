class Application:
    def __init__(self,application_name,category,company,app_size,no_of_users,ratings):
        self.application_name=application_name
        self.category=category
        self.company=company
        self.app_size=app_size
        self.no_of_users=no_of_users
        self.ratings=ratings
    def signup(self):
        print(f"sign up done,{self.application_name}")
    def login(self):
        print(f"Welcome to Application,{self.application_name}")
    def info(self):
        print(f"{self.category},{self.company},{self.app_size},{self.no_of_users},{self.ratings}")
    def logout(self):
        print("Thank you")
app1=Application("Instagram","social media","Meta","42.47","1000",4.4)
app2=Application("facebook","social media","meta",30.52,"2000",4)
app3=Application("zomato","Food","eternal Limited","35.45","40.56","4.5")
app1.signup()
app1.login()
app1.logout()
app1.info()
app2.signup()
app2.login()
app2.logout()
app2.info()
app3.signup()
app3.login()
app3.info()
app3.logout()



