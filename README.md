# Finetuning with Axolotl

## Start the Docker

`docker compose up -d`

`docker compose exec axolotl bash`  

## Start the Script
Prepare the dataset:
  
`CUDA_VISIBLE_DEVICES="" python -m axolotl.cli.preprocess training/qlora-qwen0B.yaml`


`accelerate launch -m axolotl.cli.train training/qlora-openllama3b.yaml`

## Update

Find the fitting docker container here: https://github.com/OpenAccess-AI-Collective/axolotl?tab=readme-ov-file#docker
