#!/bin/sh
apk add doas
adduser nisha1 -G nginx
echo 'nisha1:123456' | chpasswd
echo 'permit nopass :nginx as root' > /etc/doas.conf
su nisha1 