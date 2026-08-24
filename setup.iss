[Setup]
AppName=Matin Calculator
AppVersion=1.0
DefaultDirName={pf}\MatinCalculator
DefaultGroupName=Matin Calculator
OutputDir=output
OutputBaseFilename=MatinCalculatorSetup
SetupIconFile=icon\main_icon.ico
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Matin Calculator"; Filename: "{app}\main.exe"
Name: "{userdesktop}\Matin Calculator"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional icons:"

[Run]
Filename: "{app}\main.exe"; Description: "Run Matin Calculator"; Flags: nowait postinstall skipifsilent