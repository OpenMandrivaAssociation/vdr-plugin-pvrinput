
%define plugin	pvrinput
%define name	vdr-plugin-%plugin
%define version	0.1.1
%define rel	8

Summary:	VDR plugin: use Hauppauge PVR as input device
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://home.arcor.de/andreas.regel/files/pvrinput/
Source:		http://home.arcor.de/andreas.regel/files/pvrinput/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This plugin uses a Hauppauge PVR card as an input device. All cards
supported by the ivtv driver should work. You should have ivtv
version 0.4.0 or newer installed with the encoder firmware.

%prep
%setup -q -n %plugin-%version

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY TODO example/channels.conf.example


