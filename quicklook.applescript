#!/usr/bin/osascript

on run {filePath}
  set currentDir to do shell script "pwd"
  if filePath does not start with "/" then
    set filePath to currentDir & "/" & filePath
  end if
  
  tell application "Finder"
    set theFile to POSIX file filePath as alias
    reveal theFile
    activate
    delay 0.1
    select theFile
    tell application "System Events" to keystroke "y" using command down
  end tell
end run