# revision 17356
# category Package
# catalog-ctan /macros/latex/contrib/har2nat
# catalog-date 2010-03-06 16:54:30 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-har2nat
Version:	1.0
Release:	10
Summary:	Replace the harvard package with natbib
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/har2nat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/har2nat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/har2nat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package allows a LaTeX document containing the
citation commands provided by the Harvard package to be
compiled using the natbib package. Migration from harvard to
natbib thus can be achieved simply by replacing
\usepackage{harvard} with \usepackage{natbib}
\usepackage{har2nat} It is important that har2nat be loaded
after natbib, since it modifies natbib commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/har2nat/har2nat.sty
%doc %{_texmfdistdir}/doc/latex/har2nat/README
%doc %{_texmfdistdir}/doc/latex/har2nat/har2nat.pdf
%doc %{_texmfdistdir}/doc/latex/har2nat/har2nat.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752461
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718599
- texlive-har2nat
- texlive-har2nat
- texlive-har2nat
- texlive-har2nat

