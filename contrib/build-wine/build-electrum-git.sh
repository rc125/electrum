#!/bin/bash

NAME_ROOT=electrum-smart

# These settings probably don't need any change
export WINEPREFIX=/opt/wine64
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=22

PYHOME=c:/python3
PYTHON="wine $PYHOME/python.exe -OO -B"

# Let's begin!
cd `dirname $0`
set -e

mkdir -p tmp
cd tmp

for repo in electrum-smart electrum-smart-locale electrum-smart-icons; do
    if [ -d $repo ]; then
	cd $repo
	git pull
	git checkout master
	cd ..
    else
	URL=https://github.com/rc125/$repo.git
	git clone -b master $URL $repo
    fi
done

pushd electrum-smart-locale
for i in ./locale/*; do
    dir=$i/LC_MESSAGES
    mkdir -p $dir
    msgfmt --output-file=$dir/electrum.mo $i/electrum.po || true
done
popd

pushd electrum-smart
if [ ! -z "$1" ]; then
    #git checkout $1
    git checkout master
fi

VERSION=`git describe --tags`
echo "Last commit: $VERSION"
find -exec touch -d '2000-11-11T11:11:11+00:00' {} +
popd

rm -rf $WINEPREFIX/drive_c/electrum-smart
cp -r electrum-smart $WINEPREFIX/drive_c/electrum-smart
cp electrum-smart/LICENCE .
cp -r electrum-smart-locale/locale $WINEPREFIX/drive_c/electrum-smart/lib/
cp electrum-smart-icons/icons_rc.py $WINEPREFIX/drive_c/electrum-smart/gui/qt/

# Install frozen dependencies
$PYTHON -m pip install -r ../../deterministic-build/requirements.txt

$PYTHON -m pip install -r ../../deterministic-build/requirements-hw.txt

pushd $WINEPREFIX/drive_c/electrum-smart
$PYTHON setup.py install
popd

cd ..

rm -rf dist/

# build standalone and portable versions
wine "$PYHOME/scripts/pyinstaller.exe" --noconfirm --ascii --clean --name $NAME_ROOT-$VERSION -w deterministic.spec

# set timestamps in dist, in order to make the installer reproducible
pushd dist
find -exec touch -d '2000-11-11T11:11:11+00:00' {} +
popd

# build NSIS installer
# $VERSION could be passed to the electrum-smart.nsi script, but this would require some rewriting in the script itself.
wine "$WINEPREFIX/drive_c/Program Files (x86)/NSIS/makensis.exe" /DPRODUCT_VERSION=$VERSION electrum-smart.nsi

cd dist
mv electrum-smart-setup.exe $NAME_ROOT-$VERSION-setup.exe
cd ..

echo "Done."
sha256sum dist/electrum-smart*exe