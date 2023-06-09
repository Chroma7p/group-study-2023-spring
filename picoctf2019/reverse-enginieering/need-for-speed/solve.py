def decrypt(key: int, encrypted_flag: bytes) -> bytes:
  decrypted_flag = bytearray(encrypted_flag)

  for i in range(len(encrypted_flag)):
    key_prime = key + (i & 1)
    decrypted_flag[i] ^= key_prime & 0xff

    key = (key * 0x55555556) % (1 << 32)
    key = key - ((key >> 31) << 1)

  return bytes(decrypted_flag)

key = 0x12d687ae
encrypted_flag = bytes.fromhex("1a8f098908920abd0ba922a26eac21a46fad35a320af3fa172a427b573e566f237f266f162f676b527a33da231a83ee63baa35a83ce721")

decrypted_flag = decrypt(key, encrypted_flag)
print(decrypted_flag)