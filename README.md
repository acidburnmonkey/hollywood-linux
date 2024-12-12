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
git clone --depth 1 https://github.com/acidburnmonkey/hollywood-fedora.git
cd hollywood-fedora
sudo cp -r bin lib share /usr/
```
## Removal
```
sudo rm /bin/hollywood
sudo rm -r /lib/hollywood
sudo rm -r /usr/share/hollywood
```

## OG Creator notes
Launch Byobu
Open a random number of splits, random sizes
In each split, run a noisy text app

Rules:
- Must work as a non-root user
- Must display information indefinitely (a la "watch", or cmatrix)
- Can use a while/true + a timeout
- Must not OOM a system
- Must not over load a system
- Must not be too egregious with I/O
- Must not require outbound internet access

Sample Apps:
- atop		# xxx Root
- bmon		# DONE
- cmatrix	# DONE
- dnstop	# xxx Root
- ethstatus
- glances
- htop
- ifstat
- iotop
- iptotal
- iptraf-ng
- itop
- jnettop
- kerneltop
- latencytop
- logtop
- netmrg
- nload
- nmon
- ntop
- powertop
- sagan
- slurm
- snetz
- top
- tiptop
- vnstat
