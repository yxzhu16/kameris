from setuptools import setup, find_packages


setup(
    name='modmap-toolkit',
    version='0.0.1pre',
    description=('Generation, analysis, and evaluation tools for Molecular '
                 'Distance Maps.'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    author='Stephen',
    author_email='stephsolis@gmail.com',
    url='https://github.com/stephensolis/modmap-toolkit/',
    license='MIT',
    packages=find_packages(),
    package_data={
        'modmap_toolkit': ['scripts/*']
    },
    entry_points={
        'console_scripts': [
            'modmap-toolkit = modmap_toolkit.launcher:main'
        ]
    },
    install_requires=[
        'numpy',
        'ruamel.yaml',
        # it's necessary to freeze scikit-learn since models are neither
        # forward nor backward-compatible
        # modmap-toolkit classify will warn if the current scikit-learn
        # version doesn't match the version at train time
        'scikit-learn==0.19.1',
        'scipy',
        'six',
        'stopit',
        'tabulate',
        'tqdm',
        'watchtower'
    ]
)