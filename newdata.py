import json
import os
if os.name == 'nt':
    pass
if os.name == 'linux':
    import simplejson as json
else:
    try:
        import json
    except:
        import simplejson as json
with open('settings.json', 'r+') as f:
    data = json.load(f)
    data['token'] = input("Please Enter Your Account Token: ")
    data['channel'] = input("Please Enter Your Channel ID: ")
    data['owodmid'] = input("Please Enter Your OwO's DMs Channel ID: ")
    while True:
        data["proxy"] = input("Will You Use Proxy? [YES/NO]")
        data["proxy_"] = {}
        if data["proxy"].upper() == "YES":
          data["proxy_"]["server"] = input("Proxy Server: ")
          data["proxy_"]["port"] = input("Proxy Server Port: ")
          break
        if data["proxy"].upper() == "NO":
          data["proxy_"]["server"] = None
          data["proxy_"]["port"] = None
          break
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()     # remove remaining part
