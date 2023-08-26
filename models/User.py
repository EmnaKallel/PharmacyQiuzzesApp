class User :
    id = 0
    def __init__(self, userName, password, isAdmin=False) :
        self.id = User.id
        self.isAdmin = isAdmin
        self.userName = userName
        self.password = password
        User.id = User.id + 1