
from User import User


user = User.register()
print(user.password)
User.login(user.email, user.password)
print('login done')

