match (a:Table_aliasContext)-[:connects*]->(b)-[:connects*]->(c:Table_source_itemContext)<-[:connects*]-(d)<-[:connects*]-(e:Table_nameContext)

return a.text,b.text,c.text,d.text,e.text
