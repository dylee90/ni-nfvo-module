#!/bin/bash
# From Swagger editor, export swagger.yaml and generate server / client code.
# Copy the three files to this directory and run this script.

# Remove old directories.
if [ -d python-client ]; then rm -rf python-client; fi;
if [ -d python-flask-server ]; then rm -rf python-flask-server; fi;

# Extract generated code.
unzip python-client-generated.zip
unzip python-flask-server-generated.zip

# Copy main code / files into server folder.
cp ai_module.py python-flask-server

# Clean up.
rm python-client-generated.zip
rm python-flask-server-generated.zip
