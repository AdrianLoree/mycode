#!/usr/bin/python3
'''pandas change json to csv'''

#import standard library
import pandas

#main function
def main():
    '''loads at run time used to change json to csv'''

    #create dataframe from json file
    df = pandas.read_json("5movies.json")
    
    #write out dataframe to CSV
    df.to_csv("5movies-translated-from-json.csv")

#best practice way to end main function
if __name__ == "__main__":
    main()

