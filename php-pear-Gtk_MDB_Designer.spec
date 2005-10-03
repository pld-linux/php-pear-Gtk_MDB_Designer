%include	/usr/lib/rpm/macros.php
%define		_class		Gtk
%define		_subclass	MDB
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Designer

Summary:	%{_pearname} - an GTK+ Database schema designer
Summary(pl):	%{_pearname} - oparty na GTK+ projektant schematów baz danych
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	5.3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	65bb0042a2476d19c8300c1479ebc63e
URL:		http://pear.php.net/package/Gtk_MDB_Designer/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php4-gtk
Requires:	php-common >= 3:4.3
Requires:	php-pear >= 4:1.0-8
Requires:	php-pear-MDB >= 1.1.1
Requires:	php-pear-XML_Parser >= 1.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A graphical database schema designer, based loosely around the MDB
schema, it features:
- table boxes which are dragged around a window to layout your
  database
- add/delete tables
- add/delete columns
- support for NotNull, Indexes, Sequences, Unique Indexes and
  defaults
- works totally in non-connected mode (eg. no database or setting up
  required)
- stores in MDB like xml file
- saves to any supported database SQL create tables files
- screenshots at http://devel.akbkhome.com/Gtk_MDB/.

Future enhancements:
- real MDB schema exports
- relationships = with lines etc.

Note: the primary aim is to generate SQL files, (so that I can get my
work done) however it is eventually planned to support MDB schemas
fully... - just a matter of time.

In PEAR status of this package is: %{_status}.

%description -l pl
Graficzny projektant schematów baz danych, lu¼nie oparty na schemacie
MDB, pozwalaj±cy na:
- przeci±ganie prostok±tów tabel po oknie
- dodawanie/usuwanie tabel
- dodawanie/usuwanie kolumn
- obs³ugê atrybutów NotNull, indeksów, sekwencji, unikalnych indeksów
  i domy¶lnych
- dzia³anie w trybie bez po³±czenia (nie wymagaj±cym bezy danych ani
  konfiguracji)
- zapis do pliku XML w stylu MDB
- zapis do plików tworz±cych tabele SQL w dowolnej obs³ugiwanej bazie.

Zrzuty ekranu dostêpne s± pod http://devel.akbkhome.com/Gtk_MDB/.

Przysz³e rozszerzenia:
- prawdziwe eksportowanie schematów MDB
- zale¿no¶ci = z liniami itp.

G³ównym celem jest generowanie plików SQL (co pozwoli autorowi
wykonywaæ swoj± pracê), ale opcjonalnie planowana jest pe³na obs³uga
schematów MDB... - to tylko kwestia czasu.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}/Designer.php
%{php_pear_dir}/%{_class}/%{_subclass}/Designer
