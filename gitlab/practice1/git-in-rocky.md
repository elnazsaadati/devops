# Install Git manually on Rocky Linux

# Install development tools
sudo dnf groupinstall -y "Development Tools"

# Install required Git dependencies
sudo dnf install -y libuuid-devel perl-devel python3-devel asciidoc xmlto

# Download the latest Git source code from kernel.org
wget https://www.kernel.org/pub/software/scm/git/git-2.52.0.tar.gz

# Extract the downloaded archive
tar -xzf git-2.52.0.tar.gz

# Enter the Git source directory
cd git-2.52.0

# Generate the configure script
make configure

# Configure the build environment
./configure

# Compile Git from source
make

# Install Git on the system
sudo make install

# Verify the installed Git version
git --version
