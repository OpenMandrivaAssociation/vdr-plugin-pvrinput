
%define plugin	pvrinput
%define name	vdr-plugin-%plugin
%define oversion 2010-04-14
%define version	%(echo %oversion | tr - .)
%define rel	1

Summary:	VDR plugin: use Hauppauge PVR as input device
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
# otherwise GPL+, but menu.c contains GPLv2+ making this GPLv2+ as a whole
License:	GPLv2+
URL:		https://projects.vdr-developer.org/projects/show/plg-pvrinput
Source:		vdr-%plugin-%oversion.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin uses a Hauppauge PVR card as an input device. All cards
supported by the ivtv driver should work. This version of the plugin
requires ivtv driver version 0.8 or higher.

%prep
%setup -q -n %plugin-%oversion
%vdr_plugin_prep

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
%doc README HISTORY TODO example 
