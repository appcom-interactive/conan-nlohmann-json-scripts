from conans import ConanFile, CMake, tools
import os

class NlohmannJsonConan(ConanFile):
    name = "NlohmannJson"
    version = "3.4.0"
    author = "Ralph-Gordon Paul (gordon@rgpaul.com)"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "android_ndk": "ANY", "android_stl_type":["c++_static", "c++_shared"]}
    default_options = "shared=False", "android_ndk=None", "android_stl_type=c++_static"
    description = "Compressing File-I/O Library"
    url = "https://github.com/Manromen/conan-nlohmann-json-scripts"
    license = "MIT"

    # download zlib sources
    def source(self):
        url = "https://github.com/nlohmann/json/archive/v%s.zip" % self.version
        tools.get(url)
        
    # compile using cmake
    def build(self):
        cmake = CMake(self)
        cmake.verbose = True

        library_folder = "json-%s" % self.version

        if self.settings.os == "Android":
            cmake.definitions["CMAKE_SYSTEM_VERSION"] = self.settings.os.api_level
            cmake.definitions["CMAKE_ANDROID_NDK"] = os.environ["ANDROID_NDK_PATH"]
            cmake.definitions["CMAKE_ANDROID_NDK_TOOLCHAIN_VERSION"] = self.settings.compiler
            cmake.definitions["CMAKE_ANDROID_STL_TYPE"] = self.options.android_stl_type

        if self.settings.os == "iOS":
            ios_toolchain = "cmake-modules/Toolchains/ios.toolchain.cmake"
            cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = ios_toolchain
            if self.settings.arch == "x86" or self.settings.arch == "x86_64":
                cmake.definitions["IOS_PLATFORM"] = "SIMULATOR"
            else:
                cmake.definitions["IOS_PLATFORM"] = "OS"

        if self.settings.os == "Macos":
            cmake.definitions["CMAKE_OSX_ARCHITECTURES"] = tools.to_apple_arch(self.settings.arch)

        cmake.configure(source_folder=library_folder)
        cmake.build()
        cmake.install()

#    def package(self):
#        self.copy("*", dst="include", src='include')
#        self.copy("*.lib", dst="lib", src='lib', keep_path=False)
#        self.copy("*.dll", dst="bin", src='bin', keep_path=False)
#        self.copy("*.so", dst="lib", src='lib', keep_path=False)
#        self.copy("*.dylib", dst="lib", src='lib', keep_path=False)
#        self.copy("*.a", dst="lib", src='lib', keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.includedirs = ['include']

    def config_options(self):
        # remove android specific option for all other platforms
        if self.settings.os != "Android":
            del self.options.android_ndk
            del self.options.android_stl_type
