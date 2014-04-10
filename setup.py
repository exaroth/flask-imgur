"""
Flask-Imgur
-----------


This is simple flask extension allowing uploading
images straight to Imgur image hosting service.


"""


from setuptools import setup

setup(
    name="Flask-Imgur",
    version="0.1",
    url="https://github.com/exaroth/flask-imgur",
    license="BSD",
    author="Konrad Wasowicz",
    author_email="exaroth@gmail.com",
    description="Upload images straight to Imgur",
    long_description=__doc__,
    zip_safe=False,
    packages=["flask-imgur"],
    include_package_data=True,
    platforms="any",
    install_requires=["Flask", "six"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
