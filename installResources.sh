#!/bin/bash

# installResources.sh

# Lista pakietów do zainstalowania
packages=(
    numpy
    pandas
    requests
    matplotlib
    scikit-learn
    flask
    beautifulsoup4
)

# Instalacja pakietów
for package in "${packages[@]}"; do
    pip install "$package"
done
