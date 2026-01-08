from setuptools import setup

setup(
    name='browser_cookie',
    version='0.1.0',
    packages=['browser_cookie'],
    # look for package contents in current directory
    package_dir={'browser_cookie': 'browser_cookie'},
    author='cipher-shad0w',
    description='Loads cookies from your browser into a cookiejar object so can download with urllib and other libraries the same content you see in the web browser.',     # noqa: E501
    url='https://github.com/borisbabic/browser_cookie',
    install_requires=[
        'lz4',
        'pycryptodomex',
        'dbus-python; python_version < "3.7" and ("bsd" in sys_platform or sys_platform == "linux")',
        'jeepney; python_version >= "3.7" and ("bsd" in sys_platform or sys_platform == "linux")',
        'shadowcopy; python_version >= "3.7" and platform_system == "Windows"',
    ],
    entry_points={'console_scripts': ['browser-cookie=browser_cookie.__main__:main']},
    license='lgpl'
)
