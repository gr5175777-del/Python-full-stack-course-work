'''
class whatsappV0:
    def status(self):
        print("you can upload image and videos")

class whatsappV1:
    def status(self):
        print("you can like,react and reply")
        
class whatsappV2(whatsappV0,whatsappV1):
    def status(self):
       whatsappV0.status(self)
       whatsappV1.status(self)
       
       print("you can add music and filters also")


raju = whatsappV2()
raju.status()'''


