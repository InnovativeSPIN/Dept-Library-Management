from cx_Freeze import setup, Executable


includefiles = ["dataBase", "Assets"]  # include any files here that you wish
excludes = []
packages = []

exe = Executable(
    # what to build
    script="Main.py",  # the name of your main python script goes here
    init_script=None,
    base="Win32GUI",  # if creating a GUI instead of a console app, type "Win32GUI"
    target_name="Library Management System.exe",  # this is the name of the executable file
    icon="Assets/icon.ico"  # if you want to use an icon file, specify the file name here
)

setup(
    # the actual setup & the definition of other misc. info
    name="Library Management System",  # program name
    version="0.1",
    description='A library management system for Nadar Saraswathi College of Engineering and Technology',
    author="ISPIN",
    options={"build_exe": {"excludes": excludes, "packages": packages,
                           "include_files": includefiles}},
    executables=[exe]
)