<font size=4 face='face'>  

$ sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make  
$ sudo mv python python.bak  
$ sudo wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz  
$ sudo mkdir -p /usr/local/python3  
$ cd /usr/local/python3  
$ sudo tar -zxvf Python-3.7.1.tgz  
$ cd Python-3.7.1  
$ sudo ./configure prefix=/usr/local/python3  
$ sudo ./configure --prefix=/usr/local/python3  
$ sudo make && make install  
$ sudo ln -s /usr/local/python3/bin/python3 /usr/bin/python  
$ cd /usr/bin  
$ ll python*  
$ sudo ln -s /usr/local/python3/bin/python3 /usr/bin/python  
$ sudo ln -s /usr/bin/python2.7 /usr/bin/python2  
$ export LANG=zh_CN.UTF-8  
$ export LANGUAGE=zh_CN.UTF-8  
$ sudo ./configure prefix=/usr/local/python3  
$ sudo make && make install  
$ sudo ./configure prefix=/usr/local/python3  
$ sudo make  
$ sudo make install  
$ sudo ln -snf /usr/bin/python2.7 /usr/bin/python2  
$ python2 -m pip list  
$ python3 -m pip list  
$ python -m pip install robotframework  
$ python -m pip install robotframework -i http://pypi.douban.com/simple  
$ sudo vim .pip/pip.conf  
$ sudo update-alternatives --config python  
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1   
$ sudo update-alternatives --install /usr/bin/python python /usr/local/python3 2   
$ sudo update-alternatives --install /usr/bin/python python /usr/local/python3/bin/python3  
$ update-alternatives --display python  
$ sudo update-alternatives --remove python /usr/local/python3/  
$ ls *[ython]*  
$ sudo rm -f Python-3.6.2.tar.xz  
$ sudo rm -f Python-3.7.1.tar.xz  
$ sudo find / -name ssl.h  
$ cd /usr/include/openssl/  
$ cat ssl.h  
$ sudo wget install libssl-dev  
$ sudo ln -s /usr/local/python3/bin/pip3 pip3  
$ ll pip*  
$ cd Python-3.7.1  
$ sudo ./configure prefix=/usr/local/python3 --with-ssl  
$ sudo make  
$ sudo make install  
$ sudo ./configure --with-ssl  
$ sudo make  
$ sudo make install  
$ sudo ./configure --enable-optimizations  
$ sudo make  
$ sudo make install  
$ pip3 --trusted-host pypi.python.org install robotframework  
$ pip3 --trusted-host pypi.org/simple install robotframework  
$ sudo ./configure --prefix=/usr/local/python3 --enable-optimizations --with-ssl   
$ sudo make  
$ sudo make install  
$ pip3 install robotframework -i http://pypi.douban.com/simple  
$ sudo vim ~/.pip/pip.comf  
$ openssl version  

$ sudo wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz  
$ sudo tar xzf Python-3.6.6.tgz  
$ cd Python-3.6.6  
$ sudo ./configure --enable-optimizations  
$ sudo make  
$ sudo make install  
$ whereis python3.6  
$ cd /usr/bin  
$ ll python*   
$ sudo ln -s /usr/local/bin/python3.6m python3.6  
$ ll python*   
$ python3.6  
$ ll pip*  
$ sudo ln -s /usr/local/bin/pip3.6 pip3.6  
$ ll pip*  
$ pip3.6 list  
$ pip3.6 install --upgrade pip  
$ sudo pip3.6 install --upgrade pip  
$ sudo pip3.6 install robotframework  

$ mkdir mkdir Test_Master_5_Min_Py3  
$ ls  
$ cd Test_Master_5_Min_Py3/  
$ git status  
$ git init   
$ git remote add origin git@code.aliyun.com:ChangK/thejoyrunTestcode.git  
$ git pull origin joyrun_for_py3  

$ sudo wget install virtualenvwrapper  
$ sudo pip install virtualenvwrapper  
$ sudo mkvirtualenv -p /usr/bin/python3.6m env36  
$ mkvirtualenv  
$ mkvirtualenvwrapper  
$ sudo pip install virtualenv  
$ sudo virtualenv env36m  
$ sudo virtualenv -p python3.6 env36m  
$ sudo virtualenv --system-site-packages env36m  
$ source env36m/bin/activate  
$ python --version  
$ pybot --version  
$ python3 --version  
$ python3.7 --version  
$ deactivate  
$ sudo rm -rf env36m  





$ sudo ./configure --enable-shared --enable-loadable-sqlite-extensions  



$ sudo update-alternatives --config python  
$ python version  
$ sudo wget install virtualenvrapper  
$ sudo pip install virtualenvrapper  
$ pip --version  
$ ll pip*  
$ sudo mkvirtualenv -p /usr/bin/python3.6m env36  
$ sudo pip install virtualenv  
$ sudo virtualenv env36m  
$ sudo virtualenv -p python3.6 env36m  
$ sudo virtualenv --system-site-packages env36m  
$ source env36m/bin/activate  
$ deactivate  
$ virtualenv -h  
$ sudo rm -rf env36m  

$ cd /opt  
$ sudo python3 -m venv py3  
$ ls  
$ source /opt/py3/bin/activate  
$ deactivate  
$ sudo python3.6 -m venv py3.6  
$ source /opt/py3.6/bin/activate  
$ python  
$ pybot  
$ pip list  
$ pip robotframework  
$ pip --version  
$ pip install robotframework  
$ sudo pip install robotframework  
$ ./pip install robotframework  
$ sudo ./pip install robotframework  
$ cd py3.6/bin  
$ ls   
$ sudo ./pip install robotframework  
$ pip list  
$ pip install --upgrade pip  
$ sudo ./pip install robotframework-requests  
$ sudo ./pip install pymysql  
$ sudo ./pip install robotframework -databaselibrary  
$ sudo ./pip install jsonpointer  
$ deactivate  
$ cd /var/lib/jenkins/workspace/Joyrun_Server/  
$ ls  
$ mkdir Online_Master_Day_5_Py3  
$ ls  
$ cd Online_Master_Day_5_Py3/   
$ git init  
$ git remote add origin git@code.aliyun.com:ChangK/thejoyrunTestcode.git   
$ git pull origin joyrun_for_py3  
$ ls  









