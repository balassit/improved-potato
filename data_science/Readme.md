# Datascience



```
git clone data_structures
cd data_structures
conda create -n env python -y
source activate env
conda install --yes --file requirements.txt
python3 example.py
```

### Anaconda

[Install Anaconda](https://www.anaconda.com/download/#macos)

### Miniconda

The fastest way to obtain conda is to install Miniconda, a mini version of Anaconda that includes only conda and its dependencies. If you prefer to have conda plus over 720 open source packages, install Anaconda.

[docs](https://conda.io/docs/user-guide/install/index.html)

[Install Miniconda](https://conda.io/miniconda.html)

```
brew install wget
brew install md5sha1sum
wget https://repo.continuum.io/miniconda/Miniconda3-3.6.0-Linux-x86_64.sh -O ~/Downloads/miniconda.sh
bash ~/Downloads/miniconda.sh -b -p $HOME/miniconda
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> ~/.bash_profile
rm ~/Downloads/miniconda.sh
```