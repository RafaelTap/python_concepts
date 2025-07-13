"""
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

'r'	open the achive to read (default).
'w'	open the archive to write, tricked it first.
'x'	creat the archive to write and fails, if exists.
'a'	open the archive to write adding content to final if it exists.
'b'	binary mode.
't'	text mode.
'+'open the archive to update (read or write).

"""