### Inheritance in Python
### Parent Class - Device
### Child Class - Printer
### Printer class knows about Device. But Device doesn't know about printer
### !r --> call __reper__ function for self.name. It will have <> added during output display
### super is used to call Parent class objects/methods
class Device:
    
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
        
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"        ## !r --> call __str__ function for self.name. It will have <> added during output display
    
    def disconnect(self):
        self.connected = False
        print("Disconnected...")
    
## printer = Device("Printer", "USB")
## print(printer)
## printer.disconnect()
## print(printer)

#### Output for above code : Device 'Printer' (USB)
#### Disconnected...
#### Device 'Printer' (USB)

## A printer may have many additional features which are not covered here
## To make use of existing feature that is present for Device Class we will make use of Inheritance

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        ## We can define each object here
        ## But the best way is to make use of the features that is available in Super class (Device)
        super().__init__(name, connected_by)            ## super is used to call Parent class objects/methods
        self.capacity = capacity
        self.remaining_pages = capacity
        
    def __str__(self):
        return f"{super().__str__()} {self.remaining_pages} pages remaining"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages
        

printer = Printer("Ipson Printer", "USB", 100)
print(printer)
printer.print(20)
printer.print(40)
print(printer)
printer.disconnect()
print(printer)
printer.print(10)
print(printer)
