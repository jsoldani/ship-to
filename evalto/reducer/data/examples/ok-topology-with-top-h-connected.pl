node(xx,toskerNodesSoftware,c_xx).
node(zz,toskerNodesSoftware,c_zz).
node(ww,toskerNodesSoftware,c_ww).
node(ss,toskerNodesSoftware,c_ss).
node(yy,toskerNodesContainer,c_yy).
node(vv,toskerNodesContainer,c_vv).
node(rr,bottom,c_rr).

edge(h,xx,ss).
edge(h,zz,ww).
edge(h,ww,xx).

edge(v,xx,yy).
edge(v,zz,yy).
edge(v,ww,vv).
edge(v,ss,vv).
edge(v,yy,rr).
edge(v,vv,rr).
