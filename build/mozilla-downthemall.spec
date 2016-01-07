#Firefox globals
%global moz_extensions %{_datadir}/mozilla/extensions
%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}

#Addon
%global src_ext_id \{DDC359D1-844A-42a7-9AA1-88A850A938A8\}
%global inst_dir %{moz_extensions}/%{firefox_app_id}/%{src_ext_id}
%global firefox_inst_dir %{moz_extensions}/%{firefox_app_id}

Name:           mozilla-downthemall
Version:        2.0.18
Release:        1%{?dist}
Summary:        The first and only download manager/accelerator built inside Firefox

Group:          Applications/Internet
License:        GPLv2
URL:            https://addons.mozilla.org/en-US/firefox/addon/downthemall/
Source0:        https://addons.cdn.mozilla.net/user-media/addons/201/downthemall-%{version}-sm+fx.xpi
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
DownThemAll is all you can desire from a download manager: it features an
advanced accelerator that increases speed up to 4x and it allows you to pause
and resume downloads at any time.

%prep
#%setup -q -c

%build
rm -rf %{buildroot}

mkdir -p %{buildroot}%{moz_extensions}/%{firefox_app_id}
install -Dp -m 644 %{SOURCE0} %{buildroot}%{inst_dir}.xpi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{inst_dir}.xpi

%changelog
* Thu Jan 7 2016 Chris Smart <csmart@kororaproject.org>- 2.0.18-1
- Upstream 2.0.18 release.
- Use signed mozilla xpi so that it works with Firefox 43

* Sat Jul 26 2014 Ian Firns <firnsy@kororaproject.org>- 2.0.17-1
- Upstream 2.0.17 release.
- Re-wrapped description.

* Sun Jun 16 2013 Chris Smart <csmart@kororaproject.org>- 2.0.16-1
- Upstream 2.0.16 release.

* Tue Jan 15 2013 Chris Smart <chris@kororaa.org>- 2.0.15-1
- Upstream 2.0.15 release.

* Wed Sep 12 2012 Chris Smart <chris@kororaa.org>- 2.0.14-1
- Upstream 2.0.14 release.

* Sat Feb 16 2012 Chris Smart <chris@kororaa.org>- 2.0.13-1
- Upstream 2.0.13 release.

* Wed Sep 12 2011 Chris Smart <chris@kororaa.org>- 2.0.8-1
- Upstream release, Firefox 8 compatible.

* Sat Sep 10 2011 Chris Smart <chris@kororaa.org>- 2.0.7-1
- Initial port.
