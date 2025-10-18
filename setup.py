from setuptools import find_packages,setup

setup(

    name = "my_package",
    version = "0.1.0",
    author = "Suvignan",
    author_email="suvignan@gmail.com",
    packages = find_packages(),
    install_requires = ['numpy','pandas','flask','scikit-learn','tensorflow' ,'matplotlib','seaborn'],
    
)