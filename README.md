# pyshposh

[![Build Status](https://travis-ci.org/poise/python.png?branch=master)](https://travis-ci.org/poise/python)

*Python Execution Environment for Remoting Powershell*

This is a helper application intended to facilitate the execution of PowerShell scripts from Linux
hosts. We rely heavily on [WinRM](https://github.com/diyan/pywinrm) for the actual heavy lifting of
making WinRM connections.

## Requirements
### Platforms
* Debian, Ubuntu
* CentOS, Red Hat, Fedora

### Modules
* PyYAML
* [winrm](https://github.com/diyan/pywinrm)

## Example Usage

```bash
./poshtest.py -i localgrabber.ps1 -s settings.yml
```
## Contributors (alphabetically)

- Scott Pack

## License

* pyshposh is licensed under the CC BY-NC 3.0 License: http://creativecommons.org/licenses/by-nc/3.0/
