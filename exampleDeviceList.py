from pulseDevicelist import ffi, lib

# This is where we'll store the input device list
inputDevicelist = ffi.new(pa_devicelist_t,"pa_input_devicelist[16]")

# This is where we'll store the output device list
outputDevicelist = ffi.new(pa_devicelist_t,"pa_output_devicelist[16]")

if (lib.pa_get_devicelist(inputDevicelist,outputDevicelist) < 0):
    print("failed to get device list\n")

for i in range(16):
    if not outputDevicelist[i].initialized:
        break

    print("=======[ Output Device {i} ]=======\n", i)
    print("Description: {s}\n",
          s = outputDevicelist[i].description)
    print("Name: {s}\n", s =  outputDevicelist[i].name)
    print("Index: {d}\n", d =  outputDevicelist[i].index)
    print("\n")

