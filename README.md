# flask-upload-app
Simple application run on Domino which allows file uploads via browser or curl cli 

This Application aims to allow for unrestricted uploads via both the browser and cli using cUrl. 
The code is using flask, it is intended to run in Domino Data Lab platform.  Tested on 5.8 and 5.11 . 

Package requirements are minimal and should already be satisfied in the Domino Standard Environments. 

### Installation
Clone the repository in to your project.
Change BASEURL variable in script app-flask.py . 
Change MYPATH variable to the location you would like files to be written to (local dataset is prefered). 
Run app.sh. 

### Deployment settings and considerations. 
For the app to be available without authentication you will have to start it with permissions (Anyone, including anonymous users)

For uploading larger than 25MiB files you have to set the central config key: com.cerebro.domino.computegrid.kubernetes.apps.nginx.clientBodyMaxSizeMiB 

NOTE: The maximum size for  apps.nginx.clientBodyMaxSizeMiB tested is 5120 . Anything larger might need additional settings changed. 
