def username_generator(first_name,last_name):
  username = first_name[0:3] + last_name[0:4]
  return username

new_user = username_generator("Oberton", "Poberton")
# print(new_user)

def password_generator(user_name):
  password = ""
  for i in range(len(user_name)):
    password = user_name[-1] + user_name[:-1]
    return password
  
new_password = password_generator("ObePobe")
print(new_password)