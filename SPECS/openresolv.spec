Summary:   Management framework for resolv.conf
Name:      openresolv
Version:   3.9.0
Release:   1%{?dist}
License:   BSD
Group:     System Environment/Base
URL:       http://roy.marples.name/projects/openresolv
Source0:   http://roy.marples.name/downloads/openresolv/openresolv-%{version}.tar.xz
BuildArch: noarch

%description
Allows multiple daemons to manage resolv.conf and configures
local resolvers such as dnsmasq and unbound.
Please read resolvconf(8) and resolvconf.conf(5) for detailed instructions.

Be sure to stop NetworkManager before you use openresolv, refer to
 * https://bugzilla.redhat.com/show_bug.cgi?id=668153
for the reason.

%prep
%setup -q

%build
%configure \
  --sbindir=%{_sbindir} \
  --libexecdir=%{_libexecdir}/resolvconf
make

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%config(noreplace) %{_sysconfdir}/resolvconf.conf
%dir %{_libexecdir}/resolvconf
%attr(0755,root,root) %{_libexecdir}/resolvconf/dnsmasq
%attr(0755,root,root) %{_libexecdir}/resolvconf/libc
%attr(0755,root,root) %{_libexecdir}/resolvconf/named
%attr(0755,root,root) %{_libexecdir}/resolvconf/pdnsd
%attr(0755,root,root) %{_libexecdir}/resolvconf/unbound
%attr(0755,root,root) %{_sbindir}/resolvconf
%{_mandir}/man5/resolvconf.conf.5.gz
%{_mandir}/man8/resolvconf.8.gz


%changelog
* Wed Mar 01 2017  Flos Guo <qguo@redhat.com> - 3.9.0-1
- Bump to new version.
- Update description.

* Fri Jan 21 2011  Jiri Popelka <jpopelka@redhat.com> - 3.4.1-2
- Package review fixes (#668153).

* Mon Jan 03 2011  Jiri Popelka <jpopelka@redhat.com> - 3.4.1-1
- Initial srpm.
