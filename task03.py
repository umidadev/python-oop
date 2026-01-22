class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active


user1 = User("ali123", "ali@gmail.com", True)
user2 = User("dilnoza_k", "dilnoza@mail.com", False)

print(user1.username, user1.email, user1.is_active)
print(user2.username, user2.email, user2.is_active)
