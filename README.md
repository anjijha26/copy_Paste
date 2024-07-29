Copy-Paste Tool

This tool, built using PyQt5 and Python, allows users to copy files with ease. It features a user-friendly interface where the user can select a source file and a destination path, ensuring a smooth and efficient file transfer process.

Features:
1.	Source File Selection:

o	Users can select a source file they wish to copy.
o	The selected source file path is displayed in a LineEdit, allowing users to see and modify the path if needed.

2.	Path Verification:

o	The tool verifies the correctness of the source file path.
o	If the path is incorrect or the file does not exist, the LineEdit turns red.
o	If the path is correct and the file exists, the LineEdit turns green.

3.	Destination Path Selection:

o	Users can select the destination path where they want to copy the file.

4.	Copy Button Activation:

o	The copy button is initially disabled.
o	Once both the source file and the destination path are selected, the copy button is enabled.

5.	File Copying with Progress Bar:

o	Upon clicking the copy button, the file copying process begins.
o	A progress bar updates to reflect the percentage of the file that has been copied.
o	The progress bar shows 100% once the copying is complete.

6.	Multithreading for Smooth Operation:

o	The tool uses multithreading to handle the file copying process and the progress bar update simultaneously.
o	This ensures that both processes run smoothly without interfering with each other.

