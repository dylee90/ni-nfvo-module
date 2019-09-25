#!/bin/bash

# Copy different swagger clients (e.g., AI and NFVO) and rename them so that each can be called individually.

# AI
sed -i 's|swagger_client|swagger_client_ai|g' ai_module_client/swagger_client_ai/*.py
sed -i 's|swagger_client|swagger_client_ai|g' ai_module_client/swagger_client_ai/api/*.py
sed -i 's|swagger_client|swagger_client_ai|g' ai_module_client/swagger_client_ai/models/*.py

# NFVO
sed -i 's|swagger_client|swagger_client_nfvo|g' nfvo_module_client/swagger_client_nfvo/*.py
sed -i 's|swagger_client|swagger_client_nfvo|g' nfvo_module_client/swagger_client_nfvo/api/*.py
sed -i 's|swagger_client|swagger_client_nfvo|g' nfvo_module_client/swagger_client_nfvo/models/*.py
