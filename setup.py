import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="steriplus",
    version="0.1.0",
    author="Kjell Jorner",
    author_email="kjell.jorner@gmail.com",
    description="A package to calculate Sterimol values.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=["steriplus"],
    install_requires=["matplotlib", "numpy", "scipy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "steriplus_sterimol=steriplus.script_sterimol:main",
            "steriplus_sasa=steriplus.script_sasa:main",
        ]}
)
