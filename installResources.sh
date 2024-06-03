#!/bin/bash




packages=(
    numpy
    pandas
    requests
    matplotlib
    scikit-learn
    flask
    beautifulsoup4
)


for package in "${packages[@]}"; do
    pip install "$package"
done
