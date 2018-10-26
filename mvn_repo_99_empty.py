
import re
from flask import Flask, send_file, abort
app = Flask(__name__)

@app.route("/<path:group_path>/<string:artifact_id>/<string:version>/<string:filename>")
def hello_world(group_path, artifact_id, version, filename):
    
    
    # /$groupId[0]/../$groupId[n]/$artifactId/$version/$artifactId-$version-$classifier.$type.$ext
    if not filename.startswith(f"{artifact_id}-{version}"):
        abort(400)
    
    print(f"ending of filename {filename[(len(artifact_id) + len(version) + 1):]}")
    m = re.match(r"(?:-([^.]+))?(?:\.([^.]+))(?:\.(.+))?", filename[(len(artifact_id) + len(version) + 1):])
    
    if not m :
        abort(400)
    
    classifier = m.group(1)
    type = m.group(2)
    ext = m.group(3)
    
    group_id = group_path.replace("/", ".")
    

    if not re.match(r"^999?(?:\.0)?(?:-does-not-exist|-empty|-EMPTY|-exclude|-EXCLUDE)$", version):
        abort(404)

    if type == "pom":
        pom = (  "<project>\n"
                    "  <modelVersion>4.0.0</modelVersion>\n"
                    f"  <groupId>{group_id}</groupId>\n"
                    f"  <artifactId>{artifact_id}</artifactId>\n"
                    f"  <version>{version}</version>\n")
        if classifier :
            pom = pom + f"  <classifier>{classifier}</classifier>\n"
        
        pom = pom + "</project>\n"

        if not ext:
            return pom
        elif ext in ("sha1", "md5"):
            import hashlib
            hash = hashlib.new(ext)
            hash.update(bytearray(pom, "utf-8"))
            return hash.hexdigest()
        elif ext == "asc":
            abort(404)
        else:
            abort(400)
    elif type == "jar":
        if not ext:
            return send_file("empty.jar", attachment_filename=filename)
        elif ext == "sha1":
            return "511847dcab0945d5844c85637434fe76bb180efe"
        elif ext == "md5":
            return "da4d58b358a5ce67f93258a00894aa41"
        elif ext == "asc":
            abort(404)
        else:
            abort(400)

    abort(404)
        
    #return f"group: {group_id}, artifact ID: {artifact_id}, ver: {version}, file: {filename}, type: {type}, classifier: {classifier}"
    
