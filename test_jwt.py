from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],
                           deprecated='auto')

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

get_pass = input('ведите пароль:')
hash_pass = get_password_hash(get_pass)
print(hash_pass)
print(verify_password(get_pass, hash_pass))
