%global tl_name gs1
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	23
Release:	%{tl_revision}.1
Summary:	Typeset EAN barcodes using TeX rules, only
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gs1
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gs1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gs1.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gs1.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The (LaTeX3) package typesets EAN-8 and EAN-13 barcodes, using the
facilities of the rule-D package.

