▽
#!/usr/bin/python

import winrm, sys, argparse, yaml

inputfile = ''

parser = argparse.ArgumentParser(description='Short Sample PyshPosh App')

parser.add_argument('-i', action='store', dest='inputfile', help='Filename of Powershell Script to Run')
parser.add_argument('-s', action='store', dest='settingsfile', default='settings.yaml', help='Path to settings yaml file')

results = parser.parse_args()

with open (results.inputfile, "r") as myfile:
  ps_script=myfile.read()

file = open('settings.yml')
settings = yaml.load(file)

for host in settings['hosts'] :

  # Create the WinRM connection
  session = winrm.Session( host['hostname'], auth=( host['user'], host['pass']) )
  script_rev = session.run_ps(ps_script)

  if script_rev.status_code == 0 :
    print script_rev.std_out
  else :
    print script_rev.std_err

exit(1)
