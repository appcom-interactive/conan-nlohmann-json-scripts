# Conan NlohmannJson

This repository contains the conan receipe that is used to build the nlohmann json packages at appcom.

For Infos about the library please visit [Github](https://github.com/nlohmann/json).  
The library is licensed under the [MIT License](https://github.com/nlohmann/json/blob/master/LICENSE.MIT).  
This repository is licensed under the [MIT License](LICENSE).


## macOS

To create a package for macOS you can run the conan command like this:

`conan create . nlohmann-json/3.6.1@appcom/stable`

### Requirements

* [CMake](https://cmake.org/)
* [Conan](https://conan.io/)
* [Xcode](https://developer.apple.com/xcode/)
