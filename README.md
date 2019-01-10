# sql-parse-to-neo4j
This demostrates the parsing of T-SQL with ANTLR and puts the parse tree into neo4j with the beginnings of extracting out relational information into a property graph.

You will need to install the ANTLR runtime libraries for python. http://www.antlr.org/download.html

If you want to generate grammars for other languages, you will need to download the ANTLR parser generator which is only java.

There are some very neat integrations with the Intellij platform both for ANTLR and Neo4j. I would recommend using it. It eliminates much of the command line work.

running docker-compose up will spinn up neo4j without mounting the file system and persisting data. The following will mount the file system and will persist data outside the life of a container:

```
docker run --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data --volume=$HOME/neo4j/logs:/logs neo4j
```

When a fresh instance starts, authenticate with neo4j/neo4j and change the password.
