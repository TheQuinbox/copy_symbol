@echo off
nuitka --windows-company-name=QuinSoft --windows-product-name=copy_symbol --windows-file-version=0.1 --windows-product-version=0.1 --windows-file-description=copy_symbol --standalone --python-flag=no_site --windows-disable-console --output-dir=build --remove-output src/main.pyw
pause
