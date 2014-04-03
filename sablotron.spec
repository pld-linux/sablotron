#
# Conditional build:
%bcond_with	javascript	# enable experimental JavaScript XSLT extension

Summary:	XSL Transformations Processor
Summary(pl.UTF-8):	Procesor Transformacji XSL
Summary(pt_BR.UTF-8):	Processador de XSL
Name:		sablotron
Version:	1.0.3
Release:	3
License:	MPL v1.1 or GPL
Group:		Applications/Publishing/XML
#Source0Download:	http://www.gingerall.org/downloads.html
Source0:	http://download-1.gingerall.cz/download/sablot/Sablot-%{version}.tar.gz
# Source0-md5:	72654c4b832e7562f8240ea675577f5e
Patch0:		%{name}-link.patch
URL:		http://www.gingerall.org/sablotron.html
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

%description -l pl.UTF-8
Sablotron jest próbą stworzenia szybkiego, małego i przenośnego
procesora XSLT. Potrzebowaliśmy takiego procesora dla projektu
Charlie, więc zdecydowaliśmy się stworzyć odpowiedni. Sablotron jest
projektem otwartym. Inni użytkownicy i programiści mogą partycypować
przy tworzeniu, ulepszaniu, a także jego testowaniu. Celem tego
projektu jest stworzenie niezawodnego i szybkiego procesora XSLT,
który będzie zgodny z normami W3C oraz dostępny wszystkim tak, by
każdy mógł go użyć jako podstawę wieloplatformowych systemów
rozpowszechniania danych w standardzie XML.

%description -l pt_BR.UTF-8
Salotron é um processador XSL implementado em C++.

%package apidocs
Summary:	Sablotron API documetation
Summary(pl.UTF-8):	Dokumentacja API Sablotron
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Sablotron API documetation.

%description apidocs -l pl.UTF-8
Dokumentacja API Sablotron.

%package devel
Summary:	Header files for sablotron library
Summary(es.UTF-8):	Archivos de inclusión del sablotron
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sablotron
Summary(pt_BR.UTF-8):	Arquivos de inclusão do sablotron
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1.95.6-2
%{?with_javascript:Requires: js-devel}
Requires:	libstdc++-devel
Obsoletes:	libsablotron0-devel

%description devel
Sablotron header files.

%description devel -l es.UTF-8
Archivos de inclusión del sablotron.

%description devel -l pl.UTF-8
Pliki nagłówkowe projektu Sablotron.

%description devel -l pt_BR.UTF-8
Salotron é um processador XSL implementado em C++.

Arquivos de inclusão do sablotron.

%package static
Summary:	Sablotron static library
Summary(pl.UTF-8):	Biblioteka statyczna Sablotrona
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com a biblioteca sablotron
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Sablotron static library.

%description static -l es.UTF-8
Bibliotecas estáticas del sablotron.

%description static -l pl.UTF-8
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

rm -r $RPM_BUILD_ROOT%{_docdir}/html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README RELEASE doc/misc/{DEBUGGER,NOTES} %{?with_javascript:README_JS}
%attr(755,root,root) %{_bindir}/sabcmd
%attr(755,root,root) %{_libdir}/libsablot.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsablot.so.0
%{_mandir}/man1/*

%files apidocs
%defattr(644,root,root,755)
%doc doc/apidoc/{sablot,sxp} %{?with_javascript:doc/apidoc/jsdom-ref}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sablot-config
%attr(755,root,root) %{_libdir}/libsablot.so
%{_libdir}/libsablot.la
%{_includedir}/s*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsablot.a
