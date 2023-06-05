import tkinter as tk
from tkinter import *
# import mysql.connector

resolution = (1020, 720)
root = tk.Tk()
bg = PhotoImage( file = "bg_r.png")
canvas = tk.Canvas(root, width = resolution[0], height = resolution[1])

canvas.pack() 
root.title("Cash And Carry")

customers = {}
products = {} 
sales = {}

buttoncolor = 'SeaGreen1'

activebackcolor = 'firebrick1'

activeforcolor = 'white'
displaycolor = 'orchid1'
framecolor = bg
foregroundcolor = 'black'
saleforegroundcolor = 'dodger blue'


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


def add_product_menu():
    
    add_frame = tk.Frame(root )
    add_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    lbl = tk.Label(add_frame,image = framecolor)
    lbl.place(x=0,y=0)
    label1 = tk.Label(add_frame, text = 'Enter Product Code : ' )
    label1.place(relx = 0.15, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    label2 = tk.Label(add_frame, text = 'Enter Product Name : ' )
    label2.place(relx = 0.15, rely = 0.2, relwidth = 0.3, relheight = 0.05)
    label3 = tk.Label(add_frame, text = 'Enter Product Price : ' )
    label3.place(relx = 0.15, rely = 0.3, relwidth = 0.3, relheight = 0.05)
    label4 = tk.Label(add_frame, text = 'Enter Category : ')
    label4.place(relx = 0.15, rely = 0.4, relwidth = 0.3, relheight = 0.05)


    entry1 = tk.Entry(add_frame, bg = buttoncolor)
    entry1.place(relx = 0.4, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    entry2 = tk.Entry(add_frame, bg = buttoncolor)
    entry2.place(relx = 0.4, rely = 0.2, relwidth = 0.3, relheight = 0.05)
    entry3 = tk.Entry(add_frame, bg = buttoncolor)
    entry3.place(relx = 0.4, rely = 0.3, relwidth = 0.3, relheight = 0.05)
    entry4 = tk.Entry(add_frame, bg = buttoncolor)
    entry4.place(relx = 0.4, rely = 0.4, relwidth = 0.3, relheight = 0.05)


    button_add = tk.Button(add_frame, text = 'ADD', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : add_product(entry1, entry2, entry3, entry4, add_frame))
    button_add.place(relx = 0.2, rely = 0.7, relwidth = 0.3, relheight = 0.08) 
    button_go_back = tk.Button(add_frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
    button_go_back.place(relx = 0.5, rely = 0.7, relwidth = 0.3, relheight = 0.08)




def add_product(entry1, entry2, entry3, entry4, add_frame):
    if entry1.get() and entry2.get() and entry3.get() and entry4.get():
        try:
            product_code = int(entry1.get())
        except:
            
            print('This Product Code has already been alotted to a Product, please use a different Product Code ')
            product_code = 'none'

        product_name = entry2.get()
        try:
            product_price = int(entry3.get())
        except:
            product_price = 'none'
        category = entry4.get()
        #check = input('Press 1 to add more products ')
        #if check != '1':
        #    break
        if product_code not in products.keys() and product_code != 'none' and product_price != 'none':
            products[product_code] = [product_name, product_price, category]
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            label = tk.Label(add_frame)
            label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
            label = tk.Label(add_frame, text = 'Product Added Successfully', bg = displaycolor)
            label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
                    
        else:
            if product_code == 'none' and product_price == 'none':
                label = tk.Label(add_frame, text = 'Product Code and Price Must only contain digits, Enter a Valid Numbers', bg = displaycolor)
                label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
            if product_price == 'none':
                label = tk.Label(add_frame, text = 'Product Price Must only contain digits, Enter a Valid Product Price', bg = displaycolor)
                label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
            elif product_code == 'none':
                label = tk.Label(add_frame, text = 'Product Code Must only contain digits, Enter a Valid Product Code', bg = displaycolor)
                label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)      
            else:
                print('This Product Code has already been alotted to a Product, please use a different Product Code ')
                label = tk.Label(add_frame, text = 'This Product Code has already been alotted to a Product, please use a different Product Code', bg = displaycolor)
                label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
        
    else:
        label = tk.Label(add_frame, text = 'Please Fill all Fields before Adding', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------








def view_product():

    view_frame = tk.Frame(root) 
    view_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(view_frame,image = framecolor)
    lbl.place(x=0,y=0)
    
    if products:
        labely = 0.3
        label1 = tk.Label(view_frame, text = 'Product Code', bg = displaycolor )
        label1.place(relx = 0.05, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label2 = tk.Label(view_frame, text = 'Product Name', bg = displaycolor )
        label2.place(relx = 0.23, rely = 0.2, relwidth = 0.3, relheight = 0.08)
        label3 = tk.Label(view_frame, text = 'Price', bg = displaycolor )
        label3.place(relx = 0.5, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label4 = tk.Label(view_frame, text = 'Category', bg = displaycolor )
        label4.place(relx = 0.7, rely = 0.2, relwidth = 0.24, relheight = 0.08)
        print('product Code\t\t\tproduct name\t\t\tprice\t\t\tcategory')
        for i in products.keys():
            lst = products[i]
            print(i,'\t\t\t', lst[0], '\t\t\t', lst[1], '\t\t\t', lst[2])
            label5 = tk.Label(view_frame, text = str(i), bg = displaycolor )
            label5.place(relx = 0.05, rely = labely, relwidth = 0.22, relheight = 0.08)
            label6 = tk.Label(view_frame, text = lst[0], bg = displaycolor )
            label6.place(relx = 0.23, rely = labely, relwidth = 0.3, relheight = 0.08)
            label7 = tk.Label(view_frame, text = lst[1], bg = displaycolor )
            label7.place(relx = 0.5, rely = labely, relwidth = 0.22, relheight = 0.08)
            label8 = tk.Label(view_frame, text = lst[2], bg = displaycolor )
            label8.place(relx = 0.7, rely = labely, relwidth = 0.24, relheight = 0.08)
            labely += 0.05
    else:
        print('No Products Record found')
        label = tk.Label(view_frame, text = 'No Products Record Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
    button_go_back = tk.Button(view_frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
    button_go_back.place(relx = 0.36, rely = 0.9, relwidth = 0.3, relheight = 0.08)
   

#--------------------------------------------------------------------------------------------------------------------------------------------------------------



#search
def search_product_menu():

    frame = tk.Frame(root) 
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)

    if products:
    #ask = eval(input('Enter the product code you want to search for '))

        label = tk.Label(frame, text = 'Enter Product Code : '   )
        label.place(relx = 0.15, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        entry = tk.Entry(frame, bg = buttoncolor)
        entry.place(relx = 0.4, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        button_add = tk.Button(frame, text = 'Search', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : product_search(entry, frame))
        button_add.place(relx = 0.2, rely = 0.7, relwidth = 0.3, relheight = 0.08) 
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
        button_go_back.place(relx = 0.5, rely = 0.7, relwidth = 0.3, relheight = 0.08)

    else:

        label = tk.Label(frame, text = 'No Products Record Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
        print('No products Record is there to be searched for, Please Add Products First')
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
        button_go_back.place(relx = 0.36, rely = 0.9, relwidth = 0.3, relheight = 0.08)



def product_search(entry, frame):

    try:
        productid = int(entry.get())
    except:
        productid = 'none'
    found = False
    lst = []
    for i in products.keys():
        if i == productid:
            lst = products[i]
            found = True
            break

    if found:

        label1 = tk.Label(frame, text = 'Searched Product Found', bg = displaycolor )
        label1.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.08)
        label2 = tk.Label(frame, text = 'Product Code', bg = displaycolor )
        label2.place(relx = 0.05, rely = 0.5, relwidth = 0.22, relheight = 0.08)
        label3 = tk.Label(frame, text = 'Product Name', bg = displaycolor )
        label3.place(relx = 0.23, rely = 0.5, relwidth = 0.3, relheight = 0.08)
        label4 = tk.Label(frame, text = 'Price', bg = displaycolor )
        label4.place(relx = 0.5, rely = 0.5, relwidth = 0.22, relheight = 0.08)
        label5 = tk.Label(frame, text = 'Category', bg = displaycolor )
        label5.place(relx = 0.7, rely = 0.5, relwidth = 0.24, relheight = 0.08)
        label6 = tk.Label(frame, text = str(productid), bg = displaycolor )
        label6.place(relx = 0.05, rely = 0.6, relwidth = 0.22, relheight = 0.08)
        label7 = tk.Label(frame, text = lst[0], bg = displaycolor )
        label7.place(relx = 0.23, rely = 0.6, relwidth = 0.3, relheight = 0.08)
        label8 = tk.Label(frame, text = lst[1], bg = displaycolor )
        label8.place(relx = 0.5, rely = 0.6, relwidth = 0.22, relheight = 0.08)
        label9 = tk.Label(frame, text = lst[2], bg = displaycolor )
        label9.place(relx = 0.7, rely = 0.6, relwidth = 0.24, relheight = 0.08)  
        entry.delete(0, 'end')   
        print('your searched code found')
        print('product Code\t\tproduct name\t\tprice\t\tproduct category')
        print(i,'\t\t', lst[0], '\t\t', lst[1], '\t\t', lst[2])



    else:

        label = tk.Label(frame, text = 'Your Search Product not Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.08)


        label2 = tk.Label(frame   )
        label2.place(relx = 0.05, rely = 0.5, relwidth = 0.22, relheight = 0.08)
        label3 = tk.Label(frame   )
        label3.place(relx = 0.23, rely = 0.5, relwidth = 0.3, relheight = 0.08)
        label4 = tk.Label(frame)
        label4.place(relx = 0.5, rely = 0.5, relwidth = 0.22, relheight = 0.08)
        label5 = tk.Label(frame   )
        label5.place(relx = 0.7, rely = 0.5, relwidth = 0.24, relheight = 0.08)
        label6 = tk.Label(frame   )
        label6.place(relx = 0.05, rely = 0.6, relwidth = 0.22, relheight = 0.08)
        label7 = tk.Label(frame   )
        label7.place(relx = 0.23, rely = 0.6, relwidth = 0.3, relheight = 0.08)
        label8 = tk.Label(frame   )
        label8.place(relx = 0.5, rely = 0.6, relwidth = 0.22, relheight = 0.08)
        label9 = tk.Label(frame   )
        label9.place(relx = 0.7, rely = 0.6, relwidth = 0.24, relheight = 0.08)
        entry.delete(0, 'end') 
        print('Your searched code not found')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------



def edit_product_menu():
    frame = tk.Frame(root  ) 
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)


    if products:
    #ask = eval(input('Enter the product code you want to search for '))

        label = tk.Label(frame, text = 'Enter Product Code : '   )
        label.place(relx = 0.03, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        entry = tk.Entry(frame, bg = buttoncolor)
        entry.place(relx = 0.28, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        button_add = tk.Button(frame, text = 'Search', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : edit_product_frame2(entry, frame))
        button_add.place(relx = 0.6, rely = 0.2, relwidth = 0.3, relheight = 0.05) 
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
        button_go_back.place(relx = 0.37, rely = 0.82, relwidth = 0.3, relheight = 0.08)

    else:

        label = tk.Label(frame, text = 'No Products Record Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
        print('No products Record is there to be searched for, Please Add Products First')
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
        button_go_back.place(relx = 0.36, rely = 0.82, relwidth = 0.3, relheight = 0.08)



def edit_product_frame2(entry, frame):

    try:
        productid = int(entry.get())
    except:
        productid = 'none'
    found = False
    lst = []
    for i in products.keys():
        if i == productid:
            lst = products[i]
            found = True
            break
    if found:

        label = tk.Label(frame, text = 'Editing Record For Product ID : ' + str(productid) , bg = displaycolor )
        label.place(relx = 0.05, rely = 0.28, relwidth = 0.9, relheight = 0.08)

        label1 = tk.Label(frame, text = 'Enter New Name : '   )
        label1.place(relx = 0.03, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        label2 = tk.Label(frame, text = 'Enter New Price : '   )
        label2.place(relx = 0.03, rely = 0.5, relwidth = 0.3, relheight = 0.05)
        label3 = tk.Label(frame, text = 'Enter New Category : '   )
        label3.place(relx = 0.03, rely = 0.6, relwidth = 0.3, relheight = 0.05)

        entry1 = tk.Entry(frame, bg = buttoncolor)
        entry1.place(relx = 0.28, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        entry2 = tk.Entry(frame, bg = buttoncolor)
        entry2.place(relx = 0.28, rely = 0.5, relwidth = 0.3, relheight = 0.05)
        entry3 = tk.Entry(frame, bg = buttoncolor)
        entry3.place(relx = 0.28, rely = 0.6, relwidth = 0.3, relheight = 0.05)

        button1 = tk.Button(frame, text = 'Update Name', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : edit_product_name(entry1, productid, frame))
        button1.place(relx = 0.6, rely = 0.4, relwidth = 0.3, relheight = 0.05) 
        button2 = tk.Button(frame, text = 'Update Price', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : edit_product_price(entry2, productid, frame))
        button2.place(relx = 0.6, rely = 0.5, relwidth = 0.3, relheight = 0.05) 
        button3= tk.Button(frame, text = 'Update Category', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : edit_product_category(entry3, productid, frame))
        button3.place(relx = 0.6, rely = 0.6, relwidth = 0.3, relheight = 0.05) 

    

    else:

        label = tk.Label(frame  )
        label.place(relx = 0.03, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        label = tk.Label(frame  )
        label.place(relx = 0.03, rely = 0.5, relwidth = 0.3, relheight = 0.05)
        label = tk.Label(frame  )
        label.place(relx = 0.03, rely = 0.6, relwidth = 0.3, relheight = 0.05)

        label = tk.Label(frame  )
        label.place(relx = 0.28, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        label = tk.Label(frame  )
        label.place(relx = 0.28, rely = 0.5, relwidth = 0.3, relheight = 0.05)
        label = tk.Label(frame  )
        label.place(relx = 0.28, rely = 0.6, relwidth = 0.3, relheight = 0.05)

        label = tk.Label(frame  )
        label.place(relx = 0.6, rely = 0.4, relwidth = 0.3, relheight = 0.05) 
        label = tk.Label(frame  )
        label.place(relx = 0.6, rely = 0.5, relwidth = 0.3, relheight = 0.05) 
        label= tk.Label(frame  )
        label.place(relx = 0.6, rely = 0.6, relwidth = 0.3, relheight = 0.05)       

        label = tk.Label(frame, text = 'Your Search Product not Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.28, relwidth = 0.9, relheight = 0.08)

        label = tk.Label(frame   )
        label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)

    button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
    button_go_back.place(relx = 0.37, rely = 0.82, relwidth = 0.3, relheight = 0.08)

    label = tk.Label(frame   )
    label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)

    

    entry.delete(0, 'end')



def edit_product_name(entry, productid, frame):
        new_name = entry.get()
        products[productid][0] = new_name 
        label = tk.Label(frame, text = 'Product Name of Product Code : ' + str(productid) +' has been Replaced with ' + new_name, bg = displaycolor )
        label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)
        entry.delete(0, 'end')


def edit_product_price(entry, productid, frame):
        new_price = entry.get()
        products[productid][1] = new_price 
        label = tk.Label(frame, text = 'Price of Product Code : ' + str(productid) +' has been Replaced with ' + new_price, bg = displaycolor )
        label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)
        entry.delete(0, 'end')


def edit_product_category(entry, productid, frame):
        new_category = entry.get()
        products[productid][2] = new_category 
        label = tk.Label(frame, text = 'Category of Product Code : ' + str(productid) +' has been Replaced with ' + new_category, bg = displaycolor )
        label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)
        entry.delete(0, 'end')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------


def delete_product_menu():
    frame = tk.Frame(root  ) 
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)
    if products:
    #ask = eval(input('Enter the product code you want to search for '))

        label = tk.Label(frame, text = 'Enter Product : '   )
        label.place(relx = 0.15, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        entry = tk.Entry(frame, bg = buttoncolor)
        entry.place(relx = 0.4, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        button_add = tk.Button(frame, text = 'Delete', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : product_delete(entry, frame))
        button_add.place(relx = 0.2, rely = 0.7, relwidth = 0.3, relheight = 0.08) 
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
        button_go_back.place(relx = 0.5, rely = 0.7, relwidth = 0.3, relheight = 0.08)

    else:
        label = tk.Label(frame, text = 'No Product Record is there to be Deleted', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
        print('No Product Record is there to be searched for, Please Add products First')
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
        button_go_back.place(relx = 0.36, rely = 0.9, relwidth = 0.3, relheight = 0.08)



def product_delete(entry, frame):
    try:
        productid = int(entry.get())
    except:
        productid = 'none'
    found = False
    lst = []
    for i in products.keys():
        if i == productid:
            lst = products[i]
            found = True
            break

    if found:
        products.pop(productid)
        label = tk.Label(frame, text = 'Product Record of product ID :' + str(productid) + ' has been Deleted ' , bg = displaycolor )
        label.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.08)  


    else:
        label = tk.Label(frame, text = 'Your Searched Product not Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.08)

    entry.delete(0, 'end') 




#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def product_menu():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0) 

    button1 = tk.Button(frame, text = 'Add Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = add_product_menu)
    button1.place(relx = 0.36, rely = 0.2, relwidth = 0.3, relheight = 0.08) 

    button2 = tk.Button(frame, text = 'View Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = view_product)
    button2.place(relx = 0.36, rely = 0.3, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Search for Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = search_product_menu)
    button3.place(relx = 0.36, rely = 0.4, relwidth = 0.3, relheight = 0.08)    

    button4 = tk.Button(frame, text = 'Edit Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = edit_product_menu)
    button4.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08)
    
    button5 = tk.Button(frame, text = 'Delete Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = delete_product_menu)
    button5.place(relx = 0.36, rely = 0.6, relwidth = 0.3, relheight = 0.08)

    button6 = tk.Button(frame, text = 'Go Back', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button6.place(relx = 0.36, rely = 0.7, relwidth = 0.3, relheight = 0.08) 

    label = tk.Label(frame, text ='          CENTRAL PERK CASH AND CARRY          ', bg = displaycolor )
    label.pack()

def customer_product_menu():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0) 

    # button1 = tk.Button(frame, text = 'Add Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = add_product_menu)
    # button1.place(relx = 0.36, rely = 0.2, relwidth = 0.3, relheight = 0.08) 

    # button2 = tk.Button(frame, text = 'View Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = view_product)
    # button2.place(relx = 0.36, rely = 0.3, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Search for Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = search_product_menu)
    button3.place(relx = 0.36, rely = 0.4, relwidth = 0.3, relheight = 0.08)    

    # button4 = tk.Button(frame, text = 'Edit Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = edit_product_menu)
    # button4.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08)
    
    # button5 = tk.Button(frame, text = 'Delete Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = delete_product_menu)
    # button5.place(relx = 0.36, rely = 0.6, relwidth = 0.3, relheight = 0.08)

    button6 = tk.Button(frame, text = 'Go Back', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customerframe)
    button6.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08) 

    label = tk.Label(frame, text ='          CENTRAL PERK CASH AND CARRY          ', bg = displaycolor )
    label.pack()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


def add_customer_menu():
    
    add_frame = tk.Frame(root  )
    add_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    lbl = tk.Label(add_frame,image = framecolor)
    lbl.place(x=0,y=0)
    label1 = tk.Label(add_frame, text = 'Enter Customer ID : '   )
    label1.place(relx = 0.15, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    label2 = tk.Label(add_frame, text = 'Enter Customer Name : '   )
    label2.place(relx = 0.15, rely = 0.2, relwidth = 0.3, relheight = 0.05)
    label3 = tk.Label(add_frame, text = 'Enter Phone no. : '   )
    label3.place(relx = 0.15, rely = 0.3, relwidth = 0.3, relheight = 0.05)
    label4 = tk.Label(add_frame, text = 'Enter email: '   )
    label4.place(relx = 0.15, rely = 0.4, relwidth = 0.3, relheight = 0.05)
    label5 = tk.Label(add_frame, text = 'Enter zip code: '   )
    label5.place(relx = 0.15, rely = 0.5, relwidth = 0.3, relheight = 0.05)


    entry1 = tk.Entry(add_frame, bg = buttoncolor)
    entry1.place(relx = 0.4, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    entry2 = tk.Entry(add_frame, bg = buttoncolor)
    entry2.place(relx = 0.4, rely = 0.2, relwidth = 0.3, relheight = 0.05)
    entry3 = tk.Entry(add_frame, bg = buttoncolor)
    entry3.place(relx = 0.4, rely = 0.3, relwidth = 0.3, relheight = 0.05)
    entry4 = tk.Entry(add_frame, bg = buttoncolor)
    entry4.place(relx = 0.4, rely = 0.4, relwidth = 0.3, relheight = 0.05)
    entry5 = tk.Entry(add_frame, bg = buttoncolor)
    entry5.place(relx = 0.4, rely = 0.5, relwidth = 0.3, relheight = 0.05)
    


    button_add = tk.Button(add_frame, text = 'ADD', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : add_customer(entry1, entry2, entry3, entry4, entry5, add_frame))
    button_add.place(relx = 0.2, rely = 0.7, relwidth = 0.3, relheight = 0.08) 
    button_go_back = tk.Button(add_frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
    button_go_back.place(relx = 0.5, rely = 0.7, relwidth = 0.3, relheight = 0.08)




def add_customer(entry1, entry2, entry3, entry4, entry5,add_frame):
    if entry1.get() and entry2.get() and entry3.get() and entry4.get():

        try:
            customerid = int(entry1.get())
        except:
            customerid = 'none'

        customer_name = entry2.get()
        phoneno = entry3.get()
        address = entry4.get()
        #check = input('Press 1 to add more products ')
        #if check != '1':
        #    break
        if customerid not in customers.keys() and customerid != 'none':
            customers[customerid] = [customer_name, phoneno, address]
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            entry5.delete(0, 'end')
            label = tk.Label(add_frame  )
            label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
            label = tk.Label(add_frame, text = 'Customer Added Successfully', bg = displaycolor)
            label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)

        else:
            if customerid == 'none':
                label = tk.Label(add_frame, text = 'Customer ID must contain digits only, please use a different Customer ID', bg = displaycolor)
                label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
            else:
                print('This Customer ID has already been alotted to a Customer, please use a different Customer ID ')
                label = tk.Label(add_frame, text = 'This Customer ID has already been alotted to a Customer, please use a different Customer ID', bg = displaycolor)
                label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
        
    else:
        label = tk.Label(add_frame, text = 'Please Fill all Fields before Adding', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def view_customer():
    view_frame = tk.Frame(root  ) 
    view_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(view_frame,image = framecolor)
    lbl.place(x=0,y=0)
    
    if customers:
        labely = 0.3
        label1 = tk.Label(view_frame, text = 'Customer ID', bg = displaycolor )
        label1.place(relx = 0.05, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label2 = tk.Label(view_frame, text = 'Customer Name', bg = displaycolor )
        label2.place(relx = 0.23, rely = 0.2, relwidth = 0.3, relheight = 0.08)
        label3 = tk.Label(view_frame, text = 'Phone Number', bg = displaycolor )
        label3.place(relx = 0.5, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label4 = tk.Label(view_frame, text = 'Email', bg = displaycolor )
        label4.place(relx = 0.7, rely = 0.2, relwidth = 0.24, relheight = 0.08)
        print('Customer Code\t\t\t name\t\t\tphoneno\t\t\tEmail')
        for i in customers.keys():
            lst = customers[i]
            print(i,'\t\t\t', lst[0], '\t\t\t', lst[1], '\t\t\t', lst[2])
            label5 = tk.Label(view_frame, text = str(i), bg = displaycolor )
            label5.place(relx = 0.05, rely = labely, relwidth = 0.22, relheight = 0.08)
            label6 = tk.Label(view_frame, text = lst[0], bg = displaycolor )
            label6.place(relx = 0.23, rely = labely, relwidth = 0.3, relheight = 0.08)
            label7 = tk.Label(view_frame, text = lst[1], bg = displaycolor )
            label7.place(relx = 0.5, rely = labely, relwidth = 0.22, relheight = 0.08)
            label8 = tk.Label(view_frame, text = lst[2], bg = displaycolor )
            label8.place(relx = 0.7, rely = labely, relwidth = 0.24, relheight = 0.08)
            labely += 0.05
    else:
        print('No Customers Record found')
        label = tk.Label(view_frame, text = 'No Customers Record Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
    button_go_back = tk.Button(view_frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
    button_go_back.place(relx = 0.36, rely = 0.9, relwidth = 0.3, relheight = 0.08)
   

#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#search
def search_customer_menu():
    frame = tk.Frame(root  ) 
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)
    if customers:
    #ask = eval(input('Enter the product code you want to search for '))

        label = tk.Label(frame, text = 'Enter Customer ID: '   )
        label.place(relx = 0.15, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        entry = tk.Entry(frame, bg = buttoncolor)
        entry.place(relx = 0.4, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        button_add = tk.Button(frame, text = 'Search', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : customer_search(entry, frame))
        button_add.place(relx = 0.2, rely = 0.7, relwidth = 0.3, relheight = 0.08) 
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
        button_go_back.place(relx = 0.5, rely = 0.7, relwidth = 0.3, relheight = 0.08)

    else:
        label = tk.Label(frame, text = 'No Customer Record Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
        print('No Customer Record is there to be searched for, Please Add Customers First')
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
        button_go_back.place(relx = 0.36, rely = 0.9, relwidth = 0.3, relheight = 0.08)


def customer_search(entry, frame):
    try:
        customerid = int(entry.get())
    except:
        customerid = 'none'
    found = False
    lst = []
    for i in customers.keys():
        if i == customerid:
            lst = customers[i]
            found = True
            break

    if found:
        label1 = tk.Label(frame, text = 'Searched Customer Found', bg = displaycolor )
        label1.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.08)
        label2 = tk.Label(frame, text = 'Customer ID', bg = displaycolor )
        label2.place(relx = 0.05, rely = 0.5, relwidth = 0.22, relheight = 0.08)
        label3 = tk.Label(frame, text = 'Customer Name', bg = displaycolor )
        label3.place(relx = 0.23, rely = 0.5, relwidth = 0.3, relheight = 0.08)
        label4 = tk.Label(frame, text = 'Phone Number', bg = displaycolor )
        label4.place(relx = 0.5, rely = 0.5, relwidth = 0.22, relheight = 0.08)
        label5 = tk.Label(frame, text = 'Address', bg = displaycolor )
        label5.place(relx = 0.7, rely = 0.5, relwidth = 0.24, relheight = 0.08)
        label6 = tk.Label(frame, text = str(customerid), bg = displaycolor )
        label6.place(relx = 0.05, rely = 0.6, relwidth = 0.22, relheight = 0.08)
        label7 = tk.Label(frame, text = lst[0], bg = displaycolor )
        label7.place(relx = 0.23, rely = 0.6, relwidth = 0.3, relheight = 0.08)
        label8 = tk.Label(frame, text = lst[1], bg = displaycolor )
        label8.place(relx = 0.5, rely = 0.6, relwidth = 0.22, relheight = 0.08)
        label9 = tk.Label(frame, text = lst[2], bg = displaycolor )
        label9.place(relx = 0.7, rely = 0.6, relwidth = 0.24, relheight = 0.08)  
          



    else:
        label = tk.Label(frame, text = 'Your Searched Customer not Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.08)

        label2 = tk.Label(frame   )
        label2.place(relx = 0.05, rely = 0.5, relwidth = 0.22, relheight = 0.08)
        label3 = tk.Label(frame   )
        label3.place(relx = 0.23, rely = 0.5, relwidth = 0.3, relheight = 0.08)
        label4 = tk.Label(frame   )
        label4.place(relx = 0.5, rely = 0.5, relwidth = 0.22, relheight = 0.08)
        label5 = tk.Label(frame   )
        label5.place(relx = 0.7, rely = 0.5, relwidth = 0.24, relheight = 0.08)
        label6 = tk.Label(frame   )
        label6.place(relx = 0.05, rely = 0.6, relwidth = 0.22, relheight = 0.08)
        label7 = tk.Label(frame   )
        label7.place(relx = 0.23, rely = 0.6, relwidth = 0.3, relheight = 0.08)
        label8 = tk.Label(frame   )
        label8.place(relx = 0.5, rely = 0.6, relwidth = 0.22, relheight = 0.08)
        label9 = tk.Label(frame   )
        label9.place(relx = 0.7, rely = 0.6, relwidth = 0.24, relheight = 0.08)

    entry.delete(0, 'end') 





#---------------------------------------------------------------------------------------------------------------------------------------------------------------


def edit_customer_menu():
    frame = tk.Frame(root  ) 
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)


    if customers:
    #ask = eval(input('Enter the customer code you want to search for '))

        label = tk.Label(frame, text = 'Enter Customer Code : '   )
        label.place(relx = 0.03, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        entry = tk.Entry(frame, bg = buttoncolor)
        entry.place(relx = 0.28, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        button_add = tk.Button(frame, text = 'Search', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : edit_customer_frame2(entry, frame))
        button_add.place(relx = 0.6, rely = 0.2, relwidth = 0.3, relheight = 0.05) 
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
        button_go_back.place(relx = 0.37, rely = 0.82, relwidth = 0.3, relheight = 0.08)

    else:

        label = tk.Label(frame, text = 'No Customers Record Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
        print('No Customers Record is there to be searched for, Please Add Customers First')
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
        button_go_back.place(relx = 0.36, rely = 0.82, relwidth = 0.3, relheight = 0.08)



def edit_customer_frame2(entry, frame):

    try:
        customerid = int(entry.get())
    except:
        customerid = 'none'
    found = False
    lst = []
    for i in customers.keys():
        if i == customerid:
            lst = customers[i]
            found = True
            break
    if found:

        label = tk.Label(frame, text = 'Editing Record For Customer ID : ' + str(customerid) , bg = displaycolor )
        label.place(relx = 0.05, rely = 0.28, relwidth = 0.9, relheight = 0.08)

        label1 = tk.Label(frame, text = 'Enter New Name : '   )
        label1.place(relx = 0.03, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        label2 = tk.Label(frame, text = 'Enter New Price : '   )
        label2.place(relx = 0.03, rely = 0.5, relwidth = 0.3, relheight = 0.05)
        label3 = tk.Label(frame, text = 'Enter New Category : '   )
        label3.place(relx = 0.03, rely = 0.6, relwidth = 0.3, relheight = 0.05)

        entry1 = tk.Entry(frame, bg = buttoncolor)
        entry1.place(relx = 0.28, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        entry2 = tk.Entry(frame, bg = buttoncolor)
        entry2.place(relx = 0.28, rely = 0.5, relwidth = 0.3, relheight = 0.05)
        entry3 = tk.Entry(frame, bg = buttoncolor)
        entry3.place(relx = 0.28, rely = 0.6, relwidth = 0.3, relheight = 0.05)

        button1 = tk.Button(frame, text = 'Update Name', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : edit_customer_name(entry1, customerid, frame))
        button1.place(relx = 0.6, rely = 0.4, relwidth = 0.3, relheight = 0.05) 
        button2 = tk.Button(frame, text = 'Update Price', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : edit_customer_price(entry2, customerid, frame))
        button2.place(relx = 0.6, rely = 0.5, relwidth = 0.3, relheight = 0.05) 
        button3= tk.Button(frame, text = 'Update Category', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : edit_customer_category(entry3, customerid, frame))
        button3.place(relx = 0.6, rely = 0.6, relwidth = 0.3, relheight = 0.05) 

    

    else:

        label = tk.Label(frame  )
        label.place(relx = 0.03, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        label = tk.Label(frame  )
        label.place(relx = 0.03, rely = 0.5, relwidth = 0.3, relheight = 0.05)
        label = tk.Label(frame  )
        label.place(relx = 0.03, rely = 0.6, relwidth = 0.3, relheight = 0.05)

        label = tk.Label(frame  )
        label.place(relx = 0.28, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        label = tk.Label(frame  )
        label.place(relx = 0.28, rely = 0.5, relwidth = 0.3, relheight = 0.05)
        label = tk.Label(frame  )
        label.place(relx = 0.28, rely = 0.6, relwidth = 0.3, relheight = 0.05)

        label = tk.Label(frame  )
        label.place(relx = 0.6, rely = 0.4, relwidth = 0.3, relheight = 0.05) 
        label = tk.Label(frame  )
        label.place(relx = 0.6, rely = 0.5, relwidth = 0.3, relheight = 0.05) 
        label= tk.Label(frame  )
        label.place(relx = 0.6, rely = 0.6, relwidth = 0.3, relheight = 0.05)       

        label = tk.Label(frame, text = 'Your Searched Customer not Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.28, relwidth = 0.9, relheight = 0.08)

        label = tk.Label(frame   )
        label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)

    button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
    button_go_back.place(relx = 0.37, rely = 0.82, relwidth = 0.3, relheight = 0.08)

    label = tk.Label(frame   )
    label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)

    

    entry.delete(0, 'end')



def edit_customer_name(entry, customerid, frame):
        new_name = entry.get()
        customers[customerid][0] = new_name 
        label = tk.Label(frame, text = 'Customer Name of Customer Code : ' + str(customerid) +' has been Replaced with ' + new_name, bg = displaycolor )
        label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)
        entry.delete(0, 'end')


def edit_customer_price(entry, customerid, frame):
        new_price = entry.get()
        customers[customerid][1] = new_price 
        label = tk.Label(frame, text = 'Price of Customer Code : ' + str(customerid) +' has been Replaced with ' + new_price, bg = displaycolor )
        label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)
        entry.delete(0, 'end')


def edit_customer_category(entry, customerid, frame):
        new_category = entry.get()
        customers[customerid][2] = new_category 
        label = tk.Label(frame, text = 'Category of Customer Code : ' + str(customerid) +' has been Replaced with ' + new_category, bg = displaycolor )
        label.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.08)
        entry.delete(0, 'end')



#---------------------------------------------------------------------------------------------------------------------------------------------------------------


def delete_customer_menu():
    frame = tk.Frame(root  ) 
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)
    if customers:
    #ask = eval(input('Enter the product code you want to search for '))

        label = tk.Label(frame, text = 'Enter Customer : '   )
        label.place(relx = 0.15, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        entry = tk.Entry(frame, bg = buttoncolor)
        entry.place(relx = 0.4, rely = 0.2, relwidth = 0.3, relheight = 0.05)
        button_add = tk.Button(frame, text = 'Delete', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : customer_delete(entry, frame))
        button_add.place(relx = 0.2, rely = 0.7, relwidth = 0.3, relheight = 0.08) 
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
        button_go_back.place(relx = 0.5, rely = 0.7, relwidth = 0.3, relheight = 0.08)

    else:
        label = tk.Label(frame, text = 'No Customer Record is there to be Deleted', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
        print('No Customer Record is there to be searched for, Please Add Customers First')
        button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
        button_go_back.place(relx = 0.36, rely = 0.9, relwidth = 0.3, relheight = 0.08)



def customer_delete(entry, frame):
    try:
        customerid = int(entry.get())
    except:
        customerid = 'none'
    found = False
    lst = []
    for i in customers.keys():
        if i == customerid:
            lst = customers[i]
            found = True
            break

    if found:
        customers.pop(customerid)
        label = tk.Label(frame, text = 'Customer Record of Customer ID :' + str(customerid) + ' has been Deleted ' , bg = displaycolor )
        label.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.08)  


    else:
        label = tk.Label(frame, text = 'Your Searched Customer not Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.08)

    entry.delete(0, 'end') 



#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def customer_menu():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)

    button1 = tk.Button(frame, text = 'Add Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = add_customer_menu)
    button1.place(relx = 0.36, rely = 0.2, relwidth = 0.3, relheight = 0.08) 

    button2 = tk.Button(frame, text = 'View Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = view_customer)
    button2.place(relx = 0.36, rely = 0.3, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Search for Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = search_customer_menu)
    button3.place(relx = 0.36, rely = 0.4, relwidth = 0.3, relheight = 0.08)    

    button4 = tk.Button(frame, text = 'Edit Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = edit_customer_menu)
    button4.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08)

    button5 = tk.Button(frame, text = 'Delete Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = delete_customer_menu)
    button5.place(relx = 0.36, rely = 0.6, relwidth = 0.3, relheight = 0.08)

    button6 = tk.Button(frame, text = 'Go Back', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button6.place(relx = 0.36, rely = 0.7, relwidth = 0.3, relheight = 0.08) 

    label = tk.Label(frame, text ='          CENTRAL PERK CASH AND CARRY          ', bg = displaycolor )
    label.pack()

def custome():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)

    button1 = tk.Button(frame, text = 'Add Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = add_customer_menu)
    button1.place(relx = 0.36, rely = 0.2, relwidth = 0.3, relheight = 0.08) 

    button2 = tk.Button(frame, text = 'View Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = view_customer)
    button2.place(relx = 0.36, rely = 0.3, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Search for Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = search_customer_menu)
    button3.place(relx = 0.36, rely = 0.4, relwidth = 0.3, relheight = 0.08)    

    button4 = tk.Button(frame, text = 'Edit Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = edit_customer_menu)
    button4.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08)

    button5 = tk.Button(frame, text = 'Delete Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = delete_customer_menu)
    button5.place(relx = 0.36, rely = 0.6, relwidth = 0.3, relheight = 0.08)

    button6 = tk.Button(frame, text = 'Go Back', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button6.place(relx = 0.36, rely = 0.7, relwidth = 0.3, relheight = 0.08) 

    label = tk.Label(frame, text ='          CENTRAL PERK CASH AND CARRY          ', bg = displaycolor )
    label.pack()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------------------------------------------------------------------------------------------------


'''def add_sales_menu():
    add_frame = tk.Frame(root  )
    add_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    if not products and customers:
        if not products:
            
        else:'''



def add_sales_menu():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0) 
    if not products and not customers:
        label = tk.Label(frame, text = 'No Products and Customers Record Found, Please Add Records First', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
    elif not products:
        label = tk.Label(frame, text = 'No Products Record Found, Please Add Products First', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)
    elif not customers:
        label = tk.Label(frame, text = 'No Customers Record Found, Please Add Customers First', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)

    else:
        label = tk.Label(frame, text = 'Enter Customer ID : '   )
        label.place(relx = 0.03, rely = 0.3, relwidth = 0.3, relheight = 0.05)
        entry1 = tk.Entry(frame, bg = buttoncolor)
        entry1.place(relx = 0.28, rely = 0.3, relwidth = 0.3, relheight = 0.05)
        button1 = tk.Button(frame, text = 'Enter', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : add_sales_frame2(entry1, frame))
        button1.place(relx = 0.6, rely = 0.3, relwidth = 0.3, relheight = 0.05)

    button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button_go_back.place(relx = 0.36, rely = 0.7, relwidth = 0.3, relheight = 0.08)



def add_sales_frame2(entry, frame):
    
    try:
        customerid = int(entry.get())
    except:
        customerid = 'none'

    if customerid in customers.keys() :

        label = tk.Label(frame, text = 'Enter Sales ID : '   )
        label.place(relx = 0.03, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        entry2 = tk.Entry(frame, bg = buttoncolor)
        entry2.place(relx = 0.28, rely = 0.4, relwidth = 0.3, relheight = 0.05)
        button2 = tk.Button(frame, text = 'Enter', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : add_sales_frame3(customerid, entry2, frame))
        button2.place(relx = 0.6, rely = 0.4, relwidth = 0.3, relheight = 0.05) 

    else:

        label = tk.Label(frame, text = 'Customer ID not found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
        entry.delete(0, 'end')


def add_sales_frame3(customerid, salesid, frame):
    productdict = {}
    try:
        salesid = int(salesid.get())
    except:
        salesid = 'none'

    if salesid not in sales.keys() and salesid != 'none':
        newframe = tk.Frame(root  )
        newframe.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        lbl = tk.Label(newframe,image = framecolor)
        lbl.place(x=0,y=0) 

        label = tk.Label(newframe, text = 'Enter Product ID'  )
        label.place(relx = 0.1, rely = 0.3, relwidth = 0.3, relheight = 0.05)
        label = tk.Label(newframe, text = 'Enter Quantity'  )
        label.place(relx = 0.1, rely = 0.4, relwidth = 0.3, relheight = 0.05)

        entry1 = tk.Entry(newframe, bg = buttoncolor)
        entry1.place(relx = 0.5, rely = 0.3, relwidth = 0.3, relheight = 0.05)
        entry2 = tk.Entry(newframe, bg = buttoncolor)
        entry2.place(relx = 0.5, rely = 0.4, relwidth = 0.3, relheight = 0.05)

        button_1 = tk.Button(newframe, text = 'ADD Product', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : add_sale_product(salesid, customerid, entry1, entry2, newframe, productdict))
        button_1.place(relx = 0.2, rely = 0.7, relwidth = 0.3, relheight = 0.08) 
        button_go_back = tk.Button(newframe, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = sale_menu)
        button_go_back.place(relx = 0.5, rely = 0.7, relwidth = 0.3, relheight = 0.08)

    else:
        if salesid == 'none':
            label = tk.Label(frame, text = 'Sales ID must contain digits only, Enter Valid Sales ID', bg = displaycolor )
            label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
        else:
            label = tk.Label(frame, text = 'This Sales ID has already been alotted to a customer, please add some other ID', bg = displaycolor )
            label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)



def add_sale_product(salesid, customerid, entry1, entry2, newframe, productdict):
    
    try:
        productid = int(entry1.get())
    except:
        productid = 'none'
    try:
        quantity = int(entry2.get())
    except:
        quantity = 'none'

    if productid in products.keys() and quantity != 'none':
        total_price = products[productid][1] * quantity
        productdict[productid] = [products[productid][0], products[productid][1], quantity, total_price]
        button = tk.Button(newframe, text = 'Confirm Sale', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : add_sale(salesid, customerid, productdict))
        button.place(relx = 0.2, rely = 0.8, relwidth = 0.6, relheight= 0.08)

        label = tk.Label(newframe, text = 'Product Added Successfully', bg = displaycolor)
        label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)


    else:
        if quantity == 'none' :
            label = tk.Label(newframe, text = 'Quantity must contain digits only', bg = displaycolor)
            label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
        else:
            label = tk.Label(newframe, text = 'This Product is not available', bg = displaycolor )
            label.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.08)
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')


def add_sale(salesid, customerid, productdict):
    totalbill = 0
    for i in productdict.keys():
        totalbill += productdict[i][3]
    sales[salesid] = [customerid, totalbill, productdict]

    new_frame = tk.Frame(root  )
    new_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(new_frame,image = framecolor)
    lbl.place(x=0,y=0)

    label = tk.Label(new_frame, text = 'Sale Record of Customer ID : ' + str(customerid) + ' has been added', bg = displaycolor)
    label.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.08)
    button1 = tk.Button(new_frame, text = 'Add More Sales', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = add_sales_menu)
    button1.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08)
    button1 = tk.Button(new_frame, text = 'Go to Sale Menu', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = sale_menu)
    button1.place(relx = 0.36, rely = 0.6, relwidth = 0.3, relheight = 0.08)
    print(sales)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------


def view_sale():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)
    index = 0
    if sales:
        key = []
        for i in sales.keys():
            key.append(i)

        label = tk.Label(frame, text = 'Sale ID : ' + str(key[index]), bg = displaycolor)
        label.place(relx = 0.05, rely= 0.07, relwidth = 0.24, relheight = 0.08)
        label = tk.Label(frame, text = 'Customer ID : ' + str(sales[key[index]][0]), bg = displaycolor)
        label.place(relx = 0.7, rely= 0.07, relwidth = 0.24, relheight = 0.08)

        label = tk.Label(frame, text = 'CENTRAL PERK C&C', bg = displaycolor)
        label.place(relx = 0.29, rely = 0.07, relheight = 0.15, relwidth = 0.41)

        label = tk.Label(frame, text = 'Customer Name : '+ customers[sales[key[index]][0]][0], bg = displaycolor)
        label.place(relx = 0.05, rely= 0.13, relwidth = 0.24, relheight = 0.08)
        label = tk.Label(frame, text = 'Address : ' + customers[sales[key[0]][0]][2], bg = displaycolor)
        label.place(relx = 0.7, rely= 0.13, relwidth = 0.24, relheight = 0.08)


        label = tk.Label(frame, text = 'Product Name', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label = tk.Label(frame, text = 'Unit Price', bg = displaycolor )
        label.place(relx = 0.23, rely = 0.2, relwidth = 0.3, relheight = 0.08)
        label = tk.Label(frame, text = 'Quantity', bg = displaycolor )
        label.place(relx = 0.5, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label = tk.Label(frame, text = 'Total Price', bg = displaycolor  )
        label.place(relx = 0.7, rely = 0.2, relwidth = 0.24, relheight = 0.08)

        labely = 0.3
        for j in sales[key[index]][2].keys():
            lst = sales[key[index]][2][j]
            label = tk.Label(frame, text = lst[0], bg = displaycolor )
            label.place(relx = 0.05, rely = labely, relwidth = 0.22, relheight = 0.08)
            label = tk.Label(frame, text = str(lst[1]), bg = displaycolor )
            label.place(relx = 0.23, rely = labely, relwidth = 0.3, relheight = 0.08)
            label = tk.Label(frame, text = str(lst[2]), bg = displaycolor )
            label.place(relx = 0.5, rely = labely, relwidth = 0.22, relheight = 0.08)
            label = tk.Label(frame, text = str(lst[3]), bg = displaycolor )
            label.place(relx = 0.7, rely = labely, relwidth = 0.24, relheight = 0.08)
            labely += 0.1 

    else:
        label = tk.Label(frame, text = 'No Sales Record Found', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.08)

    
    if len(key) == 1:
        button_next = tk.Button(frame, text = 'Next', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : show_next_sale(key, index, frame), state = 'disabled')
        button_next.place(relx = 0.7, rely = 0.8, relwidth = 0.3, relheight = 0.08)     
    else:
        button_next = tk.Button(frame, text = 'Next', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : show_next_sale(key, index, frame), state = 'normal')
        button_next.place(relx = 0.7, rely = 0.8, relwidth = 0.3, relheight = 0.08)     
    button_previous = tk.Button(frame, text = 'Previous', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda: show_previous_sale(key, index, frame), state = 'disabled')
    button_previous.place(relx = 0.04, rely = 0.8, relwidth = 0.3, relheight = 0.08)
    button_go_back = tk.Button(frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = sale_menu)
    button_go_back.place(relx = 0.36, rely = 0.8, relwidth = 0.3, relheight = 0.08)     


def show_next_sale(key, index, frame):

    index += 1
    if index < len(key):
        label = tk.Label(frame, text = 'Sale ID : ' + str(key[index]), bg = displaycolor)
        label.place(relx = 0.05, rely= 0.07, relwidth = 0.24, relheight = 0.08)
        label = tk.Label(frame, text = 'Customer ID : ' + str(sales[key[index]][0]), bg = displaycolor)
        label.place(relx = 0.7, rely= 0.07, relwidth = 0.24, relheight = 0.08)

        label = tk.Label(frame, text = 'CENTRAL PERK C&C', bg = displaycolor)
        label.place(relx = 0.29, rely = 0.07, relheight = 0.15, relwidth = 0.41)

        label = tk.Label(frame, text = 'Customer Name : '+ customers[sales[key[index]][0]][0], bg = displaycolor)
        label.place(relx = 0.05, rely= 0.13, relwidth = 0.24, relheight = 0.08)
        label = tk.Label(frame, text = 'Address : ' + customers[sales[key[0]][0]][2], bg = displaycolor)
        label.place(relx = 0.7, rely= 0.13, relwidth = 0.24, relheight = 0.08)


        label = tk.Label(frame, text = 'Product Name', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label = tk.Label(frame, text = 'Unit Price', bg = displaycolor )
        label.place(relx = 0.23, rely = 0.2, relwidth = 0.3, relheight = 0.08)
        label = tk.Label(frame, text = 'Quantity', bg = displaycolor )
        label.place(relx = 0.5, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label = tk.Label(frame, text = 'Total Price', bg = displaycolor  )
        label.place(relx = 0.7, rely = 0.2, relwidth = 0.24, relheight = 0.08)

        labely = 0.3
        for j in sales[key[index]][2].keys():
            lst = sales[key[index]][2][j]
            label = tk.Label(frame, text = lst[0], bg = displaycolor )
            label.place(relx = 0.05, rely = labely, relwidth = 0.22, relheight = 0.08)
            label = tk.Label(frame, text = str(lst[1]), bg = displaycolor )
            label.place(relx = 0.23, rely = labely, relwidth = 0.3, relheight = 0.08)
            label = tk.Label(frame, text = str(lst[2]), bg = displaycolor )
            label.place(relx = 0.5, rely = labely, relwidth = 0.22, relheight = 0.08)
            label = tk.Label(frame, text = str(lst[3]), bg = displaycolor )
            label.place(relx = 0.7, rely = labely, relwidth = 0.24, relheight = 0.08)
            labely += 0.1 

    if index == len(key) - 1:
        button_next = tk.Button(frame, text = 'Next', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, state = 'disabled')
        button_next.place(relx = 0.7, rely = 0.8, relwidth = 0.3, relheight = 0.08)
    button_previous = tk.Button(frame, text = 'Previous', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda: show_previous_sale(key, index, frame), state = 'normal')
    button_previous.place(relx = 0.04, rely = 0.8, relwidth = 0.3, relheight = 0.08)
    
    

def show_previous_sale(key, index, frame):

    index -= 1
    if index >= 0:
        label = tk.Label(frame, text = 'Sale ID : ' + str(key[index]), bg = displaycolor)
        label.place(relx = 0.05, rely= 0.07, relwidth = 0.24, relheight = 0.08)
        label = tk.Label(frame, text = 'Customer ID : ' + str(sales[key[index]][0]), bg = displaycolor)
        label.place(relx = 0.7, rely= 0.07, relwidth = 0.24, relheight = 0.08)

        label = tk.Label(frame, text = 'CENTRAL PERK C&C', bg = displaycolor)
        label.place(relx = 0.29, rely = 0.07, relheight = 0.15, relwidth = 0.41)

        label = tk.Label(frame, text = 'Customer Name : '+ customers[sales[key[index]][0]][0], bg = displaycolor)
        label.place(relx = 0.05, rely= 0.13, relwidth = 0.24, relheight = 0.08)
        label = tk.Label(frame, text = 'Address : ' + customers[sales[key[0]][0]][2], bg = displaycolor)
        label.place(relx = 0.7, rely= 0.13, relwidth = 0.24, relheight = 0.08)


        label = tk.Label(frame, text = 'Product Name', bg = displaycolor )
        label.place(relx = 0.05, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label = tk.Label(frame, text = 'Unit Price', bg = displaycolor )
        label.place(relx = 0.23, rely = 0.2, relwidth = 0.3, relheight = 0.08)
        label = tk.Label(frame, text = 'Quantity', bg = displaycolor )
        label.place(relx = 0.5, rely = 0.2, relwidth = 0.22, relheight = 0.08)
        label = tk.Label(frame, text = 'Total Price', bg = displaycolor  )
        label.place(relx = 0.7, rely = 0.2, relwidth = 0.24, relheight = 0.08)

        labely = 0.3
        for j in sales[key[index]][2].keys():
            lst = sales[key[index]][2][j]
            label = tk.Label(frame, text = lst[0], bg = displaycolor )
            label.place(relx = 0.05, rely = labely, relwidth = 0.22, relheight = 0.08)
            label = tk.Label(frame, text = str(lst[1]), bg = displaycolor )
            label.place(relx = 0.23, rely = labely, relwidth = 0.3, relheight = 0.08)
            label = tk.Label(frame, text = str(lst[2]), bg = displaycolor )
            label.place(relx = 0.5, rely = labely, relwidth = 0.22, relheight = 0.08)
            label = tk.Label(frame, text = str(lst[3]), bg = displaycolor )
            label.place(relx = 0.7, rely = labely, relwidth = 0.24, relheight = 0.08)
            labely += 0.1 

    if index == 0:
        button_previous = tk.Button(frame, text = 'Previous', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, state = 'disabled')
        button_previous.place(relx = 0.04, rely = 0.8, relwidth = 0.3, relheight = 0.08)

    button_next = tk.Button(frame, text = 'Next', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = lambda : show_next_sale(key, index, frame), state = 'normal')
    button_next.place(relx = 0.7, rely = 0.8, relwidth = 0.3, relheight = 0.08)
    

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------





def sale_menu():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)

    button1 = tk.Button(frame, text = 'Add Sales', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = add_sales_menu)
    button1.place(relx = 0.36, rely = 0.2, relwidth = 0.3, relheight = 0.08) 

    button2 = tk.Button(frame, text = 'View Sales', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = view_sale)
    button2.place(relx = 0.36, rely = 0.3, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Go Back', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button3.place(relx = 0.36, rely = 0.6, relwidth = 0.3, relheight = 0.08) 




#------------------------------------------------------------------------------------------------------------------------------------------------------------------



def adminframe():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0) 

    button1 = tk.Button(frame, text = 'Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = product_menu)
    button1.place(relx = 0.36, rely = 0.3, relwidth = 0.3, relheight = 0.08) 

    button2 = tk.Button(frame, text = 'Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
    button2.place(relx = 0.36, rely = 0.4, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Sales', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = sale_menu)
    button3.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Go Back', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button3.place(relx = 0.36, rely = 0.6, relwidth = 0.3, relheight = 0.08) 

    label = tk.Label(frame, text ='          CENTRAL PERK C&C           ', bg = displaycolor )
    label.place(relx = 0.36, rely = 0.1, relwidth = 0.3, relheight = 0.08)


def customerframe():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0) 

    button1 = tk.Button(frame, text = 'Products', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_product_menu)
    button1.place(relx = 0.36, rely = 0.3, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Sales', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = sale_menu)
    button3.place(relx = 0.36, rely = 0.4, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Go Back', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button3.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08) 

    label = tk.Label(frame, text ='          CENTRAL PERK C&C           ', bg = displaycolor )
    label.place(relx = 0.36, rely = 0.1, relwidth = 0.3, relheight = 0.08)


def cashierframe():
    frame = tk.Frame(root  )
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    lbl = tk.Label(frame,image = framecolor)
    lbl.place(x=0,y=0)


    button2 = tk.Button(frame, text = 'Customers', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_menu)
    button2.place(relx = 0.36, rely = 0.4, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Sales', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = sale_menu)
    button3.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(frame, text = 'Go Back', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button3.place(relx = 0.36, rely = 0.6, relwidth = 0.3, relheight = 0.08) 

    label = tk.Label(frame, text ='          CENTRAL PERK C&C           ', bg = displaycolor )
    label.place(relx = 0.36, rely = 0.1, relwidth = 0.3, relheight = 0.08)

def startframe():
    
    
    frame = tk.Frame(root)
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    lbl = tk.Label(root,image = framecolor)
    lbl.place(x=0,y=0)
    button1 = tk.Button(root, text = 'Admin', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = admin_login)
    button1.place(relx = 0.36, rely = 0.3, relwidth = 0.3, relheight = 0.08) 

    button2 = tk.Button(root, text = 'Cashier', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command= cashier_login)
    button2.place(relx = 0.36, rely = 0.4, relwidth = 0.3, relheight = 0.08) 

    button3 = tk.Button(root, text = 'Customer', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customer_login)
    button3.place(relx = 0.36, rely = 0.5, relwidth = 0.3, relheight = 0.08) 

    label = tk.Label(root, text ='          CENTRAL PERK C&C           ', bg = displaycolor )
    label.place(relx = 0.36, rely = 0.1, relwidth = 0.3, relheight = 0.08)


    
def customer_login():
    
    add_frame = tk.Frame(root  )
    add_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    lbl = tk.Label(add_frame,image = framecolor)
    lbl.place(x=0,y=0)
    label1 = tk.Label(add_frame, text = 'Enter Username : '   ,bg = buttoncolor)
    label1.place(relx = 0.15, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    label2 = tk.Label(add_frame, text = 'Enter Password: '   ,bg = buttoncolor)
    label2.place(relx = 0.15, rely = 0.2, relwidth = 0.3, relheight = 0.05)



    entry1 = tk.Entry(root, bg = buttoncolor)
    entry1.place(relx = 0.4, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    entry2 = tk.Entry(root, bg = buttoncolor)
    entry2.place(relx = 0.4, rely = 0.2, relwidth = 0.3, relheight = 0.05)
  


    button_add = tk.Button(add_frame, text = 'LOG IN', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = customerframe)
    button_add.place(relx = 0.4, rely = 0.7, relwidth = 0.3, relheight = 0.08) 
    button_add = tk.Button(add_frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button_add.place(relx = 0.4, rely = 0.8, relwidth = 0.3, relheight = 0.08)

def admin_login():
    
    add_frame = tk.Frame(root  )
    add_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    lbl = tk.Label(add_frame,image = framecolor)
    lbl.place(x=0,y=0)
    label1 = tk.Label(add_frame, text = 'Enter Username : '   )
    label1.place(relx = 0.15, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    label2 = tk.Label(add_frame, text = 'Enter Password: '   )
    label2.place(relx = 0.15, rely = 0.2, relwidth = 0.3, relheight = 0.05)



    entry1 = tk.Entry(add_frame, bg = buttoncolor)
    entry1.place(relx = 0.4, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    entry2 = tk.Entry(add_frame, bg = buttoncolor)
    entry2.place(relx = 0.4, rely = 0.2, relwidth = 0.3, relheight = 0.05)
  


    button_add = tk.Button(add_frame, text = 'LOG IN', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = adminframe)
    button_add.place(relx = 0.4, rely = 0.7, relwidth = 0.3, relheight = 0.08)
    button_add = tk.Button(add_frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button_add.place(relx = 0.4, rely = 0.8, relwidth = 0.3, relheight = 0.08)

def cashier_login():
    
    add_frame = tk.Frame(root  )
    add_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 
    lbl = tk.Label(add_frame,image = framecolor)
    lbl.place(x=0,y=0)
    label1 = tk.Label(add_frame, text = 'Enter Username : '   )
    label1.place(relx = 0.15, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    label2 = tk.Label(add_frame, text = 'Enter Password: '   )
    label2.place(relx = 0.15, rely = 0.2, relwidth = 0.3, relheight = 0.05)



    entry1 = tk.Entry(add_frame, bg = buttoncolor)
    entry1.place(relx = 0.4, rely = 0.1, relwidth = 0.3, relheight = 0.05)
    entry2 = tk.Entry(add_frame, bg = buttoncolor)
    entry2.place(relx = 0.4, rely = 0.2, relwidth = 0.3, relheight = 0.05)
  


    button_add = tk.Button(add_frame, text = 'LOG IN', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = cashierframe)
    button_add.place(relx = 0.4, rely = 0.7, relwidth = 0.3, relheight = 0.08)
    button_add = tk.Button(add_frame, text = 'GO BACK', bg = buttoncolor, fg = foregroundcolor, activebackground = activebackcolor, activeforeground = activeforcolor, command = startframe)
    button_add.place(relx = 0.4, rely = 0.8, relwidth = 0.3, relheight = 0.08)



startframe()
root.mainloop()
