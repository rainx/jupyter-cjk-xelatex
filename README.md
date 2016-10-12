# jupyter-cjk-xelatex
Handle the encoding error for jupyter nbconvert to convert notebook to pdf document

Make two changes before gen pdf file:

1. remove title \maketitle
2. replace  
        \documentclass[11pt]{article}
    to 
        \documentclass{ctexart}

Installation:

    pip install jupyter-cjx-xelatex

or 

    python setup.py install

then change ~/.jupyter/jupyter_notebook_config.py

    c.PDFExporter.latex_command=['cjk-xelatex', '{filename}']
