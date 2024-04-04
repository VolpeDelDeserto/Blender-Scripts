import bpy

def print_selected_mesh_vertices():
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            mesh = obj.data
            num_vertices = len(mesh.vertices)
            print(f"Mesh '{obj.name}' has {num_vertices} vertices.")

# Run the function to print vertices for selected meshes
print_selected_mesh_vertices()

#This script iterates over all selected objects in the scene and checks if the object type is a mesh.
# If it is, it counts the number of vertices and prints out the count along with the mesh's name.