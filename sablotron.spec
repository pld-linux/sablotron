%define		expat_ver	1.1.1
%define		sablot_ver	0.42
%define		arname		Sablot
Summary:	XSL Transformations Processor
Summary(pl):	XSL Transformations Processor
Name:		sablotron
Version:	%{sablot_ver}
Release:	1
License:	Mozilla Public License Version 1.1 or GPL
URL:		http://www.gingerall.com/charlie-bin/get/webGA/act/sablotron.act
Source0:	http://www.gingerall.com/download/%{arname}-%{sablot_ver}.tar.gz
Source1:	http://www.gingerall.com/download/%{arname}-Expat-%{expat_ver}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Group:		Applications/Publishing/XML
Group(pl):	Aplikacje/Publikowanie/XML
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
##Requires:	expat

%description
Sablotron is an attempt to develop fast, compact and portable XSLT
processor. We need such a processor for Charlie, so we have decided to create it.
Sablotron is an open project; other users and developers are encouraged to use it or to
help us testing or improving it. 
The goal of this project is to create a reliable and fast XSLT
processor conforming to the W3C specification, which is available for public and can be
used as a base for multi-platform XML data distribution systems. 

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
%{name} header files.

%description -l pl devel
Pliki nag³ówkowe %{name}.


%package -n expat
Summary:	XML 1.0 parser
Summary(pl):	XML 1.0 parser
Version:	%{expat_ver}
Release:	1
License:	Mozilla Public License Version 1.1 or GPL
URL:		http://www.jclark.com/xml/expat.html
Group:		Applications/Publishing/XML
Group(pl):	Aplikacje/Publikowanie/XML
#Patch0:		expat.patch

%description -n expat
Expat is an XML 1.0 parser written in C. It aims to be fully
conforming. It is currently not a validating XML parser.

%description -l pl -n expat 
Expat to parser XML 1.0 napisany w jêzyku C.

%package -n expat-devel
Summary:	expat header files
Summary(pl):	Pliki nag³ówkowe expat
Version:	%{expat_ver}
Release:	1
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	expat = %{expat_ver}

%description -n expat-devel
expat header files.

%description -l pl -n expat-devel
Pliki nag³ówkowe expat.


%prep
%setup0 -q -a1 -n %{arname}-%{sablot_ver}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}
%{__make} DESTDIR=$RPM_BUILD_ROOT install
%{!?debug:strip $RPM_BUILD_ROOT%{_libdir}/*.so.*.*}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n expat -p /sbin/ldconfig
%postun -n expat -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sabcmd
%attr(755,root,root) %{_libdir}/libsablot.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/s*
%{_libdir}/libsablot.so

%files -n expat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxml*.so.*.*

%files -n expat-devel
%defattr(644,root,root,755)
%{_includedir}/xml*
%{_libdir}/libxml*.so
