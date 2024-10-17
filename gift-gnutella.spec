%define name    gift-gnutella
%define version 0.0.11
%define rel	1

Summary:        Gnutella plugin for giFT
Name:           %{name}
Version:        %{version}
Release:        %mkrel %{rel}
License:        GPL
Group:          Networking/File transfer
URL:            https://gift.sf.net/
Source0:        %{name}-%{version}.tar.bz2
Requires:	gift
BuildRequires:	db4-devel
BuildRequires:	gift-devel
BuildRequires:	libxml2-devel
BuildRequires:	magic-devel
BuildRequires:	zlib-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Gnutella network plugin for giFT file transfer.

%prep
%setup -q

%build
%configure2_5x --with-libxml
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README NEWS TODO
%{_datadir}/giFT/Gnutella
%{_libdir}/giFT/*

