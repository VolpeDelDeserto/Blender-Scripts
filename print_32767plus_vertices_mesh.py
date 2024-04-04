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