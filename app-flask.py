import os
import sys
import flask
import subprocess
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

# Set variables 

# CHANGE THE FOLLOWING VARIABLES AS PER YOUR SETUP
# - Dataset path where to save the files 
MYPATH = "/domino/datasets/local/uploader-test-2/files"
# - The base URL for your deployment 
BASEURL = "emeaplay28690.support-team-sandbox.domino.tech"


# Variables to help construct the cURL example upload command 
DPROJECT = os.environ.get("DOMINO_PROJECT_NAME")
DUSER = os.environ.get("DOMINO_USER_NAME")
DRUNID = os.environ.get("DOMINO_RUN_ID")


# Domino specific proxy code 

class ReverseProxied(object):
  def __init__(self, app):
      self.app = app
  def __call__(self, environ, start_response):
      script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
      if script_name:
          environ['SCRIPT_NAME'] = script_name
          path_info = environ['PATH_INFO']
          if path_info.startswith(script_name):
              environ['PATH_INFO'] = path_info[len(script_name):]
      # Setting wsgi.url_scheme from Headers set by proxy before app
      scheme = environ.get('HTTP_X_SCHEME', 'https')
      if scheme:
        environ['wsgi.url_scheme'] = scheme
      # Setting HTTP_HOST from Headers set by proxy before app
      remote_host = environ.get('HTTP_X_FORWARDED_HOST', '')
      remote_port = environ.get('HTTP_X_FORWARDED_PORT', '')
      if remote_host and remote_port:
          environ['HTTP_HOST'] = f'{remote_host}:{remote_port}'
      return self.app(environ, start_response)
 

app = flask.Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)


@app.route('/')  
def upload():
    return render_template("file_upload_form.html", DUSER=DUSER, DPROJECT=DPROJECT, DRUNID=DRUNID, MYPATH=MYPATH, BASEURL=BASEURL)  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        # Change the saved path to MYPATH
        f.save(f'{MYPATH}/{f.filename}')  
        return render_template("success.html", name = f.filename)  


