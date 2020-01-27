Name:           elperiodic
Version:        1.0.2
Release:        1%{?dist}
Summary:        ElPeriodic Library

License:        BSD2
Source0:        elperiodic.tar.bz2
AutoReqProv:    no
      
%define debug_package %{nil}

%description 
El Periodic lib

%prep
%setup -q -n elperiodic


%build
%configure
make 

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
/usr/lib64/*

%changelog
* Mon Jan 20 2020 Manfred Eckschlager <meckschlager@eurofunk.com> 1.0.2
- incorporated changes until 04ee668a3d384bf7ad9ce161ad4f590a232580f7
* Wed May 23 2018 Manfred Eckschlager <meckschlager@eurofunk.com> 1.0.0-1
- Initial version of the package

