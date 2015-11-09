from setuptools import setup, find_packages

setup(
    name='sm',
    version='0.0.2',
    keywords=('ssh', 'manager'),
    description="ssh host command manager tool",
    license='MIT License',
    install_requires=['ecdsa==0.13', 'pexpect==4.0.1', 'ptyprocess==0.5', 'pycrypto==2.6.1', 'tabulate==0.7.5',
                      'wheel==0.24.0'],
    author='Michael Jiang',
    author_email='mymonkey110@gmail.com',
    maintainer='Michael Jiang',
    maintainer_email='mymonkey110@gmail.com',
    packages=find_packages(),
    platform=('Linux', 'Mac'),
    entry_points={
        'console_script': [
            'sm=sm.sm:main'
        ],
    }
)
