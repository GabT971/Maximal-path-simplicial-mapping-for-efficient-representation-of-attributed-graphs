
#to do the link  between vertices and original nodes
"""
SELECT nodes.ID_Nodes,
vertices.vertices
FROM nodes
JOIN Vert_Nodes 
ON nodes.ID_Nodes=Vert_Nodes.ID_Nodes 
JOIN vertices 
ON vertices.ID_V=Vert_Nodes.ID_V;
"""

# to do the link between vertices and simplices
"""
SELECT vertices.vertices,
simplices.simplices
FROM vertices
JOIN Simp_Vert
ON vertices.ID_V=Simp_Vert.ID_V 
JOIN simplices 
ON simplices.ID_S=Simp_Vert.ID_S;
"""