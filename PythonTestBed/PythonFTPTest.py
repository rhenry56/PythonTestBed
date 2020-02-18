import pycurl
import pathlib

def download_file(url: str, path: pathlib.Path) -> None:
    """Download a single file from a url, save at given path

    Args:
        url:   URL where file will be downloaded from.
        path:  File path where file will be saved.
    """
    
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, mode="wb") as fid:
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, fid)
        c.perform()
        response_code = c.getinfo(c.RESPONSE_CODE)
        if not (200 <= response_code <= 299):
            print(f"There was a problem downloading {c.getinfo(c.EFFECTIVE_URL)} ({response_code})")
        c.close() 
