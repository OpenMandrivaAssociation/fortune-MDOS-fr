%define name fortune-MDOS-fr 
%define version 20040104
%define release %mkrel 3

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
Url: http://lordoric.free.fr/fortunes
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


