---
title: How to name your PowerApps canvas app objects
layout: post
post-image: "/assets/images/SamplePost.png"
description: Get to grips with how to best name your canvas app objects
tags:
- Power Platform
- Canvas app
- Model-driven app
- Solutions
---

# Object naming conventions
As you create objects in your PowerApps apps, it’s important to use consistent naming conventions for
screens, controls, and data sources. This approach will make your apps easier to maintain, can help
improve accessibility, and will make your code easier to read as those objects are referenced.


## General naming conventions
This section describes “camel case” and “Pascal case” naming conventions. If you’re already familiar
with those terms, you can skip ahead.

### Camel case
Use camel case for controls and variables. Camel case begins with a lowercase,
removes all spaces and capitalizes the first letter of each word after the
first word. For example, a label might be named lblHeader.

### Pascal case
Use Pascal case for data sources. Like camel case, it removes spaces and capitalizes the first letter of each words. However Pascal case also capitalizes the first word. 
For example, a common data source in PowerApps is the Microsoft Office 365 Users connector, which is named Office365Users in your code.


## Screen names
Screen names should reflect the purpose of the screen, so that it’s easier to navigate through complex
apps in PowerApps Studio.

## Control names
All control names on the canvas should use camel case. They should begin with a three-character type
descriptor, followed by the purpose of the control.

- If a control is reused on multiple screens, the short screen name should be suffixed at the end – for example, galBottomNavMenuHS, where “HS” stands for “Home Screen.”

Control name	Abbreviation
button	btn
component	cmp
screen	scr
camera control	cam
canvas	can
card	crd
combo box	cmb
dates	dte
drop down	drp
form	frm
gallery	gal
group	grp
header page shape	hdr
html text	htm
icon	ico
image	img
label	lbl
page section shape	sec
shapes(rect, circle)	shp
table data	tbl
text input	txt
timer	tim
checkbox	cbx
named formula	nfo
container	cnt
hor container	
vert container


## Data source names
When you add a data source to your application, the name can’t be changed in the PowerApps app. The
name is inherited from the source connector or data entities that are derived from the connection.
Here are some examples:
- Name inherited from the source connector: The Office 365 Users connector is named Office365Users in your code.
- Data entities derived from the connection: A Microsoft SharePoint list that’s named Employees is returned from the SharePoint connector. Therefore, the name of the data source in your code is Employees.

## Code naming conventions
As you add code to your PowerApps apps, it becomes increasingly important to use consistent naming
conventions for variables and collections. If variables are named correctly, you should be able to quickly
discern the type, purpose, and scope of each.


## Variable names

- Be descriptive of the variable’s function. Think about what the variable is bound to and how it’s
used, and then name it accordingly.
- Prefix your global and context variables differently
- Prefix context variables with **loc**.
- Prefix global variables with **gbl**.

## Collection names
- Be descriptive of the collection’s contents. Think about what the collection contains and/or how
it’s used, and then name it accordingly.
- Collections should be prefixed with **col**.
- The name after the prefix should indicate the intent or purpose of the collection. Multiple words
can be used and don’t have to be separated by spaces or underscores, provided that the first
letter of each word is capitalized.
- Use **Camel casing**. Begin your collection names with a lowercase col prefix, and then capitalize
the first letter of each word in the name (that is, colUpperUpper).
Here are some good examples:
- colMenuItems
- colThriveApps
Here are some bad examples:
- orderscoll
- tempCollection





## Resources
https://pahandsonlab.blob.core.windows.net/documents/PowerApps%20canvas%20app%20coding%20standards%20and%20guidelines.pdf