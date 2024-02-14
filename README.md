# Finetuning with Axolotl

## Start the Docker

`docker compose up -d`

`docker compose exec axolotl bash`  

## Start the Script

`accelerate launch -m axolotl.cli.train /training/qlora-openllama3b.yaml`
