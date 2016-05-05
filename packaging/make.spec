Name:           make
Url:            http://www.gnu.org/software/make/make.html
Provides:       gmake
Version:        4.0
Release:        0
Summary:        GNU make
License:        GPL-2.0+
Group:          Platform Development/Build
Source:         make-%{version}.tar.bz2
Source1001:     make.manifest
BuildRequires:  makeinfo

%description
The GNU make command with extensive documentation.

%prep
%setup -q
cp %{SOURCE1001} .

%build
export AUTOPOINT=true LIBS+=" -ldl "
%reconfigure --disable-nls
%__make %{?_smp_mflags}

%check
%__make check

%install
%make_install
ln -sf make %{buildroot}%{_bindir}/gmake

%files 
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/make
%{_bindir}/gmake
%{_includedir}/gnumake.h
%doc %{_infodir}/make.info-*.gz
%doc %{_infodir}/make.info.gz
%doc %{_mandir}/man1/make.1.gz

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
