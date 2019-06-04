from conans import ConanFile, CMake, tools

class NlohmannJsonConan(ConanFile):
    name = "nlohmann-json"
    version = "3.6.1"
    author = "Ralph-Gordon Paul (gordon@rgpaul.com)"
    settings = "os", "compiler", "build_type", "arch"
    # No options are necessary, this is a header only library
    # options = {"shared": [True, False], "android_ndk": "ANY", "android_stl_type":["c++_static", "c++_shared"]}
    description = "JSON for Modern C++"
    url = "https://github.com/Manromen/conan-nlohmann-json-scripts"
    license = "MIT"
    no_copy_source = True

    # download sources
    def source(self):
        url = "https://github.com/nlohmann/json/archive/v%s.zip" % self.version
        tools.get(url)

    # compile using cmake
    def build(self):
        cmake = CMake(self)

        library_folder = "json-%s" % self.version
    
        if self.settings.os == "Macos":
            cmake.definitions["CMAKE_OSX_ARCHITECTURES"] = tools.to_apple_arch(self.settings.arch)

        cmake.configure(source_folder=library_folder)
        cmake.build()
        cmake.test()

    def package(self):
        self.copy("*", dst="include", src="json-%s/single_include" % self.version)

    def package_info(self):
        self.cpp_info.includedirs = ['include']

    # this is a header only library, so we need just one package id
    def package_id(self):
        self.info.header_only()
