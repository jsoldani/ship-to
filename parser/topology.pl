node(api,tosker.nodes.APISoftware,c_api).
node(gui,tosker.nodes.Software,c_gui).
node(maven,tosker.nodes.Container,c_maven).
node(node,tosker.nodes.Container,c_node).
node(mongodb,tosker.nodes.Container,c_mongodb).
node(dbvolume,tosker.nodes.Volume,c_dbvolume).

edge(h,api,mongodb).
edge(h,gui,api).
edge(h,mongodb,dbvolume).

edge(v,api,maven).
edge(v,gui,node).
