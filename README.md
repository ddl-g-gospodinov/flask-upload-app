# flask-upload-app

This Application aims to allow for unrestricted uploads via both the browser and cli using cUrl. 
The code is using flask, it is intended to run in Domino Data Lab platform.  Tested on 5.8 and 5.11 . 

Package requirements are minimal and should already be satisfied in the Domino Standard Environments. 

### Installation
Clone the repository in to your project.

Change **BASEURL** variable in script **app-flask.py** . 

Change **MYPATH** variable to the location you would like files to be written to (local dataset is prefered). 
Run **app.sh**. 

### Deployment settings and considerations. 
For the app to be available without authentication you will have to start it with **permissions (Anyone, including anonymous users)**

For uploading larger than **25MiB** files you have to set the central config key: 
**com.cerebro.domino.computegrid.kubernetes.apps.nginx.clientBodyMaxSizeMiB**

NOTE: The maximum size for  apps.nginx.clientBodyMaxSizeMiB tested is 5120 . Anything larger might need additional settings changed. 

### Uploading files 
After starting the application check the view app button. 
The main page of the app will allow you to submit a file for upload . 
If a cURL upload option is required the page will construct for you the curl command with the correct app url (excluding the iframe page) 
Any uploaded files will be instantly available in the Project's dataset. 


### Known issues 
So far it has been noticed that a 502 might occur . This is a result of the nginx sidecar running out of memory and you will notice an exit code 137 in the Kubernetes pod describe.
This usually happens if we try to upload several large (more than 50mb)  files simultaneously or in immediate succession.  

The application recovers on its own as Domino restarts the nginx container. You can also adjust the particular app deployment in Kubernetes and set a larger limit/request for the nginx container. 
