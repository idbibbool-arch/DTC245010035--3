with open("docker-compose.yml", "r") as f:
    content = f.read()

old_block = """  mysql_exporter:
    image: prom/mysqld-exporter:v0.15.1
    container_name: mysql_exporter
    restart: unless-stopped
    user: "65534:65534"
    depends_on:
      - mysql_db
    networks:
      - monitoring_net"""

new_block = """  mysql_exporter:
    image: prom/mysqld-exporter:v0.15.1
    container_name: mysql_exporter
    restart: unless-stopped
    environment:
      DATA_SOURCE_NAME: "root:Root@Str0ngP@ssw0rd2026!@(mysql_db:3306)/"
    depends_on:
      - mysql_db
    networks:
      - monitoring_net
      - backend_net"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open("docker-compose.yml", "w") as f:
        f.write(content)
    print("Updated successfully")
else:
    print("Pattern not matched, manual check needed")
