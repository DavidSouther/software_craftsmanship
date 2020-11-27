#!/bin/sh

sudo -- sh <<EOF
apt update -Y && \
apt upgrade -Y

update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
EOF

python -m pip install --user pygments
gem install \
    asciidoctor \
    pygments.rb \
    asciidoctor-diagram \
    asciidoctor-pdf

