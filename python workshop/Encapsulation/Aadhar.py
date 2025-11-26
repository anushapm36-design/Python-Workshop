class Adhar:
    def __init__(self,name,adhar_no,dob,finger_print,retina):
        self.name=name
        self.adhar_no=adhar_no
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina

    def display_userData(self):
        print(f"{self.name}")
        print(f"{self.adhar_no}")
        print(f"{self.dob}")
        print(f"{self._finger_print}")
        print(f"{self.__retina}")

var=Adhar("dhanu",12387,"2-jan-20000","drtgddg","green")
var.display_userData()


