node(api,toskerNodesAPISoftware,c_api).
node(gui,toskerNodesSoftware,c_gui).
node(maven,toskerNodesContainer,c_maven).
node(node,toskerNodesContainer,c_node).
node(mongodb,toskerNodesContainer,c_mongodb).
node(dbvolume,toskerNodesVolume,c_dbvolume).
node(bottom,bottom,c_bottom).

edge(h,api,mongodb).
edge(h,gui,api).
edge(h,mongodb,dbvolume).
edge(h,gui,gui). % self-dependency

edge(v,api,maven).
edge(v,gui,node).
edge(v,maven,bottom).
edge(v,node,bottom).
edge(v,mongodb,bottom).
edge(v,dbvolume,bottom).
