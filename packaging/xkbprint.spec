Name:           xkbprint
Version:        1.0.3
Release:        1
License:        MIT
Summary:        Utility to print an XKB keyboard description
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3

%description
xkbprint generates a printable or encapsulated PostScript description
of an XKB keyboard description.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%docs_package

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/xkbprint

%changelog
