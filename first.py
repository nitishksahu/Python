import myModule


def inr_to_dollars(inr): return inr / 60


friends = ['Anuj', 'Deepak', 'Koshank', 'Ritesh']

for friend in friends:
    if friend is "Ritesh":
        print('Bhadrak Wala Found \n')
        break
    else:
        print(friend + ' Is Not Prawn King \n')

ruppee = 180
dollar = inr_to_dollars(ruppee)
print('The converted dollar amount of ', ruppee, 'is ', dollar, '\n')

myModule.print_name()
