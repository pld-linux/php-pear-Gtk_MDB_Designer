# Todo:
# - pl description
%include	/usr/lib/rpm/macros.php
%define         _class          Gtk_MDB
%define         _subclass       Designer
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - An Gtk Database schema designer
Summary(pl):	%{_pearname} - Projektant schemat bazy (GTK)
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	0.1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	65bb0042a2476d19c8300c1479ebc63e
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-gtk
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A graphical database schema designer, based loosely around the MDB
schema, it features
- table boxes which are dragged around a window to layout your
  database
- add/delete tables
- add delete columns
- support for NotNull, Indexes, Sequences , Unique Indexes and
  defaults
- works totally in non-connected mode (eg. no database or setting up
  required)

- stores in MDB like xml file.
- saves to any supported database SQL create tables files.
- screenshots at http://devel.akbkhome.com/Gtk_MDB/


Future enhancements:
- real MDB schema exports
- relationships = with lines etc. Note: the primary aim is to generate
  SQL files, (so that I can get my work done) however it is eventually
  planned to support MDB schema's fully.. - just a matter of time..

This class has in PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{,Interface}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.{php,glade} $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Interface/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Interface

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*
