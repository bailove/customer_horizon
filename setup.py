from distutils.core import setup

setup(name='customer-horizon',
      version='0.1.3',
      author = 'huangml',
      author_email= 'bailove@gmail.com',
      url = '05life.com',
      description = 'OpenStack Horizon customizations',
      package_dir= { 'customer-horizon' : 'lib'},
      py_modules=['customer-horizon.scale-horizon']
)
