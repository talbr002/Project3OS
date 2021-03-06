#! /usr/bin/env python
# archive management
#
# for this project you must implement the functionnality to store within a single file, multiple file
# the files must be in ascii (no binary) with no carriage return or newline in the file 
# no validation is required, only valid file in regard to content will be used
#
# the archive information is stored in ascii (no binary).  
# The filesize and blockid, will be store as ascii string, wtih each archiveentry and datablock on a newline.
#
# the name of the archive, is hardcoded to archive.dat and must be in the current directory
#
# Command Line
#
# just must create and initialize the archive file
# python project3.py  create
#

#
# add a file to the archive.
# python project3.py  add a.txt
#

#
# remove a file from the archive. 
# python project3.py  remove  a.txt
#

#
# list the files in the archives and display information on them.
# python project3.py  list
#

# Grade:
# add file: 40
# remove file: 30
# documentation of the tests you did + fileset used: 30
# 1st bonus: if your final submission is by nov 23 : 10 pts
# 2nd bonus: if your also support updating a file in the archive : 5 pts
#
# total: 115 / 100
#

#
#add you names !!!!  
#

from array import array

import sys

import time

import os

#maximum number of entry for files in the archive  and also for data blocks for the archive
MAX_ENTRY = 32

#maximum number of block for a single file archive entry
#a file cannot splan over multiple archiveentry
MAX_BLOCK_PER_FILE = 4

#maximum number of byte per datablock
MAX_BYTE_PER_DATABLOCK = 32

#maxium lenght for a file name
MAX_FILENAME = 8

#maximum number of characters used to store datablocks uses by a file
MAX_DIGIT_FOR_BLOCK = 2

#filesize will use a maximum of 3 digits
MAX_DIGIT_FOR_FILESIZE = 3

ARCHIVE_FILENAME = "archive.dat"

#datablock id starts at 1
class DataBlock:

     def __init__(self, id=0, data="", ):

         self.id    = id
         self.data  = "Z" * MAX_BYTE_PER_DATABLOCK

     def readFromArchive( self, id, line ):
         self.id   = id
         self.data = line

     def writeToArchive( self, file ):
	#MAX_BYTE_PER_DATABLOCK = 32
         file.write( self.data.ljust( MAX_BYTE_PER_DATABLOCK ) ) 
         file.write("\n")



#an empty archiveentry has a filename = ""
#the block entries is equal to 0, when it is not in used
class ArchiveEntry:

     def __init__(self, filename="", size=0, ):

         self.filename = filename
         self.size     = size
	 
         
         self.datablocks   = [0] * MAX_BLOCK_PER_FILE #4

     def readFromArchive( self, line ):
	#MAX_DIGIT_FOR_FILESIZE = 3
         self.size     = int(line[:MAX_DIGIT_FOR_FILESIZE])#int // take the first three characters of the line
	#storing
         self.filename = line[MAX_DIGIT_FOR_FILESIZE : MAX_DIGIT_FOR_FILESIZE + MAX_FILENAME]#str
         
     def writeToArchive( self, file ):
         file.write( str(self.size).zfill( MAX_DIGIT_FOR_FILESIZE ))
         file.write( self.filename.rjust( MAX_FILENAME + (len(self.filename) ) ))
         for idx in range(0, len( self.datablocks ) ) :
		#max_digit_for_block = 2
             file.write( str(self.datablocks[ idx ]).zfill( MAX_DIGIT_FOR_BLOCK  ) ) #this prints 2 zeros times 4
         file.write("\n")

     def list( self ):
         print self.filename.rjust( MAX_FILENAME ), 
         for idx in range(0, len( self.datablocks ) ) :
             print str(self.datablocks[ idx ]).zfill( MAX_DIGIT_FOR_BLOCK ), 
         print("\n")

     def isEmpty( self ):
         return len(self.filename) == 0

     def update(self, filename = '', size = 0):
         self.filename = filename
	 self.size = size

#     def WTA( self, file ):
#	 while():
 #            file.write(str(self.size).zfill( MAX_DIGIT_FOR_FILESIZE-(len(self.size) )
#	     print(len(self.filename))
#             file.write( self.filename.rjust( MAX_FILENAME - (len(self.filename) ) ) )
#             for idx in range(0, len( self.datablocks ) ) :
#                 file.write( str(self.datablocks[ idx ]).zfill( MAX_DIGIT_FOR_BLOCK ) )
#             file.write("\n")

