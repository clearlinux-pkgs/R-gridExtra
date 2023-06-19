#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gridExtra
Version  : 2.3
Release  : 49
URL      : https://cran.r-project.org/src/contrib/gridExtra_2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gridExtra_2.3.tar.gz
Summary  : Miscellaneous Functions for "Grid" Graphics
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-gtable
BuildRequires : R-ggplot2
BuildRequires : R-gtable
BuildRequires : buildreq-R

%description
graphics, notably to arrange multiple grid-based plots on a page, and draw
    tables.

%prep
%setup -q -c -n gridExtra
cd %{_builddir}/gridExtra

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641030360

%install
export SOURCE_DATE_EPOCH=1641030360
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gridExtra
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gridExtra
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gridExtra
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gridExtra || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gridExtra/DESCRIPTION
/usr/lib64/R/library/gridExtra/INDEX
/usr/lib64/R/library/gridExtra/Meta/Rd.rds
/usr/lib64/R/library/gridExtra/Meta/features.rds
/usr/lib64/R/library/gridExtra/Meta/hsearch.rds
/usr/lib64/R/library/gridExtra/Meta/links.rds
/usr/lib64/R/library/gridExtra/Meta/nsInfo.rds
/usr/lib64/R/library/gridExtra/Meta/package.rds
/usr/lib64/R/library/gridExtra/Meta/vignette.rds
/usr/lib64/R/library/gridExtra/NAMESPACE
/usr/lib64/R/library/gridExtra/NEWS.md
/usr/lib64/R/library/gridExtra/R/gridExtra
/usr/lib64/R/library/gridExtra/R/gridExtra.rdb
/usr/lib64/R/library/gridExtra/R/gridExtra.rdx
/usr/lib64/R/library/gridExtra/doc/arrangeGrob.R
/usr/lib64/R/library/gridExtra/doc/arrangeGrob.html
/usr/lib64/R/library/gridExtra/doc/arrangeGrob.rmd
/usr/lib64/R/library/gridExtra/doc/gtable.R
/usr/lib64/R/library/gridExtra/doc/gtable.Rmd
/usr/lib64/R/library/gridExtra/doc/gtable.html
/usr/lib64/R/library/gridExtra/doc/index.html
/usr/lib64/R/library/gridExtra/doc/ngonGrob.R
/usr/lib64/R/library/gridExtra/doc/ngonGrob.Rmd
/usr/lib64/R/library/gridExtra/doc/ngonGrob.html
/usr/lib64/R/library/gridExtra/doc/tableGrob.R
/usr/lib64/R/library/gridExtra/doc/tableGrob.Rmd
/usr/lib64/R/library/gridExtra/doc/tableGrob.html
/usr/lib64/R/library/gridExtra/help/AnIndex
/usr/lib64/R/library/gridExtra/help/aliases.rds
/usr/lib64/R/library/gridExtra/help/gridExtra.rdb
/usr/lib64/R/library/gridExtra/help/gridExtra.rdx
/usr/lib64/R/library/gridExtra/help/paths.rds
/usr/lib64/R/library/gridExtra/html/00Index.html
/usr/lib64/R/library/gridExtra/html/R.css
/usr/lib64/R/library/gridExtra/tests/testthat.r
/usr/lib64/R/library/gridExtra/tests/testthat/test-arrangeGrob.R
/usr/lib64/R/library/gridExtra/tests/testthat/test-tableGrob.R
