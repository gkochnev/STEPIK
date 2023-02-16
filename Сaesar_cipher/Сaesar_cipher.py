#  Шифрует/дешифрует текс на русском/английском языке по методу Цезаря,
#  т.е. сдвигом символов в алфавите на указанное число позиций

encrypt_or_decrypt = input('\nШифровать или дешифровать? ("ш" - шифровать/"д" - дешифровать)\n')
while encrypt_or_decrypt.lower() not in 'шд':
        print('Введите "ш" - шифровать или "д" - дешифровать')
        encrypt_or_decrypt = input()

en_or_ru = input('\nКакой язык будем использовать? ("а" - английский/"р" - русский)\n')
while en_or_ru.lower() not in 'ар':
        print('Введите "а" - английский или "р" - русский')
        en_or_ru = input()

rotation = input('\nУкажите сдвиг шифрования/дешифрования:\n')
while rotation.isdigit() == False or int(rotation) < 1:
        print('Введите цифру больше или равную 1')
        rotation = input()
rotation = int(rotation)

text = input('\nВведите текст для шифрования/дешифрования:\n')

def encrypt(lang, rot, text):
        if lang == 'а':
                encrypted_text = ''
                for c in text:
                        if 65 <= ord(c) <= 90:
                                if ord(c) + rot > 90:
                                        encrypted_text += chr(ord(c) + rot - 26)
                                elif ord(c) + rot <= 90:
                                        encrypted_text += chr(ord(c) + rot)
                        elif 97 <= ord(c) <= 122:
                                if ord(c) + rot > 122:
                                        encrypted_text += chr(ord(c) + rot - 26)
                                elif ord(c) + rot <= 122:
                                        encrypted_text += chr(ord(c) + rot)
                        else:
                                encrypted_text += c
                return encrypted_text
        else:
                encrypted_text = ''
                for c in text:
                        if ord('А') <= ord(c) <= ord('Я'):
                                if ord(c) + rot > ord('Я'):
                                        encrypted_text += chr(ord(c) + rot - 32)
                                elif ord(c) + rot <= ord('Я'):
                                        encrypted_text += chr(ord(c) + rot)
                        elif ord('а') <= ord(c) <= ord('я'):
                                if ord(c) + rot > ord('я'):
                                        encrypted_text += chr(ord(c) + rot - 32)
                                elif ord(c) + rot <= ord('я'):
                                        encrypted_text += chr(ord(c) + rot)
                        else:
                                encrypted_text += c
                return encrypted_text

def decrypt(lang, rot, text):
        if lang == 'а':
                decrypted_text = ''
                for c in text:
                        if 65 <= ord(c) <= 90:
                                if ord(c) - rot < 65:
                                        decrypted_text += chr(ord(c) - rot + 26)
                                elif ord(c) - rot >= 65:
                                        decrypted_text += chr(ord(c) - rot)
                        elif 97 <= ord(c) <= 122:
                                if ord(c) - rot < 97:
                                        decrypted_text += chr(ord(c) - rot + 26)
                                elif ord(c) - rot >= 97:
                                        decrypted_text += chr(ord(c) - rot)
                        else:
                                decrypted_text += c
                return decrypted_text
        else:
                decrypted_text = ''
                for c in text:
                        if ord('А') <= ord(c) <= ord('Я'):
                                if ord(c) - rot < ord('А'):
                                        decrypted_text += chr(ord(c) - rot + 32)
                                elif ord(c) - rot >= ord('А'):
                                        decrypted_text += chr(ord(c) - rot)
                        elif ord('а') <= ord(c) <= ord('я'):
                                if ord(c) - rot < ord('а'):
                                        decrypted_text += chr(ord(c) - rot + 32)
                                elif ord(c) - rot >= ord('а'):
                                        decrypted_text += chr(ord(c) - rot)
                        else:
                                decrypted_text += c
                return decrypted_text

if encrypt_or_decrypt == 'ш':
        print(encrypt(en_or_ru, rotation, text))
else:
        print(decrypt(en_or_ru, rotation, text))
