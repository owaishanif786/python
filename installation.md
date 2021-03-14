# Installing pyenv on Ubuntu 20.04

Follow this article: <https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/>

## Install Dependencies

```bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
> libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev\
> libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl\
> git
```

### Clone Repository

`
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
`

### Configure Environment

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc

exec "$SHELL"
```

### Verify Installation

```bash
pyenv install --list
pyenv install 3.7.6
pyenv versions
pyenv shell 3.7.6
pyenv global 3.7.3
python --version
pip3.7 install --upgrade pip
pyenv help
```
