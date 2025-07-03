#caesar cypher decode message
def decrypt(message, offset):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  cipher = ""
  for x in message:
    pos = alphabet.find(x)
    if pos <0:
      cipher += x
    else:
      cipher += alphabet[(pos+offset)%26]
  return cipher

# coded_text = ("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!")
coded_text = ("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.")
coded_text2 = ("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!")
coded_text3= ("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")

decoded_text = decrypt(coded_text3,7)
# decoded_text = decrypt(coded_text2,14)
#print(decoded_text)

#ecaesar cypher encode message
def encrypt(message, offset):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  decipher = ""
  for x in message:
    pos = alphabet.find(x)
    if pos <0:
      decipher += x
    else:
      decipher += alphabet[(pos+offset)%26]
  return decipher

# decoded_text = ("Hi how are you!")

# coded_text = encrypt(decoded_text,10)
# print(coded_text)

# vigenere cipher decode
def v_decrypt(ctext, key):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    ptext = ''
    key_idx=0
    for char in ctext:
        pos = letters.find(char)
        if pos<0: #pass up punctiation
            ptext += char
        else:
            ptext += letters[(pos-letters.find(key[key_idx]))%26]
            key_idx = (key_idx+1)%len(key)
    return ptext

ciphertext = 'dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!'
plaintext  = v_decrypt(ciphertext, 'friends')
print(plaintext)

#vigenere cipher encode
def v_encrypt(ptext, key):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    ctext = ''
    key_idx=0
    for char in ptext:
        pos = letters.find(char)
        if pos<0: #pass up punctiation
            ctext += char
        else:
            ctext += letters[(pos+letters.find(key[key_idx]))%26]
            key_idx = (key_idx+1)%len(key)
    return ctext

plaintext  = 'These ciphers can get kinda cool! Next thing up is trying to crack this without knowing the key!'
ciphertext = v_encrypt(plaintext, 'friends')
print(ciphertext)