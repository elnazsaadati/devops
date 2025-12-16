# install git manually in **Rocky Linux**  
### Install development tools and required Git dependencies
```bash
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y   libuuid-devel   perl-devel   python3-devel   asciidoc   xmlto
```
### Download the latest Git source code from kernel.org


```bash wget https://www.kernel.org/pub/software/scm/git/git-2.52.0.tar.gz

tar -xzf git-2.52.0.tar.gz
cd git-2.52.0/
```
### now configure and install 
```bash make configure
 ./configure
 make
 sudo make install
```
### Verify the installed Git version
```bash
git --version
```
