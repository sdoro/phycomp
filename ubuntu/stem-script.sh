#!/bin/bash

# erase all student's home
rm -rf /home/studentestem

# restore default STEM student's home
tar zxf /root/stu.tgz -C /home/

# bot
