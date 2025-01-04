#rem Use the pyinstaller utility to create an executable for the Fit test environment
if exist build rmdir build /q /s
if exist dist rmdir dist /q /s
if exist BACpypesSimulator-2.0.0-se1.zip del BACpypesSimulator-2.0.0-se1.zip

pyinstaller BACpypesSim.spec
7z a BACpypesSimulator-2.0.0-se1.zip .\dist\BACpypesSim\*
