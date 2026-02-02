%define module pdfarranger

Name:		pdfarranger
Version:	1.13.0
Release:	1
Summary:	PDF file merging, rearranging, and splitting
Group:		Publishing
License:	GPL-3.0-only
URL:		https://github.com/jeromerobert/pdfarranger
Source0:	https://github.com/jeromerobert/pdfarranger/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	hicolor-icon-theme
BuildRequires:	intltool
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Recommends:     python%{pyver}dist(img2pdf)

Obsoletes:      pdfshuffler < 0.6.0-12
Provides:       pdfshuffler = %{version}-%{release}

%description
PDFArranger is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using an interactive and intuitive graphical interface.

The tool, which is a graphical front-end for PyPDF2, is a fork of
PDF-Shuffler that aims to "make the project a bit more active".

%prep -p
rm -rf %{module}.egg-info

%install
%{__python} setup.py install --root %{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/com.github.jeromerobert.pdfarranger.desktop
%{_datadir}/metainfo/com.github.jeromerobert.pdfarranger.metainfo.xml
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.ui
%{_datadir}/pdfarranger/menu.ui
%{_iconsdir}/hicolor/*x*/apps/com.github.jeromerobert.pdfarranger.png
%{_iconsdir}/hicolor/scalable/apps/com.github.jeromerobert.pdfarranger.svg
%{_iconsdir}/hicolor/symbolic/apps/com.github.jeromerobert.pdfarranger-symbolic.svg
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-%{version}-*.*-info
