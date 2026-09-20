Name:           try
Version:        0.2.1
Release:        1%{?dist}
Summary:        Run a command and inspect its effects before changing your live system
License:        MIT
URL:            https://github.com/binpash/try
Source0:        https://github.com/binpash/try/releases/download/v%{version}/try-%{version}.tgz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  attr
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  util-linux
Requires:       attr
Requires:       util-linux

%description
try lets you run a command, inspect the changes it would make to your
filesystem, and then decide whether to commit or discard them, without
actually touching your live system.

It works by running the command inside a copy-on-write overlay, so
nothing is written to the real filesystem until you explicitly commit
the change.

%prep
%autosetup

%build
%set_build_flags
# build chroots lack the overlayfs/unshare support that configure probes for
TRY_SKIP_RUNTIME_CHECKS=yes ./configure --prefix=%{_prefix}
%make_build

%install
make install prefix=%{buildroot}%{_prefix}

# the test suite needs overlayfs and unshare, which build chroots don't provide

%files
%license LICENSE
%doc README.md
%{_bindir}/try
%{_bindir}/try-commit
%{_bindir}/try-summary
%{_bindir}/try-parse-trace
%{_mandir}/man1/try.1*

%changelog
* Sat Sep 19 2026 try maintainers <try@binpa.sh> - 0.2.1-1
- Initial RPM packaging for COPR.
