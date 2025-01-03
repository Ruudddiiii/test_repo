import os
SECRET = os.environ['TOKEN']
if SECRET == "TrustNo1":
    print("No one can be trusted")
print(SECRET)
