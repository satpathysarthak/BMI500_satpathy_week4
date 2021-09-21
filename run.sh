#!/bin/bash

pwd
cd pack/datasets
tar -xvzf TCGA-PANCAN-HiSeq-801x20531.tar.gz
cd ..
pwd
python main.py
date
