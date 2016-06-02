class Friend:
    choclates = 10

    def distribute(self):
        self.choclates -= 1
        print('Distributed 1 choclate')

    def check_choclates(self):
        return self.choclates

friend1 = Friend()


while friend1.check_choclates() > 0:
    print(friend1.check_choclates(), ' choclates left')
    friend1.distribute()

if friend1.choclates == 0:
    print('Choclates Distributed')

