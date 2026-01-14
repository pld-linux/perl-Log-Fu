#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Log
%define		pnam	Fu
Summary:	Log::Fu - Simplified and developer-friendly screen logging
Summary(pl.UTF-8):	Log::Fu - uproszczone i przyjazne dla programistów logowanie na ekranie
Name:		perl-Log-Fu
Version:	0.31
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Log/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	28354f432e52e5d9b4553259da920068
URL:		http://search.cpan.org/dist/Log-Fu/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Constant-Generate >= 0.04
BuildRequires:	perl-Dir-Self
BuildRequires:	perl-Test-Simple
%endif
Requires:	perl-Constant-Generate >= 0.04
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple interface for console logging. It provides a few
functions, log_info, log_debug, log_warn, log_crit, and log_err. They
all take strings as arguments, and can take as many arguments as you
so desire (so any concatenation is done for you).

A message is printed to standard error (or to $target if specified),
prefixed with the filename, line number, and originating subroutine of
the message.

%description -l pl.UTF-8
Ten moduł to prosty interfejs do logowania na konsoli. Udostępnia
kilka funkcji: log_info, log_debug, log_warn, log_crit i log_err.
Wszystkie jako argumenty przyjmują łańcuchy w dowolnej liczbie
(łączenie ich jest wykonywane za programistę).

Komunikat jest wypisywany na standardowe wyjście diagnostyczne (lub
$target, jeśli został podany) i jest poprzedzany nazwą pliku, numerem
linii i procedurą, z której pochodzi komunikat.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/Fu.pm
%{perl_vendorlib}/Log/Fu
%{_mandir}/man3/Log::Fu.3pm*
