Summary:	A GNOME frontend for cdrecord
Summary(pl):	Nak³adka GNOME na program cdrecord
Name:		gtoaster
Version:	1.0Beta6
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://gnometoaster.rulez.org/archive/%{name}%{version}.tgz
# Source0-md5: 89256dbb2bedfbc44337aa6980e6fb93
Source1:	%{name}.desktop
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-pofix.patch
URL:		http://gnometoaster.rulez.org/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.54
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome Toaster is a cd creation suite for the famous Linux operating
System. Thought to be as user-friendly as possible it lets you create
cd recordables with just a few simple mouse clicks. Create your CDs by
simply dragging the desired contents onto it's display window.

%description -l pl
Gnome Toaster pozwala w wyj±tkowo prosty sposób na tworzenie p³yt CD-R
za pomoc± kilku klikniêæ. Tworzenie zawarto¶ci p³yty odbywa siê za
pomoc± przeci±gania i upuszczania plików, katalogów w oknie programu.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
rm -f missing
#%%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir} \
        $RPM_BUILD_ROOT%{_applnkdir}/Utilities/CD-RW

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install icons/gtoaster.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities/CD-RW

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc  README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/CD-RW/gtoaster.desktop
%{_pixmapsdir}/*
