#!/bin/bash

# TorchTune LoRA Fine-tuning Script
# Generated automatically

export PYTORCH_ENABLE_MPS_FALLBACK=1

cd /Users/thomaybalazs/Projects/quotes-finetuning/notebooks

tune run lora_finetune_single_device --config ../configs/quotes_training.yaml device=mps
