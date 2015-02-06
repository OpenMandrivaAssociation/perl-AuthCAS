%define upstream_name    AuthCAS
%define upstream_version 1.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Client library for CAS 2.0 authentication server
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/O/OS/OSALAUN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(LWP::UserAgent)
BuildArch:	noarch

%description
AuthCAS aims at providing a Perl API to Yale's Central Authentication
System (CAS). Only a basic Perl library is provided with CAS whereas
AuthCAS is a full object-oriented library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm -f t/pod-coverage.t

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.400.0-2mdv2011.0
+ Revision: 654876
- rebuild for updated spec-helper

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2011.0
+ Revision: 395063
- update to 1.4
- using %%perl_convert_version
- fixed license field

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-1mdv2010.0
+ Revision: 378430
- new version
- import perl-AuthCAS


* Thu May 21 2009 cpan2dist 1.3-1mdv
- initial mdv release, generated with cpan2dist

