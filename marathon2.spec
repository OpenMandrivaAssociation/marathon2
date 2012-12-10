%define		oname		Marathon2
%define		oversion	20120128

Name:		marathon2
Version:	1.0.1
Release:	2
Summary:	3D first-person shooter game
License:	GPL
Group:		Games/Arcade
Source0:	%{oname}-%{oversion}-Data.zip
URL:		http://sourceforge.net/projects/marathon/
Requires:	alephone
BuildArch:	noarch

%description
Marathon 2: Durandal is the first sequel in the Marathon series of science
fiction first-person shooter computer games from Bungie Software. It was
released on November 24, 1995. The game is mostly set on the fictional planet
of Lh'owon, homeworld of the S'pht, and once again the player takes the role
of a Security Officer from the Marathon.

Just prior to its acquisition by Microsoft in 2000, Bungie released the source
code to the Marathon 2 engine, and the Marathon Open Source project began,
resulting in the new Marathon engine called Aleph One. Since then, the fan
community has made improvements that feature OpenGL-based, high-resolution
graphics, support for Lua, a slew of internal structural changes allowing for
more advanced 3rd party mods, and Internet-capable TCP/IP-based multiplayer.

While the fundamental technology underlying the Marathon engine is still
considered rather outdated by today's standards, Aleph One has added
significant improvements and a more modern polish to its capabilities and
ported it to a wide variety of platforms, bringing Marathon and its derivatives
far beyond their Mac roots.

%prep
%setup -q -n Marathon\ 2

%build

%install
mkdir -p %{buildroot}%{_gamesdatadir}/AlephOne/%{name}
cp -r * %{buildroot}%{_gamesdatadir}/AlephOne/%{name}/

mkdir -p %{buildroot}%{_gamesbindir}
cat > %{buildroot}%{_gamesbindir}/%{name} << EOF
#!/bin/bash

alephone %{_gamesdatadir}/AlephOne/%{name}/
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Marathon 2
Comment=3D first-person shooter
Exec=%{name}
Icon=/usr/share/pixmaps/marathon.png
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamesbindir}/%{name}
%{_gamesdatadir}/AlephOne/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Mon Apr 02 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.1-1
+ Revision: 788624
- imported package marathon2

