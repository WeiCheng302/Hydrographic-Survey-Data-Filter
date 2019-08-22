# Hydrographic-Survey-Data-Filter
This program is used to help the selection of Hydrographic Survey datas. 
Usually, there are many observations on one GPS position.
In this program, we tried only get one point depth value on one GPS position.

#### `delete.py`

First, it kicks out the big errors . Then select the value when the value whose GPS position changes from one to another.


#### `pola.py`
To interpolate thepoint file got from * delete.py *

