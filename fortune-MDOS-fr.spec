%define name fortune-MDOS-fr 
%define version 20040104
%define release 8

Summary: The best of Jayce about MultiDeskOS
Summary(fr): Le meilleur de Jayce à propos de MultiDeskOS 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: multidesk.tar.bz2
License: Public Domain
Group: Toys
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Url: https://lordoric.free.fr/fortunes
BuildRequires: fortune-mod
Requires: fortune-mod locales-fr

%description -l fr
Le meilleur de la liste de discussion de MultideskOS et de la documentation
de ce système (?) d'avenir.
 
%description 
Best of MultideskOS' ML and documentation. In French.

%prep
%setup -c 

%build
sed -i 's/\r//g' multidesk
cat multidesk2 >> multidesk
%{_sbindir}/strfile multidesk

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_datadir/games/fortunes/fr/
cp multidesk multidesk.dat $RPM_BUILD_ROOT/%_datadir/games/fortunes/fr/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc multidesk.licence
%_datadir/games/fortunes/fr/multidesk*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20040104-7mdv2011.0
+ Revision: 618314
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 20040104-6mdv2010.0
+ Revision: 428879
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20040104-5mdv2009.0
+ Revision: 245327
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 20040104-3mdv2008.1
+ Revision: 136417
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Feb 25 2007 Olivier Thauvin <nanardon@mandriva.org> 20040104-3mdv2007.0
+ Revision: 125584
- rebuild
- Import fortune-MDOS-fr

* Sat Apr 29 2006 Pascal Terjan <pterjan@mandriva.org> 20040104-2mdk
- mkrel

* Sat Aug 14 2004 Pascal Terjan <pterjan@mandrake.org> 20040104-1mdk
- 20040104

