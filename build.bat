@mkdir build
g++ -c carlinhos.cpp -o build\carlinhos.o -O3
g++ -static -static-libgcc -static-libstdc++ -o build\dalva.exe build\carlinhos.o
@pause