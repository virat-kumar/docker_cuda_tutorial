import flask
# import dlib
import os
app = flask.Flask(__name__)
app.config["DEBUG"] = True
print("current working directory is ", os.getcwd())
# dlib_gpu_result = str(dlib.DLIB_USE_CUDA)
@app.route('/', methods=['GET'])
def home():
    return f"<h1>Flask app running</h1>"

app.run(host = "0.0.0.0")
