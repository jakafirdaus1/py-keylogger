# KeyLogger with Python (Educational Purposes)

<h2>Description</h2>
This projects consists of a simple Python script that lead you to experience a basic threat in cybersecurity. A Python keylogger is a program written in Python designed to monitor and record keystrokes made by a user on a keyboard. It is often used for tracking user activity or debugging purposes but can also be misused for malicious activities such as stealing sensitive information like passwords and personal data.<br/><br/>

<b>This is intended strictly for educational or ethical purposes. Do not use it for illegal or malicious activities.</b>



<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Visual Studio Code</b>

<h2>Environments Used </h2>

- <b>Virtual Environment</b>

<h2>Project walk-through:</h2>

Create a folder named project and open the folder from visual studio code. Inside the folder create a file named keylogger.py. I recommend to run this program in a virtual environment so you dont have to allow keylogger threat from the virus & threat protection in your personal computer.</br></br>

<p align="center">
Create a virtual environment:   </br>
<img src="https://i.imgur.com/VQ95EGe.png" height="80%" width="80%" alt="Creating Virtual Environment"/>
<br/>
<br/>
Activate the virtual environment:  <br/>
<img src="https://i.imgur.com/oPhu7IE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
<p align="center">
Installing pynput: <br/>
<img src="https://i.imgur.com/HMfyI7W.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Importing pynput library:  <br/>
<img src="https://i.imgur.com/YBXnimH.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Define keyPressed function:  <br/>
<img src="https://i.imgur.com/B2mRsli.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
 </p>
 
- <b>key.char: This is the character representation of the key if it's a alphabetic or numerical key (like a,b,1,2, etc.)</b></br>
- <b>AttributeError: Some keys (like Shift, CTRL, Delete, etc.) don't have .char attribute. We handle this as "Special Keys" by writing them in a special format (e.g., [Key.space] for the Spacebar.</b>
<br />
<p align="center">
Start the Listener:  <br/>
<img src="https://i.imgur.com/yUA9KTf.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
 </p>
 
- <b>keyboard.Listner(on_pressed=keyPressed): Set the listener to call keyPressed function whenever a key is pressed</b>
- <b>input(): This keeps the program running and waits for the user to press Enter to stop the keylogger.</b>
<br />
<p align="center">
Running the Keylogger:  <br/>
<img src="https://i.imgur.com/ndU43wt.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>
Now that the keylogger script is ready, you can run it. Whenever keys pressed, they will be logged in the keyfile.txt file. if special keys like Shift, Enter or Delete pressed, they will be written in a readable format (e.g., [Key.space]).

<h2>Conclusion</h2>
In this project, we created a simple keylogger that logs all the keys pressed by the user into a text file using the pynput library. Keep in mind, keylogging can be used for good purposes (e.g., creating custom shorcuts, accessibility tools) but should always be used ethically and with permission.
<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
