FROM mcr.microsoft.com/vscode/devcontainers/universal:linux

RUN sudo apt-get update && \
    sudo apt-get upgrade && \
    gem install asciidoctor && \
    python2 -m pip install --user pygments && \
    gem install pygments.rb && \
    gem install asciidoctor-diagram  && \
    gem install asciidoctor-pdf  && \
    exit 0
