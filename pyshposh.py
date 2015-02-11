#!/usr/bin/python

import winrm, sys, argparse, yaml

def winrm_run( host, ps_script ):

  # Create the WinRM connection
  session = winrm.Session( host['hostname'], auth=( host['user'], host['pass']) )
  script_rev = session.run_ps(ps_script)

  if script_rev.status_code == 0 :
    print script_rev.std_out
    return
  else :
    print script_rev.std_err
    return 1

# DEFINE ALL THE VARIABLES!!!ONE!
parser = argparse.ArgumentParser(description='Short Sample PyshPosh App')
parser.add_argument('-s', '--settings', action='store', dest='settingsfile', default='settings.yaml', help='Path to settings yaml file')
parser.add_argument('-H', '--host', action='store', dest='targethost', default='', help='Remote host')

requiredNamed = parser.add_argument_group('required named arguments')
parser.add_argument('-i', '--script', action='store', dest='inputfile', default='', required = True, help='Filename of Powershell Script to Run')

results = parser.parse_args()

# Read in the settings
try:
  file = open(results.settingsfile, 'r')
  settings = yaml.load(file)
except IOError:
  print 'Cannot Open: ', results.settingsfile
  exit(0)
except:
  print "Unexpected error:", sys.exc_info()[0]
  exit(0)
else:
  file.close()

## Now read in the script
try:
  myfile = open(results.inputfile, 'r')
except IOError:
  print 'Cannot Open: ', results.inputfile
else:
  ps_script = myfile.read()
  myfile.close()

# Finally run the script on all hosts or just the one
if results.targethost != '':
  if results.targethost in settings['hosts']:
    print 'Found host in list: ', results.targethost
    winrm_run( settings['hosts'][results.targethost], ps_script )
  else:
    print 'Invalid configuration for host: ', results.targethost
else:
  for host in settings['hosts']:
    winrm_run( settings['hosts'][host], ps_script )

exit(1)


