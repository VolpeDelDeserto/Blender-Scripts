import bpy

# Check if there are selected objects
if bpy.context.selected_objects:
    # Loop through selected objects
    for obj in bpy.context.selected_objects:
        # Check if the object is a mesh
        if obj.type == 'MESH':
            # Loop through the object's UV maps
            for uv_map in obj.data.uv_layers:
                # Change UV map name to "UVMap 0"
                uv_map.name = "UVMap 0"
        else:
            print(f"Object '{obj.name}' is not a mesh and will be skipped.")
else:
    print("No objects selected.")
