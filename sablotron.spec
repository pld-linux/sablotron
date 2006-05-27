#
# Conditional build:
%bcond_with	javascript	# enable experimental JavaScript XSLT extension
#
Summary:	XSL Transformations Processor
Summary(pl):	Procesor Transformacji XSL
Summary(pt_BR):	Processador de XSL
Name:		sablotron
Version:	1.0.2
Release:	1
License:	MPL v1.1 or GPL
Group:		Applications/Publishing/XML
#Source0Download:	http://www.gingerall.com/charlie/ga/xml/d_sab.xml
Source0:	http://download-1.gingerall.cz/download/sablot/Sablot-%{version}.tar.gz
# Source0-md5:	12243bc21b149cad89e98bc89f9c103e
Patch0:		%{name}-link.patch
URL:		http://www.gingerall.com/charlie/ga/xml/p_sab.xml
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
BuildRequires:	expat-devel >= 1.95.6-2
%{?with_javascript:BuildRequires:	js-devel}
BuildRequires:	libtool
BuildRequires:	perl-XML-Parser
Obsoletes:	libsablotron0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Sablotron jest prób± stworzenia szybkiego, ma³ego i przeno¶nego
procesora XSLT. Potrzebowali¶my takiego procesora dla projektu
Charlie, wiêc zdecydowali¶my siê stworzyæ odpowiedni. Sablotron jest
projektem otwartym. Inni u¿ytkownicy i programi¶ci mog± partycypowaæ
przy tworzeniu, ulepszaniu, a tak¿e jego testowaniu. Celem tego
projektu jest stworzenie niezawodnego i szybkiego procesora XSLT,
który bêdzie zgodny z normami W3C oraz dostêpny wszystkim tak, by
ka¿dy móg³ go u¿yæ jako podstawê wieloplatformowych systemów
rozpowszechniania danych w standardzie XML.

%description -l pt_BR
Salotron é um processador XSL implementado em C++.

%package devel
Summary:	Header files for sablotron library
Summary(es):	Archivos de inclusión del sablotron
Summary(pl):	Pliki nag³ówkowe biblioteki sablotron
Summary(pt_BR):	Arquivos de inclusão do sablotron
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1.95.6-2
%{?with_javascript:Requires:	js-devel}
Requires:	libstdc++-devel
Obsoletes:	libsablotron0-devel

%description devel
Sablotron header files.

%description devel -l es
Archivos de inclusión del sablotron.

%description devel -l pl
Pliki nag³ówkowe projektu Sablotron.

%description devel -l pt_BR
Salotron é um processador XSL implementado em C++.

Arquivos de inclusão do sablotron.

%package static
Summary:	Sablotron static library
Summary(pl):	Biblioteka statyczna Sablotrona
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com a biblioteca sablotron
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Sablotron static library.

%description static -l es
Bibliotecas estáticas del sablotron.

%description static -l pl
Biblioteka statyczna projektu Sablotron.

%prep
%setup -q -n Sablot-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%{?with_javascript:CPPFLAGS="-I/usr/include/js"}
%configure \
	%{?with_javascript:--with-js}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/doc/html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README RELEASE doc/misc/{DEBUGGER,NOTES} %{?with_javascript:README_JS}
%attr(755,root,root) %{_bindir}/sabcmd
%attr(755,root,root) %{_libdir}/libsablot.so.*.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/apidoc/{sablot,sxp} %{?with_javascript:doc/apidoc/jsdom-ref}
%attr(755,root,root) %{_bindir}/sablot-config
%attr(755,root,root) %{_libdir}/libsablot.so
%{_libdir}/libsablot.la
%{_includedir}/s*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsablot.a
