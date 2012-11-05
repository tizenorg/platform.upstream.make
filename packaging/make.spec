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
Patch2:         make-slowdown-parallelism.diff
Patch3:         make-disable-broken-tests.diff
Patch4:         make-savannah-bug30723-expand_makeflags_before_reexec.diff
Patch5:         make-savannah-bug30612-handling_of_archives.diff
Patch6:         make-fix_whitespace_tokenization.diff
Patch7:         make-glob-faster.patch
# PATCH-FIX-UPSTREAM make-arglength.patch dimstar@opensuse.org -- http://article.gmane.org/gmane.comp.gnu.make.bugs/4219
Patch8:         make-arglength.patch
# PATCH-FIX-UPSTREAM make-parallel-build.patch dmistar@opensuse.org -- http://savannah.gnu.org/bugs/?30653 
Patch9:         make-parallel-build.patch
Patch64:        make-library-search-path.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The GNU make command with extensive documentation.

%prep
%setup -q
%patch2
%patch3 -p1
%patch4
%patch5
%patch6 -p1
%patch7 -p0
%patch8 -p1
%patch9 -p1
if [ %_lib == lib64 ]; then
%patch64
fi

%build
CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --disable-nls
make %{?_smp_mflags}

%check
make check

%install
make DESTDIR=$RPM_BUILD_ROOT install
ln -s make $RPM_BUILD_ROOT/usr/bin/gmake
%find_lang %name

%files -f %name.lang
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
