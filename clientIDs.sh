#!/bin/bash

# After copying different swagger clients (e.g., AI and NFVO) into module_client_*/swagger_client_* folders, rename them so that each can be called / imported individually.
# Example for NFVO module: import module_client_nfvo.swagger_client_nfvo as swagc_nfvo.

# AI
sed -i 's|swagger_client|swagger_client_ai|g' module_client_ai/swagger_client_ai/*.py
sed -i 's|swagger_client|swagger_client_ai|g' module_client_ai/swagger_client_ai/api/*.py
sed -i 's|swagger_client|swagger_client_ai|g' module_client_ai/swagger_client_ai/models/*.py

# NFVO
sed -i 's|swagger_client|swagger_client_nfvo|g' module_client_nfvo/swagger_client_nfvo/*.py
sed -i 's|swagger_client|swagger_client_nfvo|g' module_client_nfvo/swagger_client_nfvo/api/*.py
sed -i 's|swagger_client|swagger_client_nfvo|g' module_client_nfvo/swagger_client_nfvo/models/*.py
