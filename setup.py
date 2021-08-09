from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension(
    "PyTPSA.cython.tpsalib",
    sources=[
        "cython_src/tpsalib.pyx",
        "src/polymap.cpp",
        "src/mathfunc.cpp",
    ],  # additional source file(s)
    language="c++",  # generate C++ code
    extra_compile_args=["-O3", "-std=c++11"],
)

setup(
    name="PyTPSA",
    ext_modules=cythonize(ext),
    packages=["PyTPSA", "PyTPSA.cython"],
    package_dir={"PyTPSA": "pkg", "PyTPSA.cython": "cython_src"},
    zip_safe=False,
)

