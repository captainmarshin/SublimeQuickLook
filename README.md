# Sublime Quick Look
Plugin for Sublime Text to show macOS Quick Look for selected file. 

This is edited version of [original plugin](https://github.com/wallysalami/QuickLook). 
<br/>
This plugin version uses `Apple Script` instead of `qlmanage` to show Quick Look. Apple Script was written by **ok-kompjutor** ([founded here](https://www.reddit.com/r/osx/comments/bkwnr3/comment/lzuy3hg/)) and updated to use in this plugin. 

## How it work
Plugin run Apple Script, which opens Finder with selected file and show Quick Look preview instead of launching `qlmanage` app to show Quick Look preview.

## Changelog 
- [x] Replace `qlmanage` with Apple Script
- [x] Change plugin shortcut (⌘ + Shift + /)
- [x] Update project structure and docs

## Installation
1. Download zip archive with plugin from [Releases](https://github.com/captainmarshin/SublimeQuickLook/releases) page
2. Extract QuickLook folder to ~/Library/Application Support/Sublime Text/Packages/

## Usage
Quick Look command appears in context menu (right-click on file in Folder View or in Editor).
<br/>
Alternatively, Use `⌘ + Shift + /` key shortcut to run plugin.
