Name:           make
Url:            http://www.gnu.org/software/make/make.html
Provides:       gmake
PreReq:         %install_info_prereq
Version:        3.82
Release:        0
Summary:        GNU make
License:        GPL-2.0+
Group:          Development/Tools/Building
Source:         make-%version.tar.bz2

%description
The GNU make command with extensive documentation.

%prep
%setup -q

%build
CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --disable-nls
make %{?_smp_mflags}

%check
make check

%install
make DESTDIR=$RPM_BUILD_ROOT install
ln -s make $RPM_BUILD_ROOT/usr/bin/gmake

%files 
%defattr(-,root,root)
/usr/bin/make
/usr/bin/gmake
%doc /usr/share/info/make.info-*.gz
%doc /usr/share/info/make.info.gz
%doc /usr/share/man/man1/make.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%changelog
