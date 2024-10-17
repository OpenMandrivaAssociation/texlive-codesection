Name:		texlive-codesection
Version:	34481
Release:	2
Summary:	Provides an environment that may be conditionally included
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/codesection
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codesection.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codesection.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codesection.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an environment to switch a section of
code on or off. The code may be placed anywhere in the file (it
is not limited to the document or the preamble). The motivation
for this package was to have commands which allow preselection
based on whether sections of code in a preamble of a template
are executed.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/codesection
%{_texmfdistdir}/tex/latex/codesection
%doc %{_texmfdistdir}/doc/latex/codesection

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
