Name:           sigma-release
Version:        5
Release:        1%{?dist}
Summary:        Sigma repository configuration

Packager:       Eugene Zamriy <eugene@zamriy.info>
License:        GPLv2

Group:          System Environment/Base
URL:            http://sigmarepo.zamriy.info/

Source0:        http://sigmarepo.zamriy.info/repo/RPM-GPG-KEY-SIGMA-5
Source1:        sigma.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

Requires:       redhat-release >= %{version}
Requires:       epel-release >= %{version}
Conflicts:      fedora-release


%description
This package contains the Sigma repository GPG key and configuration for yum.


%prep
%setup -q -c -T
%{__install} -pm 644 %{SOURCE0} .

%build


%install
%{__rm} -rf %{buildroot}
%{__install} -Dpm 644 %{SOURCE0} \
             %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-SIGMA-5
%{__install} -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
%{__install} -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Sun Feb 14 2016 Eugene Zamriy <eugene@zamriy.info> - 5-1
- initial release
