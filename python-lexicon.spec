#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-lexicon.spec)

Summary:	Powerful dict subclass(es) with aliasing & attribute access
Summary(pl.UTF-8):	Funkcjonalne podklasy dict z dostępem przez aliasy i atrybuty
Name:		python-lexicon
# keep 1.x here for python2 support
Version:	1.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/lexicon/
Source0:	https://files.pythonhosted.org/packages/source/l/lexicon/lexicon-%{version}.tar.gz
# Source0-md5:	3458e3a6fa04cb53f860a835b295f7a0
URL:		https://pypi.org/project/lexicon/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-six
BuildRequires:	python-spec >= 0.10.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six
BuildRequires:	python3-spec >= 0.10.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lexicon is a simple Python 2.6+ and 3.3+ compatible collection of dict
subclasses providing extra power:
- AliasDict: a dictionary supporting both simple and complex key
  aliasing:
  - Alias a single key to another key, for both reads and writes.
  - Alias a single key to a list of other keys, for writing only.
  - Aliasing is recursive: an alias pointing to another alias will
    behave as if it points to the other alias' target.
- AttributeDict: supporting attribute read & write access.
- Lexicon: a subclass of both of the above which exhibits both sets of
  behavior.

%description -l pl.UTF-8
Lexicon to zgodny z Pythonem 2.6+ i 3.3+ zbiór prostych podklas dict,
zapewniających dodatkowe funkcje:
- AliasDict - słownik obsługujący proste i bardziej złożone aliasy
  kluczy:
  - alias pojedynczego klucza pod innym przy odczycie i zapisie
  - alias wielu kluczy pod jednym, tylko do zapisu
  - aliasy są rekurencyjne: alias wskazujący na alias zachowuje się
    tak, jakby wskazywał na cel tego aliasu
- AttributeDict - obsługujący odczyt i zapis poprzez atrybuty
- Lexicon - podklasy obu, udostępniające oba zachowania.

%package -n python3-lexicon
Summary:	Powerful dict subclass(es) with aliasing & attribute access
Summary(pl.UTF-8):	Funkcjonalne podklasy dict z dostępem przez aliasy i atrybuty
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-lexicon
Lexicon is a simple Python 2.6+ and 3.3+ compatible collection of dict
subclasses providing extra power:
- AliasDict: a dictionary supporting both simple and complex key
  aliasing:
  - Alias a single key to another key, for both reads and writes.
  - Alias a single key to a list of other keys, for writing only.
  - Aliasing is recursive: an alias pointing to another alias will
    behave as if it points to the other alias' target.
- AttributeDict: supporting attribute read & write access.
- Lexicon: a subclass of both of the above which exhibits both sets of
  behavior.

%description -n python3-lexicon -l pl.UTF-8
Lexicon to zgodny z Pythonem 2.6+ i 3.3+ zbiór prostych podklas dict,
zapewniających dodatkowe funkcje:
- AliasDict - słownik obsługujący proste i bardziej złożone aliasy
  kluczy:
  - alias pojedynczego klucza pod innym przy odczycie i zapisie
  - alias wielu kluczy pod jednym, tylko do zapisu
  - aliasy są rekurencyjne: alias wskazujący na alias zachowuje się
    tak, jakby wskazywał na cel tego aliasu
- AttributeDict - obsługujący odczyt i zapis poprzez atrybuty
- Lexicon - podklasy obu, udostępniające oba zachowania.

%prep
%setup -q -n lexicon-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
spec-2 -w tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
spec-3 -w tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/lexicon
%{py_sitescriptdir}/lexicon-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-lexicon
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/lexicon
%{py3_sitescriptdir}/lexicon-%{version}-py*.egg-info
%endif
