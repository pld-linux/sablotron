%define aname	Sablot
Summary:	XSL Transformations Processor
Summary(pl):	Procesor Transformacji XSL
Name:		sablotron
Version:	0.60
Release:	2
License:	Mozilla Public License Version 1.1 or GPL
Group:		Applications/Publishing/XML
Group(de):	Applikationen/Publizieren/XML
Group(pl):	Aplikacje/Publikowanie/XML
Source0:	http://download.gingerall.cz/sablot/%{aname}-%{version}.tar.gz
Source1:	sablot_man.html
URL:		http://www.gingerall.com/charlie-bin/get/webGA/act/sablotron.act
Buildrequires:	libstdc++-devel
Buildrequires:	expat-devel >= 1.95.1
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
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
który bêdzie zgodny z normami W3C oraz dostêpny wszystkim, tak, by
ka¿dy móg³ go u¿yæ jako podstawê wieloplatformowych systemów
rozpowszechniania danych w standardzie XML.

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Sablotron header files.

%description -l pl devel
Pliki nag³ówkowe projektu Sablotron.

%package static
Summary:	Sablotron static library
Summary(pl):	Biblioteka statyczna Sablotrona
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Sablotron static library.

%description -l pl static
Bioblioteka statyczna projektu Sablotron.

%prep
%setup -q -n %{aname}-%{version}

%build
rm tools/missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c --foreign
CXXFLAGS="%{rpmcflags} -DUTF8_ICONV_CAST_OK"; export CXXFLAGS
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
%{_includedir}/s*
%attr(755,root,root) %{_libdir}/libsablot.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
