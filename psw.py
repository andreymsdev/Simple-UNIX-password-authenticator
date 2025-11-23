import pwd 
import getpass
import sys
from passlib.hash import sha512_crypt, md5_crypt, des_crypt

# Mapeia os identificadores de hash do Unix para os formatos do passlib
# Passlib é inteligente o suficiente para detectar o formato, mas isso garante compatibilidade
HASH_MAP = {
    '1': md5_crypt,
    '5': sha512_crypt, 
    '6': sha512_crypt,
    '': des_crypt, 
}

def login():
    username = input('username: ')
    try:
        user_info = pwd.getpwnam(username)
        stored_hash = user_info.pw_passwd 

        if stored_hash in ('x', '*'): 
            print('Error: No support for shadow passwords (hash is in /etc/shadow)')
            return False
            
        cleartext_password = getpass.getpass('Enter your password: ')
        
        # passlib verifica automaticamente o formato e o sal a partir do hash armazenado
        # .verify() que lida com a lógica de comparação e hashing internamente
        # Usamos try/except para lidar com hashes inválidos que passlib pode rejeitar
        try:
            hash_alg = HASH_MAP.get(stored_hash.split('$')[1][0], des_crypt)
            if hash_alg.verify(cleartext_password, stored_hash):
                return True
        except Exception:
            from passlib.hash import sun_md5
            if sun_md5.verify(cleartext_password, stored_hash):
                return True
            print("Could not verify password with passlib formats.")
            return False

        return False 

    except KeyError:
        print('User not found.')
        return False
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


if login():
    print('Login successful!')
else:
    print('Incorrect username or password.')
