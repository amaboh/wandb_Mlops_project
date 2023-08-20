import re, os
comment = os.getenv('PR_COMMENT', '')
match = re.search('/wandb[\s+](\S+)', comment)

with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    if match:
        print(f'VAL_FOUND=true', file=f)
        print(f'RUN_ID={match.group(1)}', file=f)
    else:
        print(f'VAL_FOUND=false', file=f)