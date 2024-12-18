from setuptools import find_packages, setup

setup(
    name="django-flatpage-meta",
    version="0.0.4",
    description="A simple app to add meta tag support to flatpages",
    author="Jirka Schaefer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1  - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
    zip_safe=False,
    extras_require={
        "dev": [
            "pytest",
            "model_bakery",
        ]
    },
)
