#
# Conditional build:
# _with_javascript	- enable experimental JavaScript XSLT extension
#
Summary:	XSL Transformations Processor
Summary(pl):	Procesor Transformacji XSL
Summary(pt_BR):	Processador de XSL
Name:		sablotron
Version:	0.97
Release:	1
License:	Mozilla Public License Version 1.1 or GPL
Group:		Applications/Publishing/XML
#Source0Download:	http://www.gingerall.com/charlie/ga/xml/d_sab.xml
Source0:	http://download-2.gingerall.cz/download/sablot/Sablot-%{version}.tar.gz
# Source0-md5: 253d5e7738d85beecc2c274478431529
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-am15.patch
Patch2:		%{name}-expat.patch
URL:		http://www.gingerall.com/charlie-bin/get/webGA/act/sablotron.act
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel >= 1.95.6-2
%{?_with_javascript:BuildRequires:	js-devel}
BuildRequires:	libtool
BuildRequires:	perl-XML-Parser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libsablotron0

%description
Sablotron is an attempt to develop fast, compact and portable XSLT
processor. We need such a processor for Charlie, so we have decided to
create it. Sablotron is an open project; other users and developers
are encouraged to use it or to help us testing or improving it. The
goal of this project is to create a reliable and fast XSLT processor
conforming to the W3C specification, which is available for public and
can be used as a base for multi-platform XML data distribution
systems.

%description -l pl
Sablotron jest pr�b� stworzenia szybkiego, ma�ego i przeno�nego
procesora XSLT. Potrzebowali�my takiego procesora dla projektu
Charlie, wi�c zdecydowali�my si� stworzy� odpowiedni. Sablotron jest
projektem otwartym. Inni u�ytkownicy i programi�ci mog� partycypowa�
przy tworzeniu, ulepszaniu, a tak�e jego testowaniu. Celem tego
projektu jest stworzenie niezawodnego i szybkiego procesora XSLT,
kt�ry b�dzie zgodny z normami W3C oraz dost�pny wszystkim tak, by
ka�dy m�g� go u�y� jako podstaw� wieloplatformowych system�w
rozpowszechniania danych w standardzie XML.

%description -l pt_BR
Salotron � um processador XSL implementado em C++.

%package devel
Summary:	%{name} header files
Summary(es):	Archivos de inclusi�n del sablotron
Summary(pl):	Pliki nag��wkowe %{name}
Summary(pt_BR):	Arquivos de inclus�o do sablotron
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libsablotron0-devel

%description devel
Sablotron header files.

%description devel -l es
Archivos de inclusi�n del %{name}.

%description devel -l pl
Pliki nag��wkowe projektu Sablotron.

%description devel -l pt_BR
Salotron � um processador XSL implementado em C++.

Arquivos de inclus�o do %{name}.

%package static
Summary:	Sablotron static library
Summary(pl):	Biblioteka statyczna Sablotrona
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a biblioteca %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Sablotron static library.

%description static -l es
Bibliotecas est�ticas del %{name}.

%description static -l pl
Biblioteka statyczna projektu Sablotron.

%prep
%setup -q -n Sablot-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f tools/missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
CXX=%{__cc}
export CXXFLAGS CXX
%{?_with_javascript:CPPFLAGS="-I/usr/include/js"}
%configure \
	%{?_with_javascript:--enable-javascript}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README RELEASE doc/misc/{DEBUGGER,NOTES} doc/apidoc/{sablot,sxp}
%if 0%{?_with_javascript:1}
%doc README_JS doc/apidoc/jsdom-ref
%endif
%attr(755,root,root) %{_bindir}/sabcmd
%attr(755,root,root) %{_libdir}/libsablot.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sablot-config
%attr(755,root,root) %{_libdir}/libs*.so
%{_libdir}/libs*.la
%{_includedir}/s*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
