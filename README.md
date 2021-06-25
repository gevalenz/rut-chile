# rut-chile
Python module that provides common functionality regarding Chilean RUT

[![Build Status](https://travis-ci.com/gevalenz/rut-chile.svg?token=K7zbkgBiGA3AKhLgGz8a&branch=master)](https://travis-ci.com/gevalenz/rut-chile)

# Installation
``` 
pip install rut_chile
```
or
```
git clone https://github.com/gevalenz/rut-chile.git

python setup.py install
```

# Usage
## Validate RUT
```
from rut_chile import rut_chile

rut_chile.is_valid_rut("12345678-9")
# returns False
rut_chile.is_valid_rut("6265837-1")
# returns True


# It works with the following formats

rut_chile.is_valid_rut("98685030")
# returns True
rut_chile.is_valid_rut("9868503-0")
# returns True
rut_chile.is_valid_rut("9.868.503-0")
# returns True
rut_chile.is_valid_rut("12.667.869-K")
# returns True
rut_chile.is_valid_rut("12.667.869-k")
# returns True
```

## Get verification digit

```
from rut_chile import rut_chile

rut_chile.get_verification_digit("9868503")
# returns "0"
rut_chile.get_verification_digit("12667869")
# returns "k"
rut_chile.get_capitalized_verification_digit("12667869")
# returns "K"
```

## Format RUT

```
from rut_chile import rut_chile

rut_chile.format_rut_with_dots("12667869k")
# returns "12.667.869-k"
rut_chile.format_rut_without_dots("12667869k")
# returns "12667869-k"
rut_chile.format_capitalized_rut_without_dots("12667869k")
# returns "12667869-K"
rut_chile.format_capitalized_rut_with_dots("12667869k")
# returns "12.667.869-K"
```
