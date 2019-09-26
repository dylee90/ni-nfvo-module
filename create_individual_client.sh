#!/bin/bash

# To enable using the client APIs of multiple modules within the same module / script, this script generates a module-specific API client with a unique name that can be imported independently.
# This assumes that the client-generating output of swagger-codegen resides in the folder python-client.

TAG="nfvo"

cp -R python-client module_client_$TAG
mv module_client_$TAG/swagger_client module_client_$TAG/swagger_client_$TAG
echo "# coding: utf-8" > module_client_$TAG/__init__.py

sed -i "s|swagger_client|swagger_client_$TAG|g" module_client_$TAG/swagger_client_$TAG/*.py
sed -i "s|swagger_client|swagger_client_$TAG|g" module_client_$TAG/swagger_client_$TAG/api/*.py
sed -i "s|swagger_client|swagger_client_$TAG|g" module_client_$TAG/swagger_client_$TAG/models/*.py

