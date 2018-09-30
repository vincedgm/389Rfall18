Writeup 3 - Pentesting I
======

Name: Vince De Guzman
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Vince De Guzman

## Assignment 4 Writeup

### Part 1 (45 pts)
Using the command given I saw that I was able to enter an IP Address and that it was vulnerable to a command injection attack. The very first input I did was to enter the IP Address (142.93.117.193) followed by shell; to see if it was working correctly. After making sure that it worked, I used the same input but afterwards I put ls to look at the different directories. From there I cd into the home directory and checked to see what files were in there. After finding the flag.txt file my final input was 142.93.117.193 shell; cat home/flag.txt; and the flag I found was CMSC389R-{p1ng_as_a_$erv1c3}. Some precautions that Fred could implement would to utilize an actual web-based OSINT solution instead of utilization a Linux ping command. Fred could also utilize existing API for the website.

### Part 2 (55 pts)
My implementation was to have a while loop that takes in the different commands. Inputing shell starts a while loop that will repeatedly execute commands and utilize command injection attack. I take in the current directory and the command written on the command line and use execute_cmd to send attack to the IP address. To implement the pull command I used execute_cmd to cd to the remote-path given and from there I used mv to copy it to the local path given. Help and Quit are self explanatory where I just break the loop and help prints the help menu.
