#!/usr/bin/env bash

set -e

echo "Checking Student Management System files..."

test -f index.html
test -f students.html
test -f courses.html
test -f teachers.html
test -f css/style.css
test -f js/script.js
test -d css
test -d js

echo "All static file checks passed."