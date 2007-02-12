Summary:	XSL Transformations Processor
Summary(pl.UTF-8):   Procesor Transformacji XSL
Summary(pt_BR.UTF-8):   Processador de XSL
Name:		sablotron
Version:	0.90
Release:	1
License:	Mozilla Public License Version 1.1 or GPL
Group:		Applications/Publishing/XML
Source0:	http://download.gingerall.cz/sablot/Sablot-%{version}.tar.gz
Source1:	sablot_man.html
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-am15.patch
Patch2:		%{name}-expat.patch
URL:		http://www.gingerall.com/charlie-bin/get/webGA/act/sablotron.act
BuildRequires:	autoconf
BuildRequires:	automake
Buildrequires:	expat-devel >= 1.95.1
BuildRequires:	libtool
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

%description -l pl.UTF-8
Sablotron jest próbą stworzenia szybkiego, małego i przenośnego
procesora XSLT. Potrzebowaliśmy takiego procesora dla projektu
Charlie, więc zdecydowaliśmy się stworzyć odpowiedni. Sablotron jest
projektem otwartym. Inni użytkownicy i programiści mogą partycypować
przy tworzeniu, ulepszaniu, a także jego testowaniu. Celem tego
projektu jest stworzenie niezawodnego i szybkiego procesora XSLT,
który będzie zgodny z normami W3C oraz dostępny wszystkim, tak, by
każdy mógł go użyć jako podstawę wieloplatformowych systemów
rozpowszechniania danych w standardzie XML.

%description -l pt_BR.UTF-8
Salotron é um processador XSL implementado em C++.

%package devel
Summary:	%{name} header files
Summary(es.UTF-8):   Archivos de inclusión del sablotron
Summary(pl.UTF-8):   Pliki nagłówkowe %{name}
Summary(pt_BR.UTF-8):   Arquivos de inclusão do sablotron
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libsablotron0-devel

%description devel
Sablotron header files.

%description devel -l es.UTF-8
Archivos de inclusión del %{name}.

%description devel -l pl.UTF-8
Pliki nagłówkowe projektu Sablotron.

%description devel -l pt_BR.UTF-8
Salotron é um processador XSL implementado em C++.

Arquivos de inclusão do %{name}.

%package static
Summary:	Sablotron static library
Summary(es.UTF-8):   %{name} static libs
Summary(pl.UTF-8):   Biblioteka statyczna Sablotrona
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com a biblioteca %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Sablotron static library.

%description static -l es.UTF-8
Bibliotecas estáticas del %{name}.

%description static -l pl.UTF-8
Bioblioteka statyczna projektu Sablotron.

%prep
%setup -q -n Sablot-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f tools/missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c --foreign
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"; export CXXFLAGS
CXX=%{__cc}; export CXX
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} .

gzip -9nf README sablot_man.html

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz sablot_man.html*
%attr(755,root,root) %{_bindir}/sabcmd
%attr(755,root,root) %{_libdir}/libsablot.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libs*.so
%attr(755,root,root) %{_libdir}/libs*.la
%{_includedir}/s*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
