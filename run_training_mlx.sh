#!/bin/bash

# MLX LoRA Training Script
# Generated automatically

cd /Users/thomaybalazs/Projects/quotes-finetuning/notebooks

python -m mlx_lm lora --model mlx-community/Llama-3.2-3B-Instruct-4bit --train --data ../data/training/mlx_format --batch-size 2 --iters 2000 --learning-rate 5e-05 --steps-per-report 25 --steps-per-eval 100 --save-every 200 --adapter-path /Users/thomaybalazs/Projects/quotes-finetuning/models/llama3.2-3b-quotes-lora-mlx --max-seq-length 2048 --grad-checkpoint
