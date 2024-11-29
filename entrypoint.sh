#!/bin/sh
apk add doas
adduser -S nisha -G nginx
echo 'nisha:123' | chpasswd
echo 'permit nopass :nginx as root' > /etc/doas.conf
su nisha 