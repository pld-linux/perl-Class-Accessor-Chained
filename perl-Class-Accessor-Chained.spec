#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Accessor-Chained
Summary:	Class::Accessor::Chained - make chained accessors
Summary(pl.UTF-8):	Class::Accessor::Chained - tworzenie łańcuchowych metod accessor
Name:		perl-Class-Accessor-Chained
Version:	0.01
Release:	2
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

%description -l pl.UTF-8
Łańcuchowa metoda accessor to taka, która zawsze zwraca obiekt przy
wywołaniu z parametrami (do ustawienia), a wartość pola przy wywołaniu
bez parametrów.

Ten moduł jest podklasą Class::Accessor dla zapewnienia tego samego
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
