#!/bin/sh

PLIST=${HOME}/Library/Preferences/com.apple.Terminal.plist
BUDDY=/usr/libexec/PlistBuddy

$BUDDY -c "Delete 'Window Settings:Pro:CharacterEncoding'" $PLIST 2>/dev/null
$BUDDY -c "Add 'Window Settings:Pro:CharacterEncoding' integer 2147484672" $PLIST 2>/dev/null
$BUDDY -c "Set 'Default Window Settings' Pro" $PLIST 2>/dev/null
