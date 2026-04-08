'''class Instagram:
    def __init__(self, username, password):
        self.username = username
        self._password = password
        self._posts = []

  
raju = Instagram('raju', 'raju@123')

print("before updating:", raju.username)
raju.username = 'govind'
print("after updating:", raju.username)'''

'''
class Instagram:
    def __init__(self, username, password):
        self.username = username
        self._password = password
        self._posts = []

    def get_password(self):
        return self._password

    def set_password(self,new_password):
        self._password=new_password

raju = Instagram('raju', 'raju@123')

print("before updating:", raju.username)
raju.username = 'govind'
print("after updating:", raju.username)


print("before updating:",raju.get_password())'''






class Instagram:
    def __init__(self, username, password):
        self.username = username
        self._password = password
        self._posts = []

    @property
    def myposts(self):
        return self._posts

    @myposts.setter
    def myposts(self, postname):
        self._posts.append(postname)

    def get_password(self):
        return self._password

    def set_password(self, new_password):
        self._password = new_password


raju = Instagram('raju', 'raju@123')

print("before updating:", raju.username)
raju.username = 'govind'
print("after updating:", raju.username)

print("before updating:", raju.get_password())
raju.set_password('govind@123')
print("after updating:", raju.get_password())

print(raju.myposts)
raju.myposts = 'sunset.png'
raju.myposts = 'beach.mp4'
print(raju.myposts)

