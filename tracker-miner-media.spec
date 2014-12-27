Summary:	Attempt to extract information from movies
Summary(pl.UTF-8):	Próba wydobywania informacji z filmów
Name:		tracker-miner-media
Version:	0.1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tracker-miner-media/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	38ef13cd88432183ac5fdd1871029b3f
URL:		http://www.gnome.org/
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgdata-devel >= 0.17
BuildRequires:	pkgconfig
BuildRequires:	tracker-devel >= 1.0
Requires:	libgdata >= 0.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Attempt to extract information from movies.

%description -l pl.UTF-8
Próba wydobywania informacji z filmów.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libexecdir}/tracker-miner-media
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Media.service
%{_datadir}/tracker/miners/tracker-miner-media.desktop
