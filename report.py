import re, os
import wandb
comment = os.getenv('PR_COMMENT', '')
match = re.search('/wandb[\s+](\S+)', comment)

with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    if match:
        print(f'VAL_FOUND=true', file=f)
        print(f'RUN_ID={match.group(1)}', file=f)
    else:
        print(f'VAL_FOUND=false', file=f)

assert wandb.__version__ == '2.1.01', f'Expected version 2.1.01, but got {wandb.__version__}'
