# $1 = plover config location

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

rm -r $DIR/dist
python3 setup.py sdist bdist_wheel

WHEEL=`ls $DIR/dist | grep .whl`
echo $WHEEL
python3 -m pip install $DIR/dist/$WHEEL --target $1/plover/plover/plugins/win/Python36/site-packages/ --upgrade
