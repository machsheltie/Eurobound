"""Read/write the JSON state block embedded in aa_team_board.html."""
import json, re, sys
P = "aa_team_board.html"
RX = re.compile(r'(<script type="application/json" id="state">)(.*?)(</script>)', re.S)
def load(path=P):
    return json.loads(RX.search(open(path, encoding="utf-8").read()).group(2))
def save(state, path=P):
    src = open(path, encoding="utf-8").read()
    js = json.dumps(state, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    open(path, "w", encoding="utf-8").write(RX.sub(lambda m: m.group(1) + js + m.group(3), src, count=1))
