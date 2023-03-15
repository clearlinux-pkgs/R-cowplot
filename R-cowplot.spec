#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cowplot
Version  : 1.1.1
Release  : 50
URL      : https://cran.r-project.org/src/contrib/cowplot_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cowplot_1.1.1.tar.gz
Summary  : Streamlined Plot Theme and Plot Annotations for 'ggplot2'
Group    : Development/Tools
License  : GPL-2.0
Requires: R-ggplot2
Requires: R-gtable
Requires: R-rlang
Requires: R-scales
BuildRequires : R-ggplot2
BuildRequires : R-gtable
BuildRequires : R-rlang
BuildRequires : R-scales
BuildRequires : buildreq-R

%description
Provides various features that help with creating publication-quality figures
    with 'ggplot2', such as a set of themes, functions to align plots and arrange
    them into complex compound figures, and functions that make it easy to annotate
    plots and or mix plots with images. The package was originally written for
    internal use in the Wilke lab, hence the name (Claus O. Wilke's plot package).
    It has also been used extensively in the book Fundamentals of Data
    Visualization.

%prep
%setup -q -c -n cowplot
cd %{_builddir}/cowplot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640993641

%install
export SOURCE_DATE_EPOCH=1640993641
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cowplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cowplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cowplot
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc cowplot || :


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
/usr/lib64/R/library/cowplot/NEWS.md
/usr/lib64/R/library/cowplot/R/cowplot
/usr/lib64/R/library/cowplot/R/cowplot.rdb
/usr/lib64/R/library/cowplot/R/cowplot.rdx
/usr/lib64/R/library/cowplot/doc/index.html
/usr/lib64/R/library/cowplot/doc/introduction.R
/usr/lib64/R/library/cowplot/doc/introduction.Rmd
/usr/lib64/R/library/cowplot/doc/introduction.html
/usr/lib64/R/library/cowplot/extdata/cow.jpg
/usr/lib64/R/library/cowplot/extdata/logo.png
/usr/lib64/R/library/cowplot/help/AnIndex
/usr/lib64/R/library/cowplot/help/aliases.rds
/usr/lib64/R/library/cowplot/help/cowplot.rdb
/usr/lib64/R/library/cowplot/help/cowplot.rdx
/usr/lib64/R/library/cowplot/help/figures/logo.png
/usr/lib64/R/library/cowplot/help/paths.rds
/usr/lib64/R/library/cowplot/html/00Index.html
/usr/lib64/R/library/cowplot/html/R.css
/usr/lib64/R/library/cowplot/tests/figs/deps.txt
/usr/lib64/R/library/cowplot/tests/figs/draw-functions/bottom-right-half-width-height.svg
/usr/lib64/R/library/cowplot/tests/figs/draw-functions/centered-full-width-height.svg
/usr/lib64/R/library/cowplot/tests/figs/draw-functions/centered-half-width-height.svg
/usr/lib64/R/library/cowplot/tests/figs/draw-functions/four-corners-aligned-scaled.svg
/usr/lib64/R/library/cowplot/tests/figs/draw-functions/four-corners-centered-scaled.svg
/usr/lib64/R/library/cowplot/tests/figs/draw-functions/label-color-specified-w-uk-spelling.svg
/usr/lib64/R/library/cowplot/tests/figs/draw-functions/label-color-specified-w-us-spelling.svg
/usr/lib64/R/library/cowplot/tests/figs/draw-functions/label-color-taken-from-theme.svg
/usr/lib64/R/library/cowplot/tests/figs/draw-functions/top-left-half-width-height.svg
/usr/lib64/R/library/cowplot/tests/figs/key-glyph/circle-key-glyph-color-used-as-fill.svg
/usr/lib64/R/library/cowplot/tests/figs/key-glyph/rectangle-key-glyph-color-used-as-fill.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/aligning-faceted-plots-w-unequal-widths.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/basic-plot-arranging-labeling.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/basic-plot-arranging-with-missing-plot.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/colwise-arranging.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/h-v-alignment-right-and-top-axes.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/horizontal-alignment-bottom-axis.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/horizontal-alignment-top-axis.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/horizontal-alignment.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/horizontal-vertical-alignment.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/scaling-plots.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/setting-heights-1-1-2.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/setting-widths-1-1-2.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/vertical-alignment-left-axis.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/vertical-alignment-right-axis.svg
/usr/lib64/R/library/cowplot/tests/figs/plot-grid/vertical-alignment.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-half-open-huge.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-half-open-tiny.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-half-open.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-minimal-grid-huge.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-minimal-grid-tiny.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-minimal-grid.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-minimal-hgrid-huge.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-minimal-hgrid-tiny.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-minimal-hgrid.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-minimal-vgrid-huge.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-minimal-vgrid-tiny.svg
/usr/lib64/R/library/cowplot/tests/figs/themes/theme-minimal-vgrid.svg
/usr/lib64/R/library/cowplot/tests/testthat.R
/usr/lib64/R/library/cowplot/tests/testthat/helper-vdiffr.R
/usr/lib64/R/library/cowplot/tests/testthat/test_align_plots.R
/usr/lib64/R/library/cowplot/tests/testthat/test_draw_.R
/usr/lib64/R/library/cowplot/tests/testthat/test_get_axes.R
/usr/lib64/R/library/cowplot/tests/testthat/test_get_legend.R
/usr/lib64/R/library/cowplot/tests/testthat/test_get_panel.R
/usr/lib64/R/library/cowplot/tests/testthat/test_get_titles.R
/usr/lib64/R/library/cowplot/tests/testthat/test_ggdraw.R
/usr/lib64/R/library/cowplot/tests/testthat/test_key_glyph.R
/usr/lib64/R/library/cowplot/tests/testthat/test_plot_components.R
/usr/lib64/R/library/cowplot/tests/testthat/test_plot_grid.R
/usr/lib64/R/library/cowplot/tests/testthat/test_themes.R
