# revision 27540
# category Package
# catalog-ctan /macros/latex/contrib/gs1
# catalog-date 2012-08-22 13:03:09 +0200
# catalog-license lppl1.3
# catalog-version 9
Name:		texlive-GS1
Version:	9
Release:	7
Summary:	Typeset EAN barcodes using TeX rules, only
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gs1
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/GS1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/GS1.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/GS1.source.tar.xz
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
%{_texmfdistdir}/tex/latex/GS1/GS1.sty
%{_texmfdistdir}/tex/latex/GS1/rule-D.sty
%doc %{_texmfdistdir}/doc/latex/GS1/GS1.pdf
%doc %{_texmfdistdir}/doc/latex/GS1/README
%doc %{_texmfdistdir}/doc/latex/GS1/examples/EANBarcode.pdf
%doc %{_texmfdistdir}/doc/latex/GS1/examples/EANBarcode.tex
%doc %{_texmfdistdir}/doc/latex/GS1/examples/EANControlDigit.pdf
%doc %{_texmfdistdir}/doc/latex/GS1/examples/EANControlDigit.tex
%doc %{_texmfdistdir}/doc/latex/GS1/examples/GSSetup.pdf
%doc %{_texmfdistdir}/doc/latex/GS1/examples/GSSetup.tex
%doc %{_texmfdistdir}/doc/latex/GS1/examples/GS_cut_EAN_control_digit.pdf
%doc %{_texmfdistdir}/doc/latex/GS1/examples/GS_cut_EAN_control_digit.tex
%doc %{_texmfdistdir}/doc/latex/GS1/examples/GS_set_EAN_control_digit.pdf
%doc %{_texmfdistdir}/doc/latex/GS1/examples/GS_set_EAN_control_digit.tex
%doc %{_texmfdistdir}/doc/latex/GS1/examples/GS_set_code_digit_seq.pdf
%doc %{_texmfdistdir}/doc/latex/GS1/examples/GS_set_code_digit_seq.tex
%doc %{_texmfdistdir}/doc/latex/GS1/examples/int_set_to_EAN_control_digit.pdf
%doc %{_texmfdistdir}/doc/latex/GS1/examples/int_set_to_EAN_control_digit.tex
%doc %{_texmfdistdir}/doc/latex/GS1/rule-D.pdf
#- source
%doc %{_texmfdistdir}/source/latex/GS1/GS1.dtx
%doc %{_texmfdistdir}/source/latex/GS1/GS1.ins
%doc %{_texmfdistdir}/source/latex/GS1/README
%doc %{_texmfdistdir}/source/latex/GS1/rule-D.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
