Name:           pdfarranger
Version:        1.1.1
Release:        1
Summary:        PDF file merging, rearranging, and splitting
Group:          Publishing
License:        GPLv3
URL:            https://github.com/jeromerobert/pdfarranger
Source0:        https://github.com/jeromerobert/pdfarranger/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         pdfarranger-1.1-install-appdata-file.patch
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(python-distutils-extra)
BuildRequires:  gettext
BuildRequires:  intltool

Requires:       python3dist(pygobject)
Requires:       python3dist(pypdf2)
Requires:       python3dist(pycairo)
Requires:	python-pkg-resources

Obsoletes:      pdfshuffler < 0.6.0-12
Provides:       pdfshuffler = %{version}-%{release}

%description
PDFArranger is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using an interactive and intuitive graphical interface.

The tool, which is a graphical front-end for PyPDF2, is a fork of
PDF-Shuffler that aims to "make the project a bit more active".

%prep
%setup -q
%autopatch -p1

%build
%py3_build

%install
%{__python3} setup.py install --root %{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.ui
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 08 2019 tv <tv> 1.1.1-3.mga7
+ Revision: 1352215
- rebuild with python 3.7

* Mon Jan 07 2019 daviddavid <daviddavid> 1.1.1-2.mga7
+ Revision: 1351037
- rebuild for new Python 3.7

* Sun Jan 06 2019 daviddavid <daviddavid> 1.1.1-1.mga7
+ Revision: 1350015
- new version: 1.1.1

* Tue Dec 25 2018 daviddavid <daviddavid> 1.1-2.mga7
+ Revision: 1344898
- now obsoletes/provides pdfshuffler

* Sun Dec 16 2018 daviddavid <daviddavid> 1.1-1.mga7
+ Revision: 1341749
- initial package pdfarranger

