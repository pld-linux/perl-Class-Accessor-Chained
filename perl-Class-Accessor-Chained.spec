#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Accessor-Chained
Summary:	Class::Accessor::Chained - make chained accessors
Summary(pl):	Class::Accessor::Chained - tworzenie ³añcuchowych metod accessor
Name:		perl-Class-Accessor-Chained
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9825a1f30a70e55e61bb5660b2bd7365
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A chained accessor is one that always returns the object when called
with parameters (to set), and the value of the field when called with
no arguments.

This module subclasses Class::Accessor in order to provide the same
mk_accessors interface.

%description -l pl
£añcuchowa metoda accessor to taka, która zawsze zwraca obiekt przy
wywo³aniu z parametrami (do ustawienia), a warto¶æ pola przy wywo³aniu
bez parametrów.

Ten modu³ jest podklas± Class::Accessor dla zapewnienia tego samego
interfejsu mk_accessors.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/Accessor/*.pm
%{perl_vendorlib}/Class/Accessor/Chained
%{_mandir}/man3/*
