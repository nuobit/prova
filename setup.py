from distutils.core import setup

setup(name='prova',
      version='0.2',
      author="NuoBiT Solutions, S.L., Eric Antones",
      author_email='eantones@nuobit.com',
      package_dir={'prova': 'src'},
      packages=['prova'],
      entry_points={
        'console_scripts': [
            'prova=prova.prova:main',
        ],
      },
      install_requires=[
      ],
      url='https://github.com/nuobit/prova',
      # download_url = 'https://github.com/eantones/imapbackup/archive/0.1.tar.gz',
      keywords=['test'],
      license='AGPLv3+',
      platform='Linux',
      description='Test',
      long_description='Test',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
      ]
      #data_files=[('config.samples', ['config.samples/servers.conf.d/01sample1.conf', 'config.samples/logger.conf']),
      #          ],
      #package_data={'coolbackup': ['config.samples/servers.conf.d/01sample1.conf', 'config.samples/logger.conf']},

)
