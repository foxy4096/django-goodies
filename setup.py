from setuptools import setup, find_packages

setup(
    name="django-goodies",
    version="0.1.0",
    description="A collection of small reusable Django apps and widgets.",
    long_description=open("readme.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="foxy4096",
    author_email="lamdbacore34@gmail.com",
    url="https://github.com/foxy4096/django-goodies",
    packages=find_packages(include=["django_goodies", "django_goodies.*"]),
    include_package_data=True,
    install_requires=[
        "Django>=3.2",
        "markdown2",
        "itsdangerous",
        "requests-oauthlib",
    ],
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    license="MIT",
    keywords="django reusable widgets autocomplete markdown auth htmx",

)
