sudo apt update
sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev \
libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz

tar -xf Python-3.8.0.tgz

cd Python-3.8.0
./configure --enable-optimizations --prefix=$HOME/python3.8.0
make -j `nproc`
make install

`export PATH="$HOME/python3.8.0/bin:$PATH"`

python3.8 --version
