from cx_Freeze import setup, Executable

# Define executables
executables = [
    Executable('main.py', base='Win32GUI', icon='icon.ico')
]

# Setup parameters
setup(
    name='KanjiReader',
    version='1.0',
    description='KanjiReader Beta',
    executables=executables,
    options={
        'build_exe': {
            'packages': ['pynput.mouse._win32', 'pynput.keyboard._win32', 'sudachidict_core'],  # List of packages to include with the executable
            'include_files': ['Text.ui'],     # Additional files/directories to include
            'include_msvcr': True,   # Include MSVC runtime files (Microsoft Visual C++ Redistributable)
        }
    }
)
