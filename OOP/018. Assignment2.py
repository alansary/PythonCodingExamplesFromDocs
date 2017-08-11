#!/usr/bin/env python3

import datetime

log = LogFile('log.txt')
c = DelimFile('text.csv', ',')

log.write('this is a log message')
log.write('this is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])


dt_str = datetime.datetime.now().strftime('%y-%m-%d %H:%M')
writecsv = WriteFile('text2.csv', CSVFormatter)
writelog = WriteFile('log2.txt', LofFormatter)
writecsv.write(['a', 'b,2', 'c', 'd'])
writelog.write('this is a log message')
writecsv.write(['1', '2', '3', '4'])
writelog.write('this is another log message')
writecsv.close()
writelog.close()
class WriteFile(object);
	...
class LogFile(WriteFile):
	...
class DelimFile(WriteFile):
	...
