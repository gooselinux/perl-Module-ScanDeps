Name:           perl-Module-ScanDeps
Version:        0.95
Release:        2%{?dist}
Summary:        Recursively scan Perl code for dependencies
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-ScanDeps/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/Module-ScanDeps-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Module::Build::ModuleInfo)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(prefork)
BuildRequires:  perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module scans potential modules used by perl programs and returns a
hash reference.  Its keys are the module names as appears in %INC (e.g.
Test/More.pm).  The values are hash references.

%prep
%setup -q -n Module-ScanDeps-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.95-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.95-1
- auto-update to 0.95 (by cpan-spec-update 0.01)
- add perl_default_filter (pro forma)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Steven Pritchard <steve@kspei.com> 0.89-1
- Update to 0.89.
- BR Test::More and prefork.
- Improve description.

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 0.84-1
- Update to 0.84.

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.82-2
- rebuild for new perl

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 0.82-1
- Update to 0.82.
- BR version.

* Thu Jan 24 2008 Steven Pritchard <steve@kspei.com> 0.81-1
- Update to 0.81.
- Use fixperms macro instead of our own chmod incantation.
- Reformat to match cpanspec output.
- BR ExtUtils::MakeMaker.

* Wed Jun 27 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.75-1
- Update to 0.75.

* Sat May  5 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.74-1
- Update to 0.74.

* Sat Mar 31 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.73-1
- Update to 0.73.

* Sun Feb  4 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.72-1
- Update to 0.72.
- Added perl(Module::Pluggable) to the build requirements list (t/2-pluggable.t).

* Fri Jan  5 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.71-1
- Update to 0.71.

* Wed Nov 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.70-1
- Update to 0.70.

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.69-1
- Update to 0.69.

* Sat Oct 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.68-1
- Update to 0.68.

* Sun Sep 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.66-1
- Update to 0.66.

* Sat Sep 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.64-1
- Update to 0.64.

* Mon Sep  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.63-1
- Update to 0.63.

* Sun Jul 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.62-1
- Update to 0.62.

* Sat Jul  1 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.61-1
- Update to 0.61.

* Wed May 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.60-1
- Update to 0.60.

* Sun May  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.59-2
- Source URL corrected (failed to detect the maintainer change).

* Wed May  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.59-1
- Update to 0.59.

* Thu Mar 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.57-1
- Update to 0.57.

* Tue Feb 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.56-1
- Update to 0.56.

* Tue Jan 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.53-1
- Update to 0.53.

* Fri Sep  9 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.51-1
- Update to Fedora Extras Template.

* Sat Jan 08 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.51-0.fdr.1
- First build.
