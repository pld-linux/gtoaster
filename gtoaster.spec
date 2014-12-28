#
# Conditional build:
%bcond_with	gnome		# build with GNOME1 support
#
Summary:	A GNOME frontend for cdrecord
Summary(pl.UTF-8):	Nakładka GNOME na program cdrecord
Name:		gtoaster
Version:	1.0Beta6
Release:	7
Epoch:		1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://gnometoaster.rulez.org/archive/%{name}%{version}.tgz
# Source0-md5:	89256dbb2bedfbc44337aa6980e6fb93
Source1:	%{name}.desktop
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-pofix.patch
Patch2:		%{name}-po-fix.patch
Patch3:		%{name}-locale_names.patch
Patch4:		%{name}-po-filetype.patch
URL:		http://gnometoaster.rulez.org/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-tools
%{?with_gnome:BuildRequires:	gnome-libs-devel >= 1.0.54}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Toaster is a CD creation suite for the famous Linux operating
System. Thought to be as user-friendly as possible it lets you create
CD recordables with just a few simple mouse clicks. Create your CDs by
simply dragging the desired contents onto it's display window.

%description -l pl.UTF-8
GNOME Toaster pozwala w wyjątkowo prosty sposób na tworzenie płyt CD-R
za pomocą kilku kliknięć. Tworzenie zawartości płyty odbywa się za
pomocą przeciągania i upuszczania plików, katalogów w oknie programu.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv -f po/{no,nb}.po

%build
rm -f missing
#%%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gnome:--without-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install icons/gtoaster.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/gtoaster.desktop
%{_pixmapsdir}/*
