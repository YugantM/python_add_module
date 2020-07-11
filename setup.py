from distutils.core import setup
setup(
  name = 'add',         
  packages = ['add'],   
  version = '1.0',      
  license='MIT',        
  description = 'This package returns addition of two integers.',   
<<<<<<< HEAD
  url = 'https://github.com/yugantm/python-add',   
  download_url = 'https://github.com/yugantm/python-add.git',
=======
  url = 'https://github.com/yugantm/python_add_module',   
  download_url = 'https://github.com/yugantm/python_add_module.git',
>>>>>>> dc297bd6fcd4e4ce1a56a4ec1b022c45bc6bb2de
  entry_points = {
              'console_scripts': ['add = add.__main__:main',],
              },
  scripts=['scripts/add'],  
  keywords = ['addition', 'calculation'],  
  
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
