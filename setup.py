from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='sm',
    version='0.1.8',
    keywords=('ssh', 'manager'),
    url='https://github.com/mymonkey110/ssh-manager',
    description="ssh host command manager tool",
    long_description=readme(),
    license='MIT License',
    install_requires=['pexpect', 'ptyprocess', 'tabulate'],
    author='Michael Jiang',
    author_email='mymonkey110@gmail.com',
    maintainer='Michael Jiang',
    maintainer_email='mymonkey110@gmail.com',
    packages=['sm'],
    package_data={
        'sm': ["config.schema"]
    },
    platform=('Linux', 'Mac'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Systems Administration',
    ],
    entry_points={
        'console_scripts': [
            'sm = sm.main:main',
        ]
    }
)
