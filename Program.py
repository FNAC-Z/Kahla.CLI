#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Manager
from flask_script import Command
from Startup import Startup
from platform import system
from Services.HomeFloderConfig import HomeFloderConfig

app = Flask(__name__)
manager = Manager(app)
configpath = HomeFloderConfig()

# Seed Config Path
configpath.mkdirconfigpath()
# Configure Routing
Startup.ConfigureRouting(manager)

if __name__ == "__main__":
    manager.run()