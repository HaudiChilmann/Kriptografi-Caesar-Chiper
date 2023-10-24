import string
abjad = string.ascii_letters  

def enkrip(pesan):
    global abjad
    key = int(input('masukan key              :'))
    cipher = ''
    for i in pesan:
        if i in abjad:
            k = abjad.find(i)
            k = (k + key) % 26  
            cipher = cipher + abjad[k]
        else:
            cipher = cipher + i
    return cipher

def dekrip(cipher):
    global abjad
    key = int(input('masukan key               :'))
    pesan = ''
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)
            k = (k - key) % 26  
            pesan = pesan + abjad[k]
        else:
            pesan = pesan + i
    return pesan

if __name__ == '__main__':
    option = int(input('1. Enkripsi \n2. Dekripsi\nPilih Option: '))
    if option == 1:
        pesan = input('masukan pesan (plaintext): ')
        print(enkrip(pesan))
    elif option == 2:
        cipher = input('masukan pesan (ciphertext): ')
        print(dekrip(cipher))
    else:
        print('Masukkan option 1 atau 2')
