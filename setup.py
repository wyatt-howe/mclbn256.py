from setuptools import setup, dist

class BinaryDistribution(dist.Distribution):
    def is_pure(self):
        return False

setup(
    # name='mclbn256',
    # package_data={'lib': ['libmclbn256.dylib']},
    # package_data={'mclbn256': ['../lib/libmclbn256.dylib', '../lib/libmclbn256.dll']},
    # package_data={'mclbn256': ['libmclbn256.dylib']},
    # data_files=['libmclbn256.dylib'],
    # include_package_data=True,
    distclass=BinaryDistribution,
    # packages=['mclbn256'],
)
