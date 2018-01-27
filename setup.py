#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'task-mapper',
        version = '1.0',
        description = 'Task Mapper',
        long_description = 'distribute tasks performed on many files on either threads or processes',
        author = "Pontus Pohl",
        author_email = "pontus.pohl@gmail.com",
        license = '',
        url = '',
        scripts=['task-mapper/scripts/task-mapper'],
        py_modules = [],
        classifiers = [
            'Development Status :: Alpha',
            'Environment :: Python',
            'Intended Audience :: Envac',
            'Intended Audience :: Envac',
            'Programming Language :: Python',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Topic :: System :: Monitoring',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3'
        ],
        entry_points = {},
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe=True,
        cmdclass={'install': install},
    )

   
