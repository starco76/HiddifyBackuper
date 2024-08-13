import sys,os

token = sys.argv[1]
# os.system('pip install -r requirements.txt')
with open('token','w') as f:
    f.write(token)
