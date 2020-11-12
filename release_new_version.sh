echo "make sure you changed version number in setup.py"
rm -r build/
rm -r dist/
rm -r flexpy.egg-info/
python setup.py sdist bdist_wheel


# # upload to testpypi
# twine upload --repository testpypi dist/*
# # use virtualenv to test new version
# mkvirtualenv flexpy
# # (if it already exists, rmvirtualenv it and make new one)
# workon flexpy
# # (it will already put you in virtualenv after you make it, but workon is how you enter an existing one)
# python -m pip install --index-url https://test.pypi.org/simple/ flexpy
# # now new flexpy should be installed in the venv so you can try it out
# python  # test stuff
# deactivate  # exit virtualenv
# rmvirtualenv flexpy


# # upload to pypi
# twine upload dist/*
# python -m pip install flexpy --upgrade
