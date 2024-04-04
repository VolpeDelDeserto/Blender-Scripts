import bpy

def print_selected_meshes_over_limit():
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            mesh = obj.data
            num_vertices = len(mesh.vertices)
            if num_vertices > 32767:
                print(f"Mesh '{obj.name}' has {num_vertices} vertices (more than 32767).")

# Run the function to print selected meshes with more than 32767 vertices
print_selected_meshes_over_limit()

#This script iterates over all selected objects in the scene and checks if the object type is a mesh.
# If it is, it counts the number of vertices and prints out the count along with the mesh's name if the number of vertices exceeds 32767.

import bpy

# Get selected objects
selected_objects = bpy.context.selected_objects

# Loop through selected objects
for obj in selected_objects:
    # Check if object is a mesh
    if obj.type == 'MESH':
        # Check if vertices count is less than 32767
        if len(obj.data.vertices) < 32767:
            # Deselect the object
            obj.select_set(False)


#It will deselect any selected mesh objects with fewer than 32767 vertices.
