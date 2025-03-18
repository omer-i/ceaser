import string
from collections import OrderedDict
sorted_dic = {}
def decrypt(encrypted_message):
    alphabet = string.ascii_lowercase
    frequancy = "etaoinsrhdlucmfywgpbvkxqjz"
    decrypted_message = ""
    dicenc = {}
    for c in encrypted_message:
        if c.isalpha():
          if c in dicenc:
            dicenc[c]+= 1
          else:
            dicenc[c] = 1

    sorted_dic = dict(sorted(dicenc.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dic)



    return sorted_dic

encrypted_message = "pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
sorted_dic = decrypt(encrypted_message)
