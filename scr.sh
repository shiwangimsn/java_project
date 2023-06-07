#!/bin/bash

systemctl status jenkins

if [ $? -eq 0 ]
then
	echo "sucessul hai"
else
	echo "down  hai"
fi	

