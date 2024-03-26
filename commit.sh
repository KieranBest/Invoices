#!/bin/sh
git add Finances.csv
timestamp() {
    date +"at %H:%M:%S on %d/%m/%Y"
}
git commit -am "Regular auto-commit $(timestamp)"
git push origin main
