Name:           hollywood
Version:        1.0
Release:        1%{?dist}
Summary:        Fork of hollywood for fedora

License:        GPLv3+
URL:            https://github.com/acidburnmonkey/hollywood-fedora
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       bash, ccze, ffmpeg, tmux

%description
Fork of hollywood for fedora

%prep
# Create a temporary directory to extract the tarball
mkdir -p %{_builddir}/%{name}-%{version}
tar -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version}

%build

%install
# Create the directories in the build root
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share
mkdir -p %{buildroot}/usr/lib

# Copy the contents of the respective directories
cp -a %{_builddir}/%{name}-%{version}/bin/* %{buildroot}/usr/bin/
cp -a %{_builddir}/%{name}-%{version}/share/* %{buildroot}/usr/share/
cp -a %{_builddir}/%{name}-%{version}/lib/* %{buildroot}/usr/lib/

%files
/usr/bin/*
/usr/share/*
/usr/lib/*

%changelog
* Sat Jun 22 2024  acidburnmonkey  acidburnmonkey@gmail.com - 1.0-1
- Initial package
