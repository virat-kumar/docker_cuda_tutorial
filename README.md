## This is a tutorial which demonstrates the following :-  
### 1. How to compose docker file.
### 2. How to use nvidia-cuda inside docker.
>> **Note:-** ```nvidia-container-toolkit``` nust be installed
### 3. Run python dlib package to check container is using GPU.
### 4. Expose a Flask application to host machine.
### 5. Mount a volume and folder.


## After building docker file run
#### docker run --rm  -p 8000:5000 dockercudatutorial
#### Go to browser and check localhost:8000 port for result

>> ##### **Note:-** The flask application runs with *ENTRYPOINT* instruction instead of *CMD* so ctrl+c won't kill the running container. Use ```docker container stop <<name-of-container>>``` to stop  
### Building image  
```docker build --pull --rm -f "./Dockerfile" -t <name of im age>:<tag> "." ```  