import base64
import hashlib
import random
import string
from Crypto.Cipher import AES

IV = "@@@@&&&&####$$$$"

def _format_key(key):
    if not key:
        return "1234567890123456".encode('utf-8')
    key_bytes = key.encode('utf-8')
    if len(key_bytes) < 16:
        key_bytes = key_bytes.ljust(16, b'0')
    elif 16 < len(key_bytes) < 24:
        key_bytes = key_bytes.ljust(24, b'0')
    elif 24 < len(key_bytes) < 32:
        key_bytes = key_bytes.ljust(32, b'0')
    elif len(key_bytes) > 32:
        key_bytes = key_bytes[:32]
    return key_bytes

def _pad(s):
    BLOCK_SIZE = 16
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def _unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def encrypt(input_str, key):
    padded_str = _pad(input_str)
    key_bytes = _format_key(key)
    cipher = AES.new(key_bytes, AES.MODE_CBC, IV.encode('utf-8'))
    encrypted_bytes = cipher.encrypt(padded_str.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt(encrypted_str, key):
    try:
        key_bytes = _format_key(key)
        cipher = AES.new(key_bytes, AES.MODE_CBC, IV.encode('utf-8'))
        decrypted_bytes = cipher.decrypt(base64.b64decode(encrypted_str))
        return _unpad(decrypted_bytes.decode('utf-8'))
    except Exception:
        return ""

def generate_signature(params, key):
    if isinstance(params, dict):
        params_string = _get_param_string(params)
    elif isinstance(params, str):
        params_string = params
    else:
        return ""
    
    salt = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
    final_string = params_string + "|" + salt
    hasher = hashlib.sha256(final_string.encode('utf-8'))
    hash_str = hasher.hexdigest()
    hash_salt = hash_str + salt
    return encrypt(hash_salt, key)

def verify_signature(params, key, checksum):
    if not checksum or not key:
        return False
    try:
        paytm_hash = decrypt(checksum, key)
        if not paytm_hash or len(paytm_hash) < 4:
            return False
        salt = paytm_hash[-4:]
        if isinstance(params, dict):
            params_string = _get_param_string(params)
        elif isinstance(params, str):
            params_string = params
        else:
            return False
        
        final_string = params_string + "|" + salt
        hasher = hashlib.sha256(final_string.encode('utf-8'))
        calculated_hash = hasher.hexdigest()
        return paytm_hash[:-4] == calculated_hash
    except Exception:
        return False

def _get_param_string(params):
    sorted_keys = sorted(params.keys())
    param_string = []
    for key in sorted_keys:
        if key.upper() != "CHECKSUMHASH" and params[key] is not None and str(params[key]).lower() != "null":
            param_string.append(str(params[key]))
    return "|".join(param_string)
