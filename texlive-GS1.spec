Name:		texlive-GS1
Version:	59620
Release:	2
Summary:	Typeset EAN barcodes using TeX rules, only
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gs1
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gs1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gs1.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gs1.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The (LaTeX 3) package typesets EAN-8 and EAN-13 barcodes, using
the facilities of the rule-D package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gs1
%doc %{_texmfdistdir}/doc/latex/gs1
#- source
%doc %{_texmfdistdir}/source/latex/gs1

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
