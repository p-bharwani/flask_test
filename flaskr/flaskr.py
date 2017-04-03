#imports

import os
import mysql
import _mysql_connector
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) #create an instance of the application
app.config.from_object(__name__) #load config from this file

# Connect with MySQL server
connect = mysql.connecter.connect(user='admin', database='mydb')
