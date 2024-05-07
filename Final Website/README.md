# Final Project: Ryanaustinaudio.com (currently still ryanaustin7.github.io)

## Why? (motivation, philosophy, inspirations)
#### I want a website to show others my work. I want to be a composer, sound designer, and audio implementer for games, and networking is a big part of that. It's also a lot cheaper to make your own website and buy a domain rather than paying for one through wix, even with the Berklee discount that's also offered to literally everyone all the time. You could say my inspiration for this was Rachel, after seeing her website and realizing I could do that too.

## How? (System Diagram, Physical Form, Hardware Configuration, Software Description)
#### I took the source code from our class website project we did (“The Brassicas” website that we did with Tim and Maya) and had that as a start. It already had everything I needed for inserting a picture and had a body paragraph so that was a good start. I knew I wanted multiple tabs, so I scoured the internet to figure out how to add a navbar. On w3schools.com there are examples of how to make a navbar, and how to make it responsive, etc. I made the background color of the navbar transparent to blend in with the background of my page. I also added a dropdown menu to the “My Stuff” section of the navbar. I also learned how to reference other .html pages from the website so that the tabs could actually take me somewhere. I also from that page learned about the "@media screen and (max-width: 600px)" to make it so when the screen shrinks it would resize for mobile! I applied a lot of other things to this media screen code to make everything on each page resize if you're on mobile.
#### I also learned that I can make separate .css files and just call them in my .html file, rather than having a bunch of stuff occupy the .html file! This became especially useful when I started adding other tabs, because if there was something universally applied to all pages and I made tweaks to one of them, I would've had to make changes to all of them. So that was a big discovery. I made a universal css file called nav, because most of the stuff in it was for the navigation bar, although it also had other universal styling stuff. I also made css files that would be specific for each page. So each page calls 2 style sheets.
#### A google search told me that a <meta> tag would be used to control dimensions and scaling of my pages, and i didn't know how to go about that. All of my searches led me nowhere, so I went to AI for this one. It gave me <meta name="viewport" content="width=device-width, initial-scale=1.0">, which seems simple enough, and taught me the word viewport. It was also in my google searches for this that I learned that I don't need to use px for font sizing, I could also use vw, which makes it responsive to size on the screen. There were other various things I learned along my searches, like adding an alternative text to my image for accessibility, adding a video player for youtube videos (I tried using a video directly in my repository and it was way too large so I tried downloading GitHub Large Files or whatever it's called and it was too complicated so I uploaded the video to YouTube and just added it from there), adding links to socials, etc. W3schools.com was clutch.
#### I did run into a lot of trouble with my page that would have 2 video players, so I added images on top of them and added opacity to remove the images when the mouse is hovering over them. The thumbnails before weren't sizing properly and it looked pretty bad. This way there's a consistent thumbnail.
#### I learned about z-indexing and how that controls the order of how things are stacked, so I'd make my background container a z-index of -1 so it's behind everything, and I made it fixed as well so you can't scroll past the bottom of the container and see white at the bottom, or a repeat of the color scheme. Speaking of color scheme, I spent a long time finding gradients I liked and put them in the linear-gradient code. There were a few moments where ai came into play, like helping me with the video container code and making small grammatical adjustments, positioning and spacing some things, teaching me what padding and margin were, ya. So that definitely came in handy for making small adjustments like that.
#### And that's really it! It now functions like a website (without a domain)

## Demo
[Ryan's Website](https://ryanaustin7.github.io/)

## What Works? (Hardware, Software, Playability, Construction)
#### Using it on my desktop or on mobile both work great. All the videos run great, the links work in my socials tab, the colors are nice, everything is functional!

## What Doesn't Work Yet?
#### There isn't anything that flat out doesn't work now, but I also don't have a domain yet so I guess that's what doesn't work lol. BUT it's online at ryanaustin7.github.io!

## Additional Features I Want in the Future
#### I want to add a Demo Reel of music and implementation stuff and have that be on the front page, and move the pic of me and short bio to an about me tab instead!
#### I want better Wwise content
#### I want to make more YouTube content so that my link to YouTube actually means something
#### I want to have music players of stuff i've written in the music tab and move the videos of me playing guitar into a separate guitar tab or something.  
#### I want to clean some things up, like fonts and capitalization of certain letters and adding more videos and wording, etc.

# References that I could find retrospectively (sorry)
#### https://www.w3schools.com/html/ for many parts (navbar, referencing other files, audio player, resizing, vw vs px for adaptive fonts)
#### 
