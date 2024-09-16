

def get_login_details(user_id,password):

    if user_id == 'rdkendre@gmail.com' and password == '123456':
        print("User id is in database")

        return "Login Successful"

    else:
        return "User id or password is incorrect"