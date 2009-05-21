%define module   AuthCAS
%define version    1.3
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Client library for CAS 2.0 authentication server
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module//%{module}-%{version}.tar.gz
Patch:      AuthCAS-1.3-workaround-stricture.patch
BuildRequires: perl-devel
BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(LWP::UserAgent)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
AuthCAS aims at providing a Perl API to Yale's Central Authentication
System (CAS). Only a basic Perl library is provided with CAS whereas
AuthCAS is a full object-oriented library.

%prep
%setup -q -n %{module}-%{version} 
%patch -p 1
rm -f t/pod-coverage.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


