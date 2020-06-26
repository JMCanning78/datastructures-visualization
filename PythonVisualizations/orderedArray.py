import random
from tkinter import *
try:
    from drawable import *
    from VisualizationApp import *
except ModuleNotFoundError:
    from .drawable import *
    from .VisualizationApp import *

CELL_SIZE = 50
CELL_BORDER = 2
CELL_BORDER_COLOR = 'black'
ARRAY_X0 = 100
ARRAY_Y0 = 100
FONT_SIZE = 20
VALUE_FONT = ('Helvetica', FONT_SIZE)
VALUE_COLOR = 'black'
FOUND_COLOR = 'brown4'

class OrderedArray(VisualizationApp):
    nextColor = 0

    def __init__(self, size=10, title="OrderedArray", **kwargs):
        super().__init__(title=title, **kwargs)
        self.size = size
        self.title = title
        self.list = []
        self.buttons = self.makeButtons()
        
        # Fill in initial array values with random integers
        # The display items representing these array cells are created later
        a = [random.randrange(90) for i in range(size-1)]
        a.sort()
        
        # Append and draw them to the list and draw them
        for i in a:
            self.list.append(drawable(i))

        self.display()        

    def __str__(self):
        return str(self.list)

    # ARRAY FUNCTIONALITY

    def createIndex(         # Create an index arrow to point at an indexed
            self, index,     # cell
            name=None,       # with an optional name label
            level=1,         # at a particular level away from the cells
            color=VARIABLE_COLOR): # (negative are below)
        cell_coords = self.cellCoords(index)
        cell_center = self.cellCenter(index)
        level_spacing = VARIABLE_FONT[1] 
        x = cell_center[0]
        if level > 0:
            y0 = cell_coords[1] - CELL_SIZE * 3 // 5 - level * level_spacing
            y1 = cell_coords[1] - CELL_SIZE * 3 // 10
        else:
            y0 = cell_coords[3] + CELL_SIZE * 3 // 5 - level * level_spacing
            y1 = cell_coords[3] + CELL_SIZE * 3 // 10
        arrow = self.canvas.create_line(
            x, y0, x, y1, arrow="last", fill=color)
        if name:
            label = self.canvas.create_text(
                x + 2, y0, text=name, anchor=SW if level > 0 else NW,
                font=VARIABLE_FONT, fill=color)
        return (arrow, label) if name else (arrow, )

    insertCode = """
def insert(self, item):
   self.__a[self.__nItems] = item
   self.__nItems += 1
"""
    insertCodeSnippets = {
        'item_assignment': ('2.3', '2.end'),
        'nitem_increment': ('3.3', '3.end'),
    }
    
    def insert(self, val):
<<<<<<< Updated upstream
        callEnviron = self.createCallEnvironment()
        self.startAnimations()
        j = self.find(val)  # Find where item should go

        self.list.append(drawable(None))
        
        indexK = self.createIndex(len(self.list), 'k', level=-1) # create "k" arrow
        callEnviron |= set(indexK)  
        
        for k in range(len(self.list) - 1, j, -1):  # Move bigger items right
            
            self.wait(1)
            for item in indexK:
                self.canvas.move(item, -CELL_SIZE, 0)  # Move "k" arrow  
                
            self.list[k].val = self.list[k - 1].val 
            self.assignElement(k - 1, k, callEnviron)    
                    
=======
        self.cleanUp()
        j = self.find(val)  # Find where item should go

        self.list.append(drawable(None))

        for k in range(len(self.list) - 1, j, -1):  # Move bigger items right
            self.wait(1)
            self.list[k].val = self.list[k - 1].val
            self.assignElement(k - 1, k)

