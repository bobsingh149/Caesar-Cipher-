import enchant
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
d = enchant.Dict('en_US')


def decrypt():

    print(logo)

    end = False

    while True:

        option = int(input('Press 1 to decrypt 0 to exit:- '))

        if option == 0:
            break

        if option != 1:
            print('invalid Response')
            continue

        ct = str(input('Enter Cipher Text:- '))

        ct = ct.lower()

        validWords = []

        for i in range(26):

            pt = ''

            print('for key ', end=' ')
            print(i)
            for w in ct:

                if w == ' ':
                    pt += ' '
                    continue

                idx = alphabet.index(w)
                nidx = idx+i
                nidx = nidx % 26
                pt += alphabet[nidx]

            print(pt)

            words = pt.split(' ')

            correct = True

            for word in words:
                if not d.check(word):
                    correct = False
                    break

            if correct:

                validWords.append(pt)

        print()
        print('Valid words list')
        print(validWords)


decrypt()
