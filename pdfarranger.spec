Name:           pdfarranger
Version:        1.12.1
Release:        2
Summary:        PDF file merging, rearranging, and splitting
Group:          Publishing
License:        GPLv3
URL:            https://github.com/jeromerobert/pdfarranger
Source0:        https://github.com/jeromerobert/pdfarranger/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(python-distutils-extra)
BuildRequires:  gettext
BuildRequires:  intltool

Requires:	python-pkg-resources
Requires:	typelib(Poppler)

Recommends:     python%{pyver}dist(img2pdf)

Obsoletes:      pdfshuffler < 0.6.0-12
Provides:       pdfshuffler = %{version}-%{release}

%description
PDFArranger is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using an interactive and intuitive graphical interface.

The tool, which is a graphical front-end for PyPDF2, is a fork of
PDF-Shuffler that aims to "make the project a bit more active".

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

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%{__python} setup.py install --root %{buildroot}
#py_install

%find_lang %{name}

