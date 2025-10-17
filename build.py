
import os
import sys
import shutil
import subprocess
import ninja.ninja

root_dir = os.path.abspath(os.path.dirname(__file__))
source_dir = f"{root_dir}/libpng"
build_dir = f"{root_dir}/build"
install_dir = f"{root_dir}/install"
uv = shutil.which("uv")
cmake = shutil.which("cmake")

print(f"root directory - {root_dir}")
print(f"source directory - {source_dir}")
print(f"build directory - {build_dir}")
print(f"install directory - {install_dir}")
print(f"use cmake - {cmake}")
print(f"use uv - {uv}")

cmake = [cmake]

subprocess.run(cmake + ["-S", source_dir,
                        "-B", build_dir,
                        "-DCMAKE_BUILD_TYPE=Release",
                        f"-DCMAKE_INSTALL_PREFIX={install_dir}",
                        "-DPNG_TESTS=OFF",
                        "-DPNG_EXECUTABLES=OFF",
                        "-DPNG_BUILD_ZLIB=OFF",
                        "-DPNG_HARDWARE_OPTIMIZATIONS=ON",
                        "-Wno-dev",
                        f"-DZLIB_ROOT={root_dir}/zlib/",
                        f"-DPNG_TOOLS=OFF"],
               cwd=source_dir,
               env=ninja.ninja.add_ninja(),
               check=True)

subprocess.run(cmake + ["--build", build_dir,"--config", "Release"],cwd=build_dir,env=ninja.ninja.add_ninja(),check=True)
subprocess.run(cmake + ["--install", build_dir,"--config", "Release"],cwd=build_dir,env=ninja.ninja.add_ninja(),check=True)
