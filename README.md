# TeleExport
A dependency-free Python script that converts a Telegram JSON contact export to importable CSV and VCF files. It supports Windows and Linux, including Debian 12 and Debian 13.

## Debian 12 and 13

Python 3 is included in a standard Debian installation. No third-party Python packages are required.

1. Download `TeleExport.py` and place it next to Telegram's exported `result.json` file.
2. Open a terminal in that directory.
3. Run:

   ```sh
   python3 TeleExport.py
   ```

The command creates `contacts.csv` and `contacts.vcf`. You can also provide custom paths:

```sh
python3 TeleExport.py telegram-export.json --csv contacts.csv --vcf contacts.vcf
```

Alternatively, make the script directly executable with `chmod +x TeleExport.py`, then run `./TeleExport.py`.

## Export contacts from Telegram

For exporting telegram contacts list follow these steps:

0. Download the <a href="https://github.com/GlassesPi/TeleExport/blob/master/TeleExport.exe?raw=true">TeleExport.exe</a>

1. Go to Settings page of a desktop-based Telegram and select Advanced

![First Step](https://github.com/GlassesPi/TeleExport/blob/master/1st-step.png)

2. Go to Export Telegram Data section

![Second Step](https://github.com/GlassesPi/TeleExport/blob/master/2nd-step.png)

3. Uncheck all checkboxes except Contact List and select Machine-Readable JSON at the bottom of form

![Third Step](https://github.com/GlassesPi/TeleExport/blob/master/3rd-step.png)

![Fourth Step](https://github.com/GlassesPi/TeleExport/blob/master/4th-step.png)

![Fifth Step](https://github.com/GlassesPi/TeleExport/blob/master/5th-step.png)

4. After the exportation ends, click on SHOW MY DATA button to open exported files directory

![Sixth Step](https://github.com/GlassesPi/TeleExport/blob/master/6th-step.png)

![Seventh Step](https://github.com/GlassesPi/TeleExport/blob/master/7th-step.jpg)

5. Put `TeleExport.exe` (Windows) or `TeleExport.py` (Linux) next to `result.json` and run it. In a few seconds, CSV and VCF files will be generated.

![Eighth Step](https://github.com/GlassesPi/TeleExport/blob/master/8th-step.png)
