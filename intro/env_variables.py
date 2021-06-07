import os

# stage = os.environ['STAGE'].upper()
stage = os.getenv('STAGE', 'dev').upper()

output = f"We are running in {stage}"

if stage.startswith('PROD'):
    output = "DANGER!!!" + output

print(output)

#STAGE=stage python env_variables.py