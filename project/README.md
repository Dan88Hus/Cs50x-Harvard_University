#################################################################################################################################
#   Assumptions:                                                                                                                #
#   There is an warehouse which can ship items to another location so we each user will save records in database and we will    #
#   SELECT from that records to dynamical website                                                                               #
#    1 company worker who logged can see all item list in warehouse                                                             #
#    item record page will return record page again to enter new item                                                           #
#    Company purchase item from supplier and send it to customers, sales dont return purchased item, no return back             #
#    SELECTION from item table will be >= it_qnty so we can transfer what we have on warehouse item list                        #
#    no delete or hide recorded data                                                                                            #
#################################################################################################################################

#Created 4 table in warehouse.db which are "location, users, item, transfer"

##all tables are connected together
item table(PK) are FK of TRANSFER TABLE ,
LOCATION table(PK) ID is FK of TRANSFER table,
USER table ID (PK) is FK of ITEM table
ITEM table id(PK) is FK of Transfer table
Reports of each table, recordings updated and transferred items

programmed website is record, update,no delete because companies dont want to delete datas, maybe archive can be to hide data
but in this scenerio I will not hide data, and report the recorded datas

