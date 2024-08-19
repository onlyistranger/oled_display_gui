ECHO using MinGW to build x86 dll
gcc -shared -Os -s -o image_processing.dll image_processing.c
copy ./image_processing.dll ./../image_processing.dll

ECHO using MinGW-w64 to build x64 dll
ECHO gcc -shared -Os -s -o image_processing_x64.dll image_processing.c
ECHO copy ./image_processing_x64.dll ./../image_processing_x64.dll