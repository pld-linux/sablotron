Summary:	XSL Transformations Processor
Summary(pl):	Procesor Transformacji XSL
Summary(pt_BR): Processador de XSL
Name:		sablotron
Version:	0.81
Release:	1
License:	Mozilla Public License Version 1.1 or GPL
Group:		Applications/Publishing/XML
Group(de):	Applikationen/Publizieren/XML
Group(es):	Aplicaciones/EditoraciÛn/XML
Group(pl):	Aplikacje/Publikowanie/XML
Group(pt_BR):	AplicaÁıes/EditoraÁ„o/XML
Source0:	http://download.gingerall.cz/sablot/Sablot-%{version}.tar.gz
Source1:	sablot_man.html
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-am15.patch
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

%description -l pl
Sablotron jest prÛb± stworzenia szybkiego, ma≥ego i przeno∂nego
procesora XSLT. Potrzebowali∂my takiego procesora dla projektu
Charlie, wiÍc zdecydowali∂my siÍ stworzyÊ odpowiedni. Sablotron jest
projektem otwartym. Inni uøytkownicy i programi∂ci mog± partycypowaÊ
przy tworzeniu, ulepszaniu, a takøe jego testowaniu. Celem tego
projektu jest stworzenie niezawodnego i szybkiego procesora XSLT,
ktÛry bÍdzie zgodny z normami W3C oraz dostÍpny wszystkim, tak, by
kaødy mÛg≥ go uøyÊ jako podstawÍ wieloplatformowych systemÛw
rozpowszechniania danych w standardzie XML.

%description -l pt_BR
Salotron È um processador XSL implementado em C++.

%package devel
Summary:	%{name} header files
Summary(es): Archivos de inclusiÛn del sablotron
Summary(pl):	Pliki nag≥Ûwkowe %{name}
Summary(pt_BR): Arquivos de inclus„o do sablotron
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Obsoletes:	libsablotron0-devel

%description devel
Sablotron header files.

%description -l es devel
Archivos de inclusiÛn del %{name}.

%description -l pl devel
Pliki nag≥Ûwkowe projektu Sablotron.

%description -l pt_BR devel
Salotron È um processador XSL implementado em C++.

Arquivos de inclus„o do %{name}.

%package static
Summary:	Sablotron static library
Summary(es): %{name} static libs
Summary(pl):	Biblioteka statyczna Sablotrona
Summary(pt_BR): Bibliotecas est·ticas para desenvolvimento com a biblioteca %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Sablotron static library.

%description -l es static
Bibliotecas est·ticas del %{name}.

%description -l pl static
Bioblioteka statyczna projektu Sablotron.

%prep
%setup -q -n Sablot-%{version}
%patch0 -p1
%patch1 -p1

%build
rm -f tools/missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c --foreign
CXXFLAGS="%{rpmcflags} -DUTF8_ICONV_CAST_OK -fno-rtti -fno-exceptions"; export CXXFLAGS
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
