# Demo script
# Just using this to master/test my libraries

import trashtxtmode as ttm
import formatting as form
from trashtxtmode import colors as col

print("Trying to autosize . . . ", end='')
ttm.forceupdate()
if ttm.tryautosize():
    print(col.OKGREEN+"Successful."+col.RESET)
    print("Size: {0} Columns, {1} Rows".format(str(ttm.columns), str(ttm.rows)))
else:
    print(col.FAIL+"Unsuccessful."+col.RESET)
    print("Setting size to defaults (80Cols*25Rows) . . . ", end='')
    ttm.forceupdate()
    ttm.columns = 80
    ttm.rows = 25
    print(col.OKBLUE+"Done."+col.RESET)

print("")
ttm.title("Hello, World!")
print(form.bold("This is a test."))
print("")
print(form.fail("Fail"))
print(form.bold("Bold"))
print(form.head("Header"))
print(form.okblu("OK (Blue)"))
print(form.okgrn("OK (Green)"))
print(form.uline("Underlined"))
print(form.warn("Warning"))