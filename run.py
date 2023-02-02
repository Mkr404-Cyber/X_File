import os, platform
os.system('git pull')
os.system('clear')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    import Mkr64
elif bit == '32bit':
    import Mkr32
