# Skltl library

## A bare-bones web framework.

What do you get when a web developer who likes doing everything from scratch collects every line of code that shows up in every single project he writes?  
This. This is what you get.

## Why

Trying to define the principles of what Skltl is would take more time than reimplementing all this code (for the 50th time), so I'll keep the goals brief.

- Modular design: Each file has one job. Sometimes the files with complicated jobs are shockingly short (such as toggle-hide buttons that I use to make menus), and sometimes simple jobs are shockingly verbose (such as color theme palettes).
- Minimal starting knowledge: This thing uses as few custom classes and IDs as possible. You can just plunk this CSS on any clean semantic HTML and it should look just fine.
- Hackable: If it isn't obvious where to find the variable to tweak this property or that, I haven't done my job right.
- Skinnable: Variables are awesome. It's super easy to redo the theme for a website only a few tweaks.
- Extensible: Any code I decide I'll reuse a lot is easy to just slot in. `@import` just might be the most useful CSS feature ever, unless someone patches in color mixing soon. ~~*cough cough `background="rgb(var(--back),50%);` cough*~~

## Features

- Script to compile modular CSS with extensive imports into a single file.
- Built-in auto dark/light theme preference matching.
- Noscript-friendly toggle-hide buttons for menus.
- Responsive: Wide screens get two sidebars, narrow screens get vertical layout.
- Content that you'd expect to be blocks are actually blocks now.
- It's easy to make certain block content into inline.
- Inline pics and SVG are sized and positioned to fit in like custom emojis.
- Navigation menus are intuitive to make now.