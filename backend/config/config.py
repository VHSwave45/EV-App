DB_HOST = "localhost"                # Database host (IP address or hostname, Bijv. localhost)
DB_PORT =  3306               # Database port (Bijv. 3306)
DB_NAME = "evbox_manager"                # Database name
DB_USER = "root"                # Database user (Bijv. root)
DB_PASSWORD = "rootpassword"            # Database password

SERVER_HOST = "localhost"            # Server host (IP address or hostname, Bijv. localhost)
SERVER_PORT =   8001            # Server port

SECRET_KEY = "ppsecret"             # Secret key for JWT (should be kept secret and secure)

serial_device = ""


management_twofa = "BQRE2OQYDTSAD3ZYOPK2Q5U26D6PFLGY" 
admin_twofa = "ROMXQP6GKFTFSITN6VDIHTUUFV3RJ7ON"

# 2FA Documentation:

# The two secret twofa tokens are used to register as an management/admin user
# How these tokens work. You add this code to any 2fa app (I personally recommend to use Microsoft Authenticator)
# Then on registration you will be able to use a code that gets regenerated every 30 seconds in that app.
# The user who posses the token in authenticator app and enters the code generated from the 2fa app will be
# able to register as either management/admin depending on the token you choose to use. Hope this helps.

# I also added the generate2fa.py in the config directory
# You can just generate a new token with it if you don't want
# to use mine. It matters not because you decide your own token
# in config.py that we do not share anyway. DO NOT FORGET TO ADD
# THE TOKEN TO THE AUTHENTICATOR APP YOU USE

# To add the token to Microsoft Authenticator you press on the big + in the app on the top-middle-right corner
# After select "Other account (Google, Facebook, etc)". It will prompt you to scan a qr code. Just ignore that
# and press the big blue button (Text:"Enter code manually") on the bottom. You can give any name to the "Account name"

# field and enter the secret twofa code that you either generated or the one I've given you already.
