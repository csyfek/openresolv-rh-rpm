Summary:   Management framework for resolv.conf
Name:      openresolv
Version:   3.4.1
Release:   1%{?dist}
License:   BSD
Group:     System Environment/Base
URL:       http://roy.marples.name/projects/openresolv
Source0:   http://roy.marples.name/downloads/openresolv/openresolv-%{version}.tar.bz2
BuildArch: noarch

Patch0:    openresolv-service-status-quiet.patch

%description
Allows multiple daemons to manage resolv.conf and configures
local resolvers such as dnsmasq and unbound.
Please read resolvconf(8) and resolvconf.conf(5) for detailed instructions.

%prep
%setup -q

%patch0 -p1 -b .service-status-quiet

%build
%configure --sbindir=/sbin
make

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%config(noreplace) %{_sysconfdir}/resolvconf.conf
%attr(0755,root,root) %{_libexecdir}/resolvconf/dnsmasq
%attr(0755,root,root) %{_libexecdir}/resolvconf/libc
%attr(0755,root,root) %{_libexecdir}/resolvconf/named
%attr(0755,root,root) %{_libexecdir}/resolvconf/pdnsd
%attr(0755,root,root) %{_libexecdir}/resolvconf/unbound
%attr(0755,root,root) /sbin/resolvconf
%{_mandir}/man5/resolvconf.conf.5.gz
%{_mandir}/man8/resolvconf.8.gz


%changelog

* Mon Jan 03 2011  Jiri Popelka <jpopelka@redhat.com> - 3.4.1-1
- Initial srpm.
