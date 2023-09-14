import subprocess
try:

    subprocess.call('py -3.9 -m venv myvenv', shell =True)
    subprocess.call('.\myvenv\Scripts\\activate', shell =True)
    subprocess.call('python -m pip install --upgrade pip', shell =True)
    subprocess.call('pip install mlagents', shell =True)
    subprocess.call('pip3 install torch torchvision torchaudio', shell =True)
    subprocess.call('pip install protobuf==3.20.3', shell =True)
    subprocess.call('mlagents-learn --help', shell =True)
 

except:
    print("oopse")