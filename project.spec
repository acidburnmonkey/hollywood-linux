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
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share
mkdir -p %{buildroot}/usr/lib

# Copy the contents of the respective directories
cp -a bin/* %{buildroot}/usr/bin/
cp -a share/* %{buildroot}/usr/share/
cp -a lib/* %{buildroot}/usr/lib/

%files
/usr/bin/*
/usr/share/*
/usr/lib/*

%changelog
* Sat Jun 22 2024  acidburnmonkey  acidburnmonkey@gmail.com - 1.0-1
- Initial package
