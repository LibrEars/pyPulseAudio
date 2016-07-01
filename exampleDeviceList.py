from DeviceList import ffi, lib

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
          + ffi.string(outputDevicelist[i].description).decode('utf8') + "\n" 
          + "Name: " 
          + ffi.string(outputDevicelist[i].name).decode('utf8') + "\n" 
          + "Index: " + str(outputDevicelist[i].index))

for i in range(16):
    if inputDevicelist[i].initialized == 0:
        break

    print("\n=======[ Input Device #" + str(i+1) + " ]=======\n"
          + "Description: " 
          + ffi.string(inputDevicelist[i].description).decode('utf8') + "\n" 
          + "Name: " 
          + ffi.string(inputDevicelist[i].name).decode('utf8') + "\n" 
          + "Index: " + str(inputDevicelist[i].index) + "\n")

