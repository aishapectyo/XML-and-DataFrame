#!/usr/bin/env python

#---Import necessary libraries---#
import sys
import os
import numpy as np
import xml.etree.ElementTree as ET
from datetime import datetime as date
import csv
from xml.dom import minidom
from lxml import etree
import pandas as pd 

#---Functions---#
def load_parse_xml(data_file):
        """Check if file exists. If file exists, load and parse the data file. """
        if os.path.isfile(data_file):
                print "File exists. Parsing..."
                data_parse = ET.ElementTree(file=data_file)
                print "File parsed."
                return data_parse

def format_date(string_date):
        date_formatted = date.strptime(string_date, "%Y-%m-%d")
        return date_formatted

def create_dataframe(data):
        df = pd.DataFrame(columns=('name', 'lastname', 'email', 'domain', 'date'))
        for i in range(len(data)):
                obj = data.getchildren()[i].getchildren()
                row = dict(zip(['name', 'lastname', 'email', 'domain', 'date'], [obj[0].text, obj[1].text, obj[2].text, obj[3].text, obj[4].text]))
                row_series = pd.Series(row)
                row_series.name = i
                df = df.append(row_series)
        return df


#---Create XML file---#
#Hard coding.
top = ET.Element("top") #base of your data tree
doc = ET.SubElement(top, "doc") #next hierarchy in your root tree
name = ET.SubElement(doc, "Name")
name.text = "Juana"
lastname = ET.SubElement(doc, "LastName")
lastname.text = "Martinez"
email = ET.SubElement(doc, "Email")
email.text = "jm@hotmal.com"
dates= ET.SubElement(doc, "Date")
dates.text = "18052015"
treetop = ET.ElementTree(top)
treetop.write("basic.xml")

#Making it more efficient...
#Open file and insert date into sub-elements.
csvfilename = 'random_data.txt'
xmlfilename = open('xmldata.xml', 'w')
data = csv.reader(open(csvfilename), delimiter=' ')
header = data.next()
counter = 0
root = etree.Element('root')
for row in data:
        entry = etree.SubElement(root,'entry')
        for index in xrange(len(header)):
                child = etree.SubElement(entry, header[index])
                child.text = row[index].decode('utf-8')
                entry.append(child)
result = etree.tostring(root, pretty_print=True)
xmlfilename.write(result)

filename = "xmldata.xml"
data_xmlfile = load_parse_xml(filename)
root_tree = data_xmlfile.getroot()
dataframe = create_dataframe(root_tree)

#---Data Analysis---#
dataframe.loc[dataframe['domain'] == '@yahoo.com']
dataframe[(dataframe.domain == '@yahoo.com') &  (dataframe.name == 'Rosemary')]
dataframe[(dataframe.domain == '@yahoo.com') & (dataframe.date > '2013-01-15')]

