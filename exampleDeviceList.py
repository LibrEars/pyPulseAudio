#from cffi import FFI
from DeviceList import ffi, lib
#ffi = FFI()

#lib = ffi.dlopen('pulse')

# This is where we'll store the input device list
inputDevicelist = ffi.new("pa_devicelist_t pa_input_devicelist[16]")

# This is where we'll store the output device list
outputDevicelist = ffi.new("pa_devicelist_t pa_output_devicelist[16]")

if (lib.pa_get_devicelist(inputDevicelist,outputDevicelist) < 0):
    print("failed to get device list\n")

for i in range(16):
    if outputDevicelist[i].initialized == 0:
        break

    print("\n=======[ Output Device #" + str(i+1) + " ]=======\n" 
          + "Description: " 
          + str(ffi.string(outputDevicelist[i].description)) + "\n" 
          + "Name: " 
          + str(ffi.string(outputDevicelist[i].name)) + "\n" 
          + "Index: " + str(outputDevicelist[i].index))

for i in range(16):
    if inputDevicelist[i].initialized == 0:
        break

    print("\n=======[ Input Device #" + str(i+1) + " ]=======\n"
          + "Description: " 
          + str(ffi.string(inputDevicelist[i].description)) + "\n" 
          + "Name: " 
          + str(ffi.string(inputDevicelist[i].name)) + "\n" 
          + "Index: " + str(inputDevicelist[i].index) + "\n")

