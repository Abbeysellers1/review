#import practiceClassKEY as p
import csv
from multiprocessing.resource_sharer import stop
from sys import set_asyncgen_hooks
import practiceClass as pc

shows = {
    "play1":{
        'id':3245,
        'name':'Phantom of the Opera',
        'capacity':65,
        'event_date':'03/01/2023'
    },
    "play2":{
        'id':1548,
        'name':'The Music Man',
        'capacity':45,
        'event_date':'05/15/2023'
    },
    "play3":{
        'id':9587,
        'name':'Hamilton',
        'capacity':124,
        'event_date':'07/21/2023'
    },
    "play4":{
        'id':6254,
        'name':'The Lion King',
        'capacity':89,
        'event_date':'09/29/2023'
    },

}

'''using the above dictionary iterate through it and create an instance of the 
play class that has id 9587
NOTE: Do not hard code the values to create the instance but use
keys and values from the dictionary '''



'''using the bookings.csv file process only those 
reservations for the same play (9587). Create an 
instance of the Booking class for each customer
that is going to play 9587 - Hamilton. 
if the play reaches capacity print out a 
error message as shown in output.JPG'''
for key in shows:
    if shows[key]["id"]==9587:
        id= shows[key]["id"]
        name= shows[key]['name']
        seats= shows[key]['capacity']
        date=shows[key]['date']
        instance= pc.Play(id, name, seats, date)
        print('yes')


#open the csv file in read mode
infile= open('bookings.csv','r')
csvfile=csv.reader(infile, delimiter=',')
next(infile)


#create a csv object from the file object from the step above


#124 cap
# use a for loop to iterate through each record in the bookings file
open_seats = instance.get_number()



for records in infile:
    if float(records[0]) == 9587:
        open_seats-=1
        if open_seats>0:
            print('Welcome')
        else:
            print('***********ERROR***********')
            print('Guest Name: ', records[1])
            print('Sorry, show: ', shows[2][1],'is sold out')
            print('****************************')
        
