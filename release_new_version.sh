echo "make sure you changed version number in setup.py"
rm -r build/
rm -r dist/
rm -r flexpy.egg-info/
python setup.py sdist bdist_wheel
