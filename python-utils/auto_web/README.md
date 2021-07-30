# auto_web
- Open a long list of URLs in the web browser orderly using two hotkeys
- Not need to copy and paste numerous URLs manually

## TODO
- [x] Modify settings (hotkeys & index & file name) in `settings.yaml`, separated from the main program `atm_web.py`
- [x] Support for the start point index and end point index of the URL list
- [x] Support for json file that stores URLs
- [ ] Add support for csv, txt, etc. files that store URLs
- [ ] Refactor and Redesign in OO design

## DEPENDENCIES
- `datproc` module for reading json file

## REQUIREMENTS
Currently, the env is listed as below:
```bash
  - pip:
    - keyboard==0.13.5
    - numpy==1.21.1
    - pandas==1.3.0
    - python-dateutil==2.8.2
    - pytz==2021.1
    - pyyaml==5.4.1
```