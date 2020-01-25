%define		_class		Gtk
%define		_subclass	MDB
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Designer
Summary:	%{_pearname} - an GTK+ Database schema designer
Summary(pl.UTF-8):	%{_pearname} - oparty na GTK+ projektant schematów baz danych
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	10
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	65bb0042a2476d19c8300c1479ebc63e
URL:		http://pear.php.net/package/Gtk_MDB_Designer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gtk)
Requires:	php-common >= 3:4.3
Requires:	php-pear >= 4:1.0-8
Requires:	php-pear-MDB >= 1:1.1.1
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
- support for NotNull, Indexes, Sequences, Unique Indexes and defaults
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

%description -l pl.UTF-8
Graficzny projektant schematów baz danych, luźnie oparty na schemacie
MDB, pozwalający na:
- przeciąganie prostokątów tabel po oknie
- dodawanie/usuwanie tabel
- dodawanie/usuwanie kolumn
- obsługę atrybutów NotNull, indeksów, sekwencji, unikalnych indeksów
  i domyślnych
- działanie w trybie bez połączenia (nie wymagającym bezy danych ani
  konfiguracji)
- zapis do pliku XML w stylu MDB
- zapis do plików tworzących tabele SQL w dowolnej obsługiwanej bazie.

Zrzuty ekranu dostępne są pod http://devel.akbkhome.com/Gtk_MDB/.

Przyszłe rozszerzenia:
- prawdziwe eksportowanie schematów MDB
- zależności = z liniami itp.

Głównym celem jest generowanie plików SQL (co pozwoli autorowi
wykonywać swoją pracę), ale opcjonalnie planowana jest pełna obsługa
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
