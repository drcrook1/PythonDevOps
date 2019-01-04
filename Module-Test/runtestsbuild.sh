mkdir $(System.DefaultWorkingDirectory)/junit
cd ./Module
docker build -t pydevopsmodule .
cd ..
cd ./Module-Test
docker build -t pydevopsmoduletests .
cd $(System.DefaultWorkingDirectory)
docker run -v  $(System.DefaultWorkingDirectory)/junit:/tests/junit pydevopsmoduletests
sudo chown -R $(id -u):$(id -u) $(System.DefaultWorkingDirectory)/junit/
