#!/bin/bash
chown -R mysql:mysql /var/lib/mysql && service mysql start && tail -f /dev/null