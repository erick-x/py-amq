#!/usr/bin/python
#coding:utf-8

from logManager import *
from lxml import etree
import re


def operationXML(xml_file,lastModparentNode,lastModChildNode=[]):

        parentNode = ""
        allChildNodes = []
        doc = etree.ElementTree(file = xml_file)
        root = doc.getroot()

        ns = getNameSpace(doc)

        if ns != None:
            parentNode = root.findall(ns+lastModparentNode,namespaces = None)
        else:
            parentNode = root.findall(lastModparentNode,namespaces = None)

        if parentNode == None or len(parentNode) == 0:
            Debug ("%s is emtpy"%(xml_file))
        else:
            for node_contents in parentNode:
                childNode=[]
                if len(lastModChildNode)!=0:
                    for childeNode in lastModChildNode:
                        node_text =""
                        if ns== None:
                            node_text = node_contents.find(childeNode)
                        else:
                            node_text = node_contents.find(ns+childeNode)
                        childNode.append(node_text.text)
                else:
                    for childAll in list(node_contents):
                        childNode.append(childAll.text)
                allChildNodes.append(childNode)
            return allChildNodes

def getNameSpace(doc):
    ns = None
    root = doc.getroot()
    r = re.compile('({.+})')
    if r.search(root.tag)!=None:
        ns = r.search(root.tag).group(1)

    return ns
