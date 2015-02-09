#!/usr/bin/python

import winrm, sys, argparse, yaml

inputfile = ''

parser = argparse.ArgumentParser(description='Short Sample PyshPosh App')
parser.add_argument('-s', '--settings', action='store', dest='settingsfile', default='settings.yaml', help='Path to settings yaml file')

requiredNamed = parser.add_argument_group('required named arguments')
parser.add_argument('-i', '--script', action='store', dest='inputfile', required = True, help='Filename of Powershell Script to Run')

results = parser.parse_args()

# Read in the settings
try:
  file = open('settings.yml')
  settings = yaml.load(file)
except IOError as e:
  print "I/O error({0}): {1}: {2}".format(e.errno, e.strerror, results.inputfile)
  exit(0)
except:
  print "Unexpected error:", sys.exc_info()[0]
  exit(0)

# Now read in the script
ps_script = ''
try:
  myfile = open(results.inputfile, "r")
  ps_script = myfile.read()
except IOError as e:
  print "I/O error({0}): {1}: {2}".format(e.errno, e.strerror, results.inputfile)
  exit(0)
except:
  print "Unexpected error:", sys.exc_info()[0]
  exit(0)

for host in settings['hosts'] :

  # Create the WinRM connection
  session = winrm.Session( host['hostname'], auth=( host['user'], host['pass']) )
  script_rev = session.run_ps(ps_script)

  if script_rev.status_code == 0 :
    print script_rev.std_out
  else :
    print script_rev.std_err

exit(1)
