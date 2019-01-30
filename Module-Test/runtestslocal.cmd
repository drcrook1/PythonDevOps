docker stop pydevopsmoduletests
docker rm pydevopsmoduletests
cd ..
cd ./Module
PWD
docker build -t pydevopsmodule .
cd ..
cd ./Module-Test
PWD
docker build -t pydevopsmoduletests .
docker run pydevopsmoduletests
