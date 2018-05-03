# Demo script
# Just using this to master/test my libraries

import trashtxtmode as ttm
import formatting as form
from trashtxtmode import colors as col
from time import sleep

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
sleep(1)

ttm.hline(1)
ttm.title("Hello, World!")
print(form.bold("This is a test."))
sleep(1)

ttm.hline(1)
print(form.fail("Fail"))
print(form.bold("Bold"))
print(form.head("Header"))
print(form.okblu("OK (Blue)"))
print(form.okgrn("OK (Green)"))
print(form.uline("Underlined"))
print(form.warn("Warning"))
sleep(1)

ttm.hline(1)
print(form.bold("Progress:"))
for i in range(1, 100):
    ttm.printprog(i)
    sleep(0.01)
    if i < 100:
        print("\r", end='')