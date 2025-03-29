from hashlib import sha256


def logins(email, stored_logins, password):

    if stored_logins[email] == hash_password(password):
        return True
    else:
        return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()
    

def main():
    login_details = {
        "aksa@gmail.com": 'a0785469c49595a0db372034177e8ad53abf0a0cc265771c839a42d62a7b74b7',
        "student@gmail.com": '712b404ac2d1958ccb99c4ebf9089858f5cf3187239d7d47d3fe452c6ea798ae',
        "xyz@contact.org": "90c6407ab3c70ed2e24a88dd0f52c877dfdedcd175b72592ad50ae1e81d9f1ea"
    }

    print(logins("aksa@gmail.com", login_details, 'aksa'))
    print(logins("aksa@gmail.com", login_details, '12901290'))

    print(logins("student@gmail.com", login_details, 'studentpass'))
    print(logins("student@gmail.com", login_details, '021021'))

    print(logins("xyz@contact.org", login_details, 'xyz22'))
    print(logins("xyz@contact.org", login_details, 'xyz321'))




if __name__ == "__main__":
    main()
