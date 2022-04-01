import flask
# import dlib
import os
import torch 
app = flask.Flask(__name__)
app.config["DEBUG"] = True
pwd= os.getcwd()
import subprocess
print("current working directory is ", os.getcwd())
# dlib_gpu_result = str(dlib.DLIB_USE_CUDA)
test_file = ""
@app.route('/', methods=['GET'])
def home():
    torch_results = ""
    try :
        # torch_results = "torch.cuda.memory_allocated: %fGB\n"%(torch.cuda.memory_allocated(0)/1024/1024/1024)
        # torch_results += "torch.cuda.memory_reserved: %fGB\n"%(torch.cuda.memory_reserved(0)/1024/1024/1024)
        # torch_results += "torch.cuda.max_memory_reserved: %fGB\n"%(torch.cuda.max_memory_reserved(0)/1024/1024/1024)
        # torch_results += "CUDA SUPPORT {}" .format(torch.cuda.is_available())
        torch_results += "Executing command: "
        torch_results  += subprocess.run(['nvidia-smi', '-L'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        torch_results += "Done executing command: {}\n".format(test_file)
    except Exception as e:
        torch_results += "Cuda Unavailable"
    file_data = ''
    try : 
        f = open("", "r")
        file_data = f.read()
    except :
        file_data = 'File not found'
    return "Flask app running present working directory is " + os.getcwd() + "   ----" + torch_results + file_data 

app.run(host = "0.0.0.0")