class Archive:

     def __init__( self ):
        self.archiveEntries = []
        self.dataEntries = []
	for i in range(MAX_ENTRY):
		self.archiveEntries.append(ArchiveEntry())
		self.dataEntries.append(DataBlock())

#        self.archiveEntries = [ ArchiveEntry()] * MAX_ENTRY
#        self.dataEntries    = [ DataBlock()] * MAX_ENTRY
     
     def writeToArchive( self ) :
        archive = open( ARCHIVE_FILENAME, "w")

        for idx in range(0, MAX_ENTRY):
           self.archiveEntries[ idx ].writeToArchive( archive )

        for idx in range(0, MAX_ENTRY):
           self.dataEntries[ idx ].writeToArchive( archive )

        archive.close( )

     def readFromArchive( self ):
        archive = open( ARCHIVE_FILENAME, "r")

        count = 0
        datablockid = 1; # this is the index of the archive z data
        for line in archive:
            line = line.rstrip('\n')
            if count < MAX_ENTRY:
               self.archiveEntries[ count ].readFromArchive( line )
            else:
               self.dataEntries[ datablockid - 1 ].readFromArchive( datablockid, line )
               datablockid = datablockid + 1
            count = count + 1



     def list( self ):
        for idx in range(0, MAX_ENTRY):
            print("entry :" + str(idx) )
            if self.archiveEntries[ idx ].isEmpty():
               print(" empty")
            else :
               self.archiveEntries[ idx ].list()
        print("\n")
     
     def create( self ):
        self.writeToArchive();


#DataBlockEntry[index].readFromArchive(1, line)

     def addToArchive( self, filename ):
	if (len(filename) >8):
	    print("Error, filename must be less than 9 characters!")
	    exit()
	thefile = open( filename, "r")
	archive = open( ARCHIVE_FILENAME, "w")
	self.archiveEntries[0].update(filename, os.path.getsize(filename))
	self.dataEntries[0]
	
	#self.archiveEntries[0].readFromArchive(filename)

#	print(thefile.read())

#	self.dataEntries[0].readFromArchive(1, 'testing 101') 
#	self.dataEntries[0].writeToArchive(archive)
	
	
#	self.archiveEntries[0].writeToArchive(archive)
#	self.archiveEntries[0].update()
        # must do validation on
#	x = ArchiveEntry(filename, os.path.getsize(filename))

#	self.archiveEntries[0].writeToArchive(archive)
	
#	x.writeToArchive(thefile)
        # filename - done
        # filesize vs maximum allowed per file
        # filesize vs free space
        # filename must be unique (case sensitive)
        # the archiveentry allocated for the file must be the 1st available starting at idx = 0
        # the file must used the minimum set of datablock requires to store the file
        # the datablock allocated for the file must be the 1st available starting at idx = 0
        #
        print("not implemented, this is your assignment\n")

     def removeFromoArchive( self, filename ):
        # it must validate the file is or not in the archive and produce an error message
        #
        # remove a file from the archive. It will reset the archiveentry to the free state (filename="", size=0, datablocks=0)
        # and overwrite the data in the datablocks with 'Z's
        #

        print("not implemented, this is your assignment\n")

def createArchive():
     print("Creating Archive")
     Archive().create()

def addToArchive():
     filename = sys.argv[ 2 ];
     print("Adding to Archive:" + filename)
     archive = Archive()
     #archive.readFromArchive()
     archive.list()
     archive.addToArchive( filename )
     archive.list()
     archive.writeToArchive();

def removeFromArchive():
     filename = sys.argv[ 2 ];
     print("Removing from Archive:" + filename)
     archive = Archive()
     archive.readFromArchive()
     archive.list()
     archive.removeFromArchive( filename )
     archive.writeToArchive();

def listArchive():
     archive = Archive()
     archive.list()


#
# processing command
#
#
command  = sys.argv[ 1 ] 

print 'Processing command:' + command

if command == 'create' :
   createArchive()
elif command == 'add' :
   addToArchive()
elif command == 'remove' :
   removeFromArchive()
elif command == 'list' :
   listArchive()
else :
   print("Invalid command")


