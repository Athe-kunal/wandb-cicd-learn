import wandb

print(f"Wandb Version is: {wandb.__version__}")
assert wandb.__version__ == '0.15.8', f"Expected version 0.15.8, but got {wandb.__version__}"
