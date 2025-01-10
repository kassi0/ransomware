import os
import pyaes


# Abrir o arquivo encriptado

file_name = 'teste.txt.ramsonkassio'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Chave de descriptografia

key = b'cassiotellestest'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
