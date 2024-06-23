Name:           hollywood-fedora
Version:        1.0
Release:        1%{?dist}
Summary:        Fork of hollywood for fedora

License:        GPLv3+
URL:            https://github.com/acidburnmonkey/hollywood-fedora
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       bash, ccze, ffmpeg

%description
Fork of hollywood for fedora

%prep
%setup -q

%build

%install
# Create the directories in the build root
mkdir -p %{hollywood}/usr/bin
mkdir -p %{hollywood}/usr/share
mkdir -p %{hollywood}/usr/lib

# Copy the contents of the respective directories
cp -a bin/* %{hollywood}/usr/bin/
cp -a share/* %{hollywood}/usr/share/
cp -a lib/* %{hollywood}/usr/lib/

%files
/usr/bin/*
/usr/share/*
/usr/lib/*

%changelog
* Fri Jun 22 2024  acidburnmonkey  acidburnmonkey@gmail.com - 1.0-1
- Initial package