>>>>>>> Stashed changes
        # Location of the new cell in the array
        toPositions = (self.cellCoords(j),
                       self.cellCenter(j))

        # Animate arrival of new value from operations panel area
        canvasDimensions = self.widgetDimensions(self.canvas)
        startPosition = [canvasDimensions[0] // 2, canvasDimensions[1]] * 2
        startPosition = add_vector(startPosition, (0, 0, CELL_SIZE, CELL_SIZE))
        cellPair = self.createCellValue(startPosition, val)
        self.moveItemsTo(cellPair, toPositions, steps=CELL_SIZE, sleepTime=0.01)
        self.list[j]= (drawable(
            val, self.canvas.itemconfigure(cellPair[0], 'fill'), *cellPair))

<<<<<<< Updated upstream
        self.window.update()  
        self.cleanUp(callEnviron)
        
    def remove(self, val):
        callEnviron = self.createCallEnvironment()
        self.startAnimations()
        index = self.find(val)
        found = index != None    # Record if value was found
        if found:
            self.wait(0.3)
=======
        self.window.update()       
        
    def remove(self,val):
        self.startAnimations()
        index = self.find(val)
        if index != None:
            self.wait(1)
            self.cleanUp()
>>>>>>> Stashed changes

            n = self.list[index]

            # Slide value rectangle up and off screen
            items = (n.display_shape, n.display_val)
            self.moveItemsOffCanvas(items, N, sleepTime=0.02)

            # Create an index for shifting the cells
            kIndex = self.createIndex(index, 'k')
            callEnviron |= set(kIndex)
            
            # Slide values from right to left to fill gap
            for i in range(index+1, len(self.list)):
                self.assignElement(i, i-1, callEnviron)
                self.moveItemsBy(kIndex, (CELL_SIZE, 0), sleepTime=0.01)

            self.removeFromEnd()
<<<<<<< Updated upstream
        
        self.cleanUp(callEnviron)
        return found
=======
            self.stopAnimations()
            return True
        self.stopAnimations()
        return False 
>>>>>>> Stashed changes
    
    def randomFill(self):
        # Clear the list so new values can be entered
        self.list=[] 
        size = self.size
        
        # Create a list of random numbers and sort them
        a = [random.randrange(90) for i in range(size)]
        a.sort()
        
        # Append and draw them to the list and draw them
        for i in a:
            self.list.append(drawable(i))
        
        self.display()         
        
    def newArraySize(self, val):
        # Clear Array and reset size and list
        self.canvas.delete("all")
        self.size = val
        self.list = []        
        
        for i in range(val):  # Draw new grid of cells
            self.createArrayCell(i)        
        
        self.window.update()

    def removeFromEnd(self):
        callEnviron = self.createCallEnvironment()
        self.startAnimations()
        # pop a Drawable from the list
        if len(self.list) == 0:
            self.setMessage('Array is empty!')
            return
        n = self.list.pop()

        # delete the associated display objects
        self.canvas.delete(n.display_shape)
        self.canvas.delete(n.display_val)
        
<<<<<<< Updated upstream
=======
        print(len(self.list))
>>>>>>> Stashed changes
        # update window
        self.window.update()
        self.cleanUp(callEnviron)


    def assignElement(
            self, fromIndex, toIndex, callEnviron,
            steps=CELL_SIZE // 2, sleepTime=0.01):
        fromDrawable = self.list[fromIndex]

        # get positions of "to" cell in array
        toPositions = (self.cellCoords(toIndex), self.cellCenter(toIndex))

        # create new display objects as copies of the "from" cell and value
        newCell = self.copyCanvasItem(fromDrawable.display_shape)
        newCellVal = self.copyCanvasItem(fromDrawable.display_val)
        callEnviron |= set([newCell, newCellVal])

        # Move copies to the desired location
        self.moveItemsTo((newCell, newCellVal), toPositions, steps=steps,
                         sleepTime=sleepTime)

        # delete the original "to" display value and the new display shape
        self.canvas.delete(self.list[toIndex].display_val)
        self.canvas.delete(self.list[toIndex].display_shape)      

        # update value and display value in "to" position in the list
        self.list[toIndex].display_val = newCellVal
        self.list[toIndex].val = self.list[fromIndex].val
        self.list[toIndex].display_shape = newCell
        self.list[toIndex].color = self.list[fromIndex].color
<<<<<<< Updated upstream
        callEnviron ^= set([newCell, newCellVal])
        
        # delete the original "from" display value and the new display shape
        self.canvas.delete(self.list[fromIndex].display_val)
        self.canvas.delete(self.list[fromIndex].display_shape)           
        
=======
        
        # delete the original "from" display value and the new display shape
        self.canvas.delete(self.list[fromIndex].display_val)
        self.canvas.delete(self.list[fromIndex].display_shape)        

>>>>>>> Stashed changes
        # update the window
        self.window.update()

    def cellCoords(self, cell_index): # Get bounding rectangle for array cell
        return (ARRAY_X0 + CELL_SIZE * cell_index, ARRAY_Y0, # at index
                ARRAY_X0 + CELL_SIZE * (cell_index + 1) - CELL_BORDER,
                ARRAY_Y0 + CELL_SIZE - CELL_BORDER)

    def cellCenter(self, index): # Center point for array cell at index
        half_cell = (CELL_SIZE - CELL_BORDER) // 2
        return add_vector(self.cellCoords(index), (half_cell, half_cell))

    def createArrayCell(self, index): # Create a box representing an array cell
        cell_coords = self.cellCoords(index)
        half_border = CELL_BORDER // 2
        rect = self.canvas.create_rectangle(
            *add_vector(cell_coords, 
                        (-half_border, -half_border,
                         CELL_BORDER - half_border, CELL_BORDER - half_border)),
            fill=None, outline=CELL_BORDER_COLOR, width=CELL_BORDER)
        self.canvas.lower(rect)
        return rect

    def createCellValue(self, indexOrCoords, key, color=None):
        """Create new canvas items to represent a cell value.  A square
        is created filled with a particular color with an text key centered
        inside.  The position of the cell can either be an integer index in
        the Array or the bounding box coordinates of the square.  If color
        is not supplied, the next color in the palette is used.
        An event handler is set up to update the VisualizationApp argument
        with the cell's value if clicked with any button.
        Returns the tuple, (square, text), of canvas items
        """
        # Determine position and color of cell
        if isinstance(indexOrCoords, int):
            rectPos = self.cellCoords(indexOrCoords)
            valPos = self.cellCenter(indexOrCoords)
        else:
            rectPos = indexOrCoords
            valPos = divide_vector(add_vector(rectPos[:2], rectPos[2:]), 2)
        if color is None:
            # Take the next color from the palette
            color = drawable.palette[OrderedArray.nextColor]
            OrderedArray.nextColor = (OrderedArray.nextColor + 1) % len(drawable.palette)

        cell_rect = self.canvas.create_rectangle(
            *rectPos, fill=color, outline='', width=0)
        cell_val = self.canvas.create_text(
            *valPos, text=str(key), font=VALUE_FONT, fill=VALUE_COLOR)
        handler = lambda e: self.setArgument(str(key))
        for item in (cell_rect, cell_val):
            self.canvas.tag_bind(item, '<Button>', handler)

        return cell_rect, cell_val

    def display(self):
        self.canvas.delete("all")

        for i in range(self.size):  # Draw grid of cells
            self.createArrayCell(i)

        # go through each Drawable in the list
        for i, n in enumerate(self.list):
            # create display objects for the associated Drawables
            n.display_shape, n.display_val = self.createCellValue(
                i, n.val, n.color)
            n.color = self.canvas.itemconfigure(n.display_shape, 'fill')

        self.window.update()

    def find(self, val): 
<<<<<<< Updated upstream
        callEnviron = self.createCallEnvironment()
        self.startAnimations()
        lo = 0                             #Point to lo
        indexLo = self.createIndex(lo, 'lo',level= 1)
        callEnviron |= set(indexLo)
        hi = len(self.list)-1              # Point to hi
        indexHi = self.createIndex(hi, 'hi', level = 3)
        callEnviron |= set(indexHi)
        mid = (lo + hi) // 2               # Point to the midpoint
        indexMid = self.createIndex(mid, 'mid', level = 2)
        callEnviron |= set(indexMid)            
=======
        self.startAnimations()
        self.cleanUp()
        lo = 0                             #Point to lo
        indexLo = self.createIndex(lo, 'lo',level= 1)
        self.cleanup |= set(indexLo)
        hi = len(self.list)-1              # Point to hi
        indexHi = self.createIndex(hi, 'hi', level = 3)
        self.cleanup |= set(indexHi)
        mid = (lo + hi) // 2               # Point to the midpoint
        indexMid = self.createIndex(mid, 'mid', level = 2)
        self.cleanup |= set(indexMid)            
>>>>>>> Stashed changes
        while lo <= hi:
            mid = (lo + hi) // 2           # Select the midpoint
            if self.list[mid].val == val:  # Did we find it at midpoint?  
                self.stopAnimations()
                self.window.update()
                return mid                 # Return the value found 
        
            elif self.list[mid].val < val: # Is item in upper half?
                deltaXLo = (mid - lo) + 1
                self.moveItemsBy(indexLo, (CELL_SIZE*deltaXLo, 0))
                lo = mid + 1               # Yes, raise the lo boundary
                deltaXMid = ((hi - lo) // 2) + 1
                self.moveItemsBy(indexMid, (CELL_SIZE*deltaXMid, 0))
               
            else:                         # Is item in lower half? 
                deltaXHi = (mid -hi) - 1 
                self.moveItemsBy(indexHi, (CELL_SIZE*deltaXHi, 0))
                hi = mid - 1              # Yes, lower the hi boundary 
                deltaXMid = ((lo- hi) //2) -1
                self.moveItemsBy(indexMid, (CELL_SIZE* deltaXMid, 0))
        
        
        self.stopAnimations()
        self.window.update()
        self.cleanUp(callEnviron)
        return lo                         #val not found 
                
    def makeButtons(self):
        vcmd = (self.window.register(numericValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        findButton = self.addOperation(
            "Find", lambda: self.clickFind(), numArguments=1,
            validationCmd=vcmd)
        insertButton = self.addOperation(
            "Insert", lambda: self.clickInsert(), numArguments=1,
            validationCmd=vcmd)
        deleteValueButton = self.addOperation(
            "Delete", lambda: self.clickDelete(), numArguments=1,
            validationCmd=vcmd)
        newSizeArrayButton = self.addOperation(
            "New", lambda: self.clickNew(), numArguments=1)
        randomFillButton = self.addOperation(
            "Random Fill", lambda: self.randomFill())
        deleteRightmostButton = self.addOperation(
            "Delete Rightmost", lambda: self.removeFromEnd())
        #this makes the pause, play and stop buttons 
<<<<<<< Updated upstream
        self.addAnimationButtons()
        
=======
        self.addAnimationButtons()        
>>>>>>> Stashed changes
        return [findButton, insertButton, deleteValueButton,
                deleteRightmostButton, randomFillButton, newSizeArrayButton]

    def validArgument(self):
        entered_text = self.getArgument()
        if entered_text and entered_text.isdigit():
            val = int(entered_text)
            if val < 100:
                return val
    
    # Button functions
    def clickFind(self):
        val = self.validArgument()
        if val is None:
            self.setMessage("Input value must be an integer from 0 to 99.")
        else:
            result = self.find(val)
            if self.list[result].val == val:
                msg = "Found {}!".format(val)
            else:
                msg = "Value {} not found".format(val)
            self.setMessage(msg)
        self.clearArgument()

    def clickInsert(self):
        val = self.validArgument()
        if val is None:
            self.setMessage("Input value must be an integer from 0 to 99.")
        else:
            if len(self.list) >= self.size:
                self.setMessage("Error! Array is already full.")
            else:
                self.insert(val)
                self.setMessage("Value {} inserted".format(val))
        self.clearArgument()

    def clickDelete(self):
        val = self.validArgument()
        if val is None:
            self.setMessage("Input value must be an integer from 0 to 99.")
        else:
            result = self.remove(val)
            if result:
                msg = "Value {} deleted!".format(val)
            else:
                msg = "Value {} not found".format(val)
            self.setMessage(msg)
        self.clearArgument()
    
    def clickNew(self):
        val = self.validArgument()
        # If the number of cells desired wouldn't fit on the screen, error message
        if val is None or self.window.winfo_width() <= ARRAY_X0 + (val+1) * CELL_SIZE:
            self.setMessage("This array size is too big to display")    
        elif val == 0:
            self.setMessage("This array size is too small")                
        else:
            self.newArraySize(val)        
        self.clearArgument()
    
    def enableButtons(self, enable=True):
        for btn in self.buttons:
            btn.config(state=NORMAL if enable else DISABLED)    
    
    def startAnimations(self):
        self.enableButtons(enable=False)
        super().startAnimations()
            
    def stopAnimations(self):
        super().stopAnimations()
        self.enableButtons(enable=True)
<<<<<<< Updated upstream
        self.argumentChanged()    
    
=======
        self.argumentChanged()        
>>>>>>> Stashed changes
        
if __name__ == '__main__':
    random.seed(3.14159)    # Use fixed seed for testing consistency
    array = OrderedArray()

    array.runVisualization()