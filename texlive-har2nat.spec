Name:		texlive-har2nat
Version:	54080
Release:	2
Summary:	Replace the harvard package with natbib
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/har2nat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/har2nat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/har2nat.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
