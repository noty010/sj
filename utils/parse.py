def parse(cmdlist, file):
    with open(file, "r", encoding="utf-8") as f:
        sql = f.read()
    rawcmd = sql.split(';')
    for cmd in rawcmd:
        cleancmd = cmd.strip()
        if cleancmd: cmdlist.append(cleancmd)