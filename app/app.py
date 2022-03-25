import flask
# import dlib
import os
import torch 
app = flask.Flask(__name__)
app.config["DEBUG"] = True
pwd= os.getcwd()
print("current working directory is ", os.getcwd())
# dlib_gpu_result = str(dlib.DLIB_USE_CUDA)
test_file = ""
@app.route('/', methods=['GET'])
def home():
    try :
        torch_results = "torch.cuda.memory_allocated: %fGB\n"%(torch.cuda.memory_allocated(0)/1024/1024/1024)
        torch_results += "torch.cuda.memory_reserved: %fGB\n"%(torch.cuda.memory_reserved(0)/1024/1024/1024)
        torch_results += "torch.cuda.max_memory_reserved: %fGB\n"%(torch.cuda.max_memory_reserved(0)/1024/1024/1024)
    except Exception as e:
        torch_results = "Cuda Unavailable"
    file_data = ''
    try : 
        f = open("", "r")
        file_data = f.read()
    except :
        file_data = 'File not found'
    return "<h1>Flask app running present working directory is " + os.getcwd() + torch_results + file_data +  "</h1>"

app.run(host = "0.0.0.0")
