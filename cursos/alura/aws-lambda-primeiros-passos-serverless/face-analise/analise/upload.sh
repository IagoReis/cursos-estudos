#!/bin/bash

imagem=$1

aws s3 cp $imagem s3://bucket-alura-1-3/_analise_$imagem