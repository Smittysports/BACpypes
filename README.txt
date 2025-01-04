Instructions to create an executable to run the BACpypes python scripts

1)	sudo apt install python3-venv
2)	python3 -m venv .venv
3)	source .venv/bin/activate
4)	pip install pyinstaller
5)	pip install ConfigParser
6)	pyinstaller BACpypesSim.spec
7)	sudo apt install 7zip
8)	7z a BACpypesSimulator-2.0.0-se1.zip .\dist\BACpypesSim\*
    a.	Only needed to zip up the executable
9) cd dist/BACpypesSim
10) ./BACpypesSim --ini=../../BACpypesSim.ini --localAddress=0.0.0.0 --objects=../../object_configurations/basic_objects_cfg.py
