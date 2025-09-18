"""
Setup configuration for VirtualInput library
With GitHub repository links
"""

from setuptools import setup, find_packages
import os
import platform

def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "Cross-platform virtual mouse and keyboard with ghost coordinates and Bézier curves"

def get_version():
    version_file = os.path.join("virtualinput", "__init__.py")
    with open(version_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
    return "1.0.0"

def get_platform_dependencies():
    extras_require = {
        'macos': [
            'pyobjc-framework-Cocoa>=9.0',
            'pyobjc-framework-Quartz>=9.0',
        ],
        'windows': [],
        'dev': [
            'pytest>=7.0.0',
            'black>=22.0.0',
            'build>=0.8.0',
            'twine>=4.0.0',
        ]
    }
    
    install_requires = []
    
    system = platform.system().lower()
    if system == 'darwin':
        install_requires.extend(extras_require['macos'])
    
    return install_requires, extras_require

install_requires, extras_require = get_platform_dependencies()

setup(
    name="virtualinput",
    version=get_version(),
    author="off.rkv",
    author_email="off.rkv@gmail.com",  # You can change this
    description="Cross-platform virtual mouse and keyboard with ghost coordinates and Bézier curves",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    
    # GitHub repository URLs
    url="https://github.com/off-rkv/Virtual-Input",
    project_urls={
        "Bug Tracker": "https://github.com/off-rkv/Virtual-Input/issues",
        "Documentation": "https://github.com/off-rkv/Virtual-Input/blob/main/README.md",
        "Source Code": "https://github.com/off-rkv/Virtual-Input",
        "Download": "https://github.com/off-rkv/Virtual-Input/releases",
    },
    
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Desktop Environment",
    ],
    
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    
    keywords=[
        "automation", "mouse", "keyboard", "virtual", "input", "simulation",
        "cross-platform", "bezier", "curves", "ghost", "coordinates",
        "windows", "macos", "recording", "macro", "bot", "rkv"
    ],
    
    include_package_data=True,
    zip_safe=False,
    license="MIT",
)
