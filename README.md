Distro agnostic since is all bash scripts anyway no reason to be
bound to snap.

## Dependencies
- IF you want to make use of the ACII map install jp2a from copr https://copr.fedorainfracloud.org/coprs/trixieua/jp2a/ 
```
ccze ffmpeg
```


## Usage
On therminal call
```
hollywood
```

## Installation
```
git clone --depth 1 https://github.com/acidburnmonkey/hollywood-linux.git
cd hollywood-linux
sudo cp -r bin lib share /usr/
```
## Removal
```
sudo rm /bin/hollywood
sudo rm -r /lib/hollywood
sudo rm -r /usr/share/hollywood
```

## Sample Apps:
- atop ,bmon ,cmatrix, dnstop ,ethstatus ,glances ,htop, ifstat
- iotop ,iptotal, iptraf-ng, itop, jnettop, kerneltop, latencytop
- logtop, netmrg, nload, nmon, ntop, powertop, sagan, slurm
- snetz, top, tiptop, vnstat
