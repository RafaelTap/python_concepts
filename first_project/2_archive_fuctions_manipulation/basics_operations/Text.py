"""
classes numbers 1,2,3

ALL BASICS ARCHIVE MANIPULATION OPERATIONS
OPEN;
READ;
WRITE;
CLOSE.

ABSOLUT
the complete reference to found an archive or directory
. It must begin with / or a directory drive label

RELATIVE
is the complete reference to found an archive or directory
from another directory where the script is.

when we open an archive we need to tell python what we want
to do.

MAINS ACCESS MODES
r: read
w:write
a:append

when we want open a binary archive (image), we add the letter b
after mode.
rb, wb, ab.

'r'	open the archive to read (default).
'w'	open the archive to write, tricked it first.
'x'	create the archive to write and fails, if exists.
'a'	open the archive to write adding content to final if it exists.
'b'	binary mode.
't'	text mode.
'+'open the archive to update (read or write).

class number 4, 5, 6, 7

that are three ways to read a text document:
.read() -> return all content of an archive as an unic string.
.readLine() -> return one archive line including \n or \n\r and advance
the cursor to the next.
.readlines() -> return a list where each item from list is a archive line.






"""