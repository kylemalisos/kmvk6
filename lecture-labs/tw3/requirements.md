# Kyle Malisos - CS4830 Fall '19 - Tuesday Week 3 Lab

## Requirements for newspaper photographic manager application
( first person - making the original document )

**Stakeholders** - photographers, editors, journalists and journalism companies (CNN, NBC, FOX, etc)
**Users** - photographers, editors, journalists, system admins

## System Requirements

	- The system will need a database management system to store information including keywords, date, filepath
	- Interface (Web based and/or mobile application)
	- Storage space to centrally store image files
	- Organize images based on keywords in filesystem
	- Aspect ratio limitations on uploaded image
    - Aspect ratio is attached to keywords of images to allow for sorting
    - Removed images will be stored in a temporary trash folder for 6 months before they are fully deleted



## Functional Requirements
    - System Admin
        - Have the ability to add and remove images
        - Can change permissions for editors, photographers etc.
        - Can change the organization of the database folders and storage.
	- Editors and Journalists
		- Editors can submit placeholder image in news articles
		- Editors can replace placeholder images with other images
		- Editors should be able to add and check copyright information on images
		- Editors can search for images based on keyword and/or date
		- Journalists will be notified if they try to publish an article containing placeholder images
	- Photographers
		- Photographers can upload images to a central repository from a web or mobile application
		- Photographers can add keywords and date of the image when uploading
		- Photographers can specify which placeholder image their uplaod will replace
        - Photographers can only add images and cannot remove them
	- System
		- The system will remove outdated images based on keywords
        - System will prompt user before removal of previous keywords
		- The system will reject images with a non-standard aspect ratio
		