#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cowplot
Version  : 0.9.2
Release  : 3
URL      : https://cran.r-project.org/src/contrib/cowplot_0.9.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cowplot_0.9.2.tar.gz
Summary  : Streamlined Plot Theme and Plot Annotations for 'ggplot2'
Group    : Development/Tools
License  : GPL-2.0
Requires: R-ggplot2
Requires: R-plyr
Requires: R-scales
Requires: R-viridis
BuildRequires : R-ggplot2
BuildRequires : R-plyr
BuildRequires : R-scales
BuildRequires : R-viridis
BuildRequires : clr-R-helpers

%description
package. In particular, this package makes it easy to combine multiple
    'ggplot2' plots into one and label them with letters, e.g. A, B, C, etc.,
    as is often required for scientific publications. The package also provides
    a streamlined and clean theme that is used in the Wilke lab, hence the
    package name, which stands for Claus O. Wilke's plot package.

%prep
%setup -q -c -n cowplot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523296455

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523296455
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cowplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cowplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cowplot
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library cowplot|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cowplot/DESCRIPTION
/usr/lib64/R/library/cowplot/INDEX
/usr/lib64/R/library/cowplot/Meta/Rd.rds
/usr/lib64/R/library/cowplot/Meta/features.rds
/usr/lib64/R/library/cowplot/Meta/hsearch.rds
/usr/lib64/R/library/cowplot/Meta/links.rds
/usr/lib64/R/library/cowplot/Meta/nsInfo.rds
/usr/lib64/R/library/cowplot/Meta/package.rds
/usr/lib64/R/library/cowplot/Meta/vignette.rds
/usr/lib64/R/library/cowplot/NAMESPACE
/usr/lib64/R/library/cowplot/NEWS
/usr/lib64/R/library/cowplot/R/cowplot
/usr/lib64/R/library/cowplot/R/cowplot.rdb
/usr/lib64/R/library/cowplot/R/cowplot.rdx
/usr/lib64/R/library/cowplot/doc/axis_position.R
/usr/lib64/R/library/cowplot/doc/axis_position.Rmd
/usr/lib64/R/library/cowplot/doc/axis_position.html
/usr/lib64/R/library/cowplot/doc/index.html
/usr/lib64/R/library/cowplot/doc/introduction.R
/usr/lib64/R/library/cowplot/doc/introduction.Rmd
/usr/lib64/R/library/cowplot/doc/introduction.html
/usr/lib64/R/library/cowplot/doc/plot_annotations.R
/usr/lib64/R/library/cowplot/doc/plot_annotations.Rmd
/usr/lib64/R/library/cowplot/doc/plot_annotations.html
/usr/lib64/R/library/cowplot/doc/plot_grid.R
/usr/lib64/R/library/cowplot/doc/plot_grid.Rmd
/usr/lib64/R/library/cowplot/doc/plot_grid.html
/usr/lib64/R/library/cowplot/doc/shared_legends.R
/usr/lib64/R/library/cowplot/doc/shared_legends.Rmd
/usr/lib64/R/library/cowplot/doc/shared_legends.html
/usr/lib64/R/library/cowplot/help/AnIndex
/usr/lib64/R/library/cowplot/help/aliases.rds
/usr/lib64/R/library/cowplot/help/cowplot.rdb
/usr/lib64/R/library/cowplot/help/cowplot.rdx
/usr/lib64/R/library/cowplot/help/paths.rds
/usr/lib64/R/library/cowplot/html/00Index.html
/usr/lib64/R/library/cowplot/html/R.css
