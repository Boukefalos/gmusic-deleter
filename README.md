# Delete songs from Google Music that you deleted from iTunes

Google Music Manager can automatically upload songs from your local iTunes library to Google Music. When you delete songs from you iTunes library, however, they remain to exist in you Google Music library. This script automates the tedious process of deleting songs from Google Music manually.

## Installation
This script relies on [pyItunes][1] and [Unofficial-Google-Music-API][2]. Installation of these dependencies is easy using pip:
```
pip install -r requirements.txt
```

Windows users can install pip as follows:
```
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
```

## Configuration
Generate an application specific password for your google account: https://security.google.com/settings/security/apppasswords

Just alter the values in broken brackets and run the script:
```
python delete.py
```

  [1]: https://github.com/liamks/pyitunes
  [2]: https://github.com/simon-weber/Unofficial-Google-Music-API