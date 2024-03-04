---
title: Get Hex code as text from ColorValue in your Canvas App
layout: post
post-image: "/assets/images/Maybe_it_s_over_to_the_left___.jpg"
description: If you need to get your color variable as text(for svg or html controls), this is the way
tags:
- Power Platform
- Canvas app
- Coding
---

#The Issue
When using svg images or html controls in an canvas app, it is common to need to be able to change color of different elements. Sadly, these controls don't recognize the data type: color.

# The Solution
To be able to get the raw hex value from these, you can convert the variable via the JSON() command.

Formula:
`
GreenColor = ColorValue("#1BCC17");
`

`
JSON(GreenColor)
`
This generate the hexcode as "#1BCC17".

But if you need the Hex value without citations (for use in svg images), append the Substitute() command.

`Substitute(JSON(gblAppColors.Green),"""","")`
Which will generate the text: #1BCC17

