docker stop pydevopsmoduletests
docker rm pydevopsmoduletests
cd ..
cd ./Module
docker build -t pydevopsmodule .
cd ..
cd ./Module-Test
docker build -t pydevopsmoduletests .
docker run pydevopsmoduletests
