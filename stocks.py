from Tkinter import *
import tkFont

root = Tk()
root.title( 'My Stock Portfolio' )

#Styles
HELVETICA12 = tkFont.Font( family = 'Helvetica', size = 12, weight = 'bold' )


#Settings
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

def doNothing():
    pass

addstockframe = Frame( root )

columnlist = [ 'Open', 'Date', 'Symbol', 'Event', 'Quantity', 'Price', 'Commission', 'Value', 'Notes', 'Calculate', '' ]
checklist = [ 'Open', 'Calculate' ]
radiolist = [ 'Event' ]
events = [ 'BUY', 'SELL' ]
valuelist = [ 'Quantity', 'Price', 'Commission', 'Value' ]
columns = len( columnlist )

column = {}
for c in range( columns ):
    column[ c ] = {}
    column[ c ][ 'label' ] = Label( addstockframe, text = columnlist[ c ] ).grid( row = 1, column = c, sticky = W )
    if columnlist[ c ] in checklist:
        column[ c ][ 'type' ] = Checkbutton( addstockframe ).grid( row = 2, column = c )
    elif columnlist[ c ] in radiolist:
        column[ c ][ 'type' ] = Frame( addstockframe )
        column[ c ][ 'type' ].grid( row = 2, column = c, sticky = W )
        for e in range( len( events ) ):
            Radiobutton( column[ c ][ 'type' ], text = events[ e ], value = events[ e ], variable = columnlist[ c ] ).grid( row = 0, column = e, sticky = W )           
    elif columnlist[ c ] in valuelist:
        column[ c ][ 'type' ] = Spinbox( addstockframe, width = 8 ).grid( row = 2, column = c, sticky = W )
    elif columnlist[ c ] == 'Notes':
        column[ c ][ 'type' ] = Entry( addstockframe ).grid( row = 2, column = c, sticky = W )
    elif columnlist[ c ] == '':
        column[ c ][ 'type' ] = Button( addstockframe, text = 'Add' ).grid( row = 2, column = c, sticky = W )
    else:
        column[ c ][ 'type' ] = Entry( addstockframe, width = 10 ).grid( row = 2, column = c, sticky = W )

#Form
Label( addstockframe, text = 'Add Stock', font = HELVETICA12 ).grid( row = 0, column = 0, sticky = W, columnspan = columns )
for c in range( columns ):
    column[ c ][ 'label' ]

for c in range( columns ):
    column[ c ][ 'type' ]

addstockframe.pack()



#Main Menu
menubar = Menu( root )
filemenu = Menu( menubar, tearoff = 0 )
filemenu.add_command( label = 'Import', command = doNothing )
filemenu.add_separator()
filemenu.add_command( label = 'Exit', command = doNothing )
menubar.add_cascade( label = "File", menu = filemenu )

viewmenu = Menu( menubar, tearoff = 0 )
viewmenu.add_command( label = 'Portfolio', command = doNothing )
viewmenu.add_command( label = 'Deposits', command = doNothing )

watchmenu = Menu( viewmenu, tearoff = 0 )
watchmenu.add_radiobutton( label = "CDN", variable = 'watchlist' )
watchmenu.add_radiobutton( label = "US", variable = 'watchlist' )
watchmenu.add_radiobutton( label = "Past", variable = 'watchlist' )
watchmenu.add_separator()
watchmenu.add_radiobutton( label = "Other...", variable = 'watchlist' )

viewmenu.add_cascade( label = 'Watch Lists', menu = watchmenu )
menubar.add_cascade( label = "View", menu = viewmenu )

stocksmenu = Menu( menubar, tearoff = 0 )
stocksmenu.add_command( label = 'Add', command = doNothing )
stocksmenu.add_command( label = 'Edit', command = doNothing )
menubar.add_cascade( label = "Stocks", menu = stocksmenu )

#Main Loop
root.config( menu = menubar )
root.geometry( "%dx%d+0+0" % ( w, h ) )
root.mainloop()
