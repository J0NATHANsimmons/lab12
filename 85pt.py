#########################################
#
#         85pt - Add a cancel button
#
#########################################


# Add a cancel button with a red background
# When the cancel button is pressed, change the color from red to blue
# and then back to red when pressed again
# Read the comment above line 24 v
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent  ### (7) remember my parent, the root
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="cancel", background= "red")
		self.button1.grid(row=0, column=0)	
		# Do not change <Button-1> when you create Button 2 :)
		self.button1.bind("<Button-1>", self.button1Click) ### (1)
		
		
	def button1Click(self, event):    ### (3)
		if self.button1["background"] == "blue": ### (4)
			self.button1["background"] = "red"
		else:
			self.button1["background"] = "blue"
	def __init__(self, parent):
		self.myParent = parent  ### (7) remember my parent, the root
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="cancel", background= "red")
		self.button1.grid(row=0, column=0)	
		# Do not change <Button-1> when you create Button 2 :)
		self.button1.bind("<Button-1>", self.button1Click) ### (1)
		
		
	def button1Click(self, event):    ### (3)
		if self.button1["background"] == "blue": ### (4)
			self.button1["background"] = "red"
		else:
			self.button1["background"] = "blue"
			### (4)
	def button3Click(self, event):
	    if self.button1["background"] == "blue":
	        self.button1["background"] = "red"
	    else:
	            self.button1["background"] = "blue"
	            
		
root = Tk()
myapp = MyApp(root)
root.mainloop()