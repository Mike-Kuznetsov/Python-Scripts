#!/bin/bash
# Script for auto installing Exodus into Tails with your account.
# English (This video is not mine): https://www.youtube.com/watch?v=1aQ7s4FIeB4
# Russian (My video): https://www.youtube.com/c/MautozTech/videos

dpkg -i /home/amnesia/Persistent/Exodus/exodus.deb
cp -f -r /home/amnesia/Persistent/Exodus /home/amnesia/.config
chown -R amnesia:amnesia /home/amnesia/.config/Exodus