echo "make sure you changed version number in setup.py"
rm -r build/
rm -r dist/
rm -r flexpy.egg-info/
/usr/bin/python3.8 setup.py sdist bdist_wheel

# # to test without having to change version number: install via pip directly from git branch (on remote)
# python -m pip install git+https://github.com/kuhron/flexpy.git@main

# # upload to testpypi
# twine upload --repository testpypi dist/*
# # use virtualenv to test new version
# mkvirtualenv flexpy
# # (if it already exists, rmvirtualenv it and make new one)
# workon flexpy
# # (it will already put you in virtualenv after you make it, but workon is how you enter an existing one)
# cd  # get out of the flexpy dir or that module will be in python's vision and it will think you already got the new version from pip
# python -m pip install --index-url https://test.pypi.org/simple/ flexpy
# # now new flexpy should be installed in the venv so you can try it out
# python  # test stuff
# deactivate  # exit virtualenv
# rmvirtualenv flexpy


# # upload to pypi
# twine upload dist/*
# python -m pip install flexpy --upgrade

